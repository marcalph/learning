
from torch.utils.data import Dataset
from omegaconf import DictConfig
import pandas as pd
from albumentations.core.composition import Compose
import torch 
import cv2
import omegaconf
import numpy as np
import ast
import os
import pytorch_lightning as pl

def load_csv_annotations(config: omegaconf.DictConfig):
    train = pd.read_csv(f'{config.data.folder_path}/train.csv')
    train[['x', 'y', 'w', 'h']] = pd.DataFrame(
        np.stack(train['bbox'].apply(lambda x: ast.literal_eval(x)))).astype(np.float32)
    # precalculate some values
    train['x1'] = train['x'] + train['w']
    train['y1'] = train['y'] + train['h']
    train['area'] = train['w'] * train['h']
    return train




class WheatDataset(Dataset):

    def __init__(self,
                 dataframe: pd.DataFrame = None,
                 mode: str = 'train',
                 image_dir: str = '',
                 cfg: DictConfig = None,
                 transforms: Compose = None):
        """
        Prepare data for wheat competition.

        Args:
            dataframe: dataframe with image id and bboxes
            mode: train/val/test
            cfg: config with parameters
            image_dir: path to images
            transforms: albumentations
        """
        self.image_dir = image_dir
        self.df = dataframe
        self.mode = mode
        self.cfg = cfg
        self.image_ids = os.listdir(self.image_dir) if self.df is None else self.df['image_id'].unique()
        self.transforms = transforms

    def __getitem__(self, idx: int):
        image_id = self.image_ids[idx].split('.')[0]
        # print(image_id)
        image = cv2.imread(f'{self.image_dir}/{image_id}.jpg', cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB).astype(np.float32)

        # normalization.
        # TO DO: refactor preprocessing
        image /= 255.0

        # test dataset must have some values so that transforms work.
        target = {'labels': torch.as_tensor([[0]], dtype=torch.float32),
                  'boxes': torch.as_tensor([[0, 0, 0, 0]], dtype=torch.float32)}

        # for train and valid test create target dict.
        if self.mode != 'test':
            image_data = self.df.loc[self.df['image_id'] == image_id]
            boxes = image_data[['x', 'y', 'x1', 'y1']].values

            areas = image_data['area'].values
            areas = torch.as_tensor(areas, dtype=torch.float32)

            # there is only one class
            labels = torch.ones((image_data.shape[0],), dtype=torch.int64)
            iscrowd = torch.zeros((image_data.shape[0],), dtype=torch.int64)

            target['boxes'] = boxes
            target['labels'] = labels
            target['image_id'] = torch.tensor([idx])
            target['area'] = areas
            target['iscrowd'] = iscrowd

            if self.transforms:
                image_dict = {
                    'image': image,
                    'bboxes': target['boxes'],
                    'labels': labels
                }
                image_dict = self.transforms(**image_dict)
                image = image_dict['image']
                target['boxes'] = torch.as_tensor(image_dict['bboxes'], dtype=torch.float32)

        else:
            image_dict = {
                'image': image,
                'bboxes': target['boxes'],
                'labels': target['labels']
            }
            image = self.transforms(**image_dict)['image']

        return image, target, image_id

    def __len__(self) -> int:
        return len(self.image_ids)




class LitWheat(pl.LightningModule):
    def __init__(self, hparams: DictConfig | None = None, cfg: DictConfig | None = None, model = None):
        super(LitWheat, self).__init__()
        self.cfg = cfg
        self.hparams = hparams
        self.model = model

    def forward(self, x, *args, **kwargs):
        return self.model(x)

    def prepare_data(self):
        datasets = get_training_datasets(self.cfg)
        self.train_dataset = datasets['train']
        self.valid_dataset = datasets['valid']

    def train_dataloader(self):
        train_loader = torch.utils.data.DataLoader(self.train_dataset,
                                                   batch_size=self.cfg.data.batch_size,
                                                   num_workers=self.cfg.data.num_workers,
                                                   shuffle=True,
                                                   collate_fn=collate_fn)
        return train_loader

    def val_dataloader(self):
        valid_loader = torch.utils.data.DataLoader(self.valid_dataset,
                                                   batch_size=self.cfg.data.batch_size,
                                                   num_workers=self.cfg.data.num_workers,
                                                   shuffle=False,
                                                   collate_fn=collate_fn)

        # prepare coco evaluator
#         coco = get_coco_api_from_dataset(valid_loader.dataset)
#         iou_types = _get_iou_types(self.model)
#         self.coco_evaluator = CocoEvaluator(coco, iou_types)

        return valid_loader

    def configure_optimizers(self):
        if 'decoder_lr' in self.cfg.optimizer.params.keys():
            params = [
                {'params': self.model.decoder.parameters(), 'lr': self.cfg.optimizer.params.lr},
                {'params': self.model.encoder.parameters(), 'lr': self.cfg.optimizer.params.decoder_lr},
            ]
            optimizer = load_obj(self.cfg.optimizer.class_name)(params)

        else:
            optimizer = load_obj(self.cfg.optimizer.class_name)(self.model.parameters(), **self.cfg.optimizer.params)
        scheduler = load_obj(self.cfg.scheduler.class_name)(optimizer, **self.cfg.scheduler.params)

        return [optimizer], [{"scheduler": scheduler,
                              "interval": self.cfg.scheduler.step,
                              'monitor': self.cfg.scheduler.monitor}]

    def training_step(self, batch, batch_idx):
        images, targets, image_ids = batch
        targets = [{k: v for k, v in t.items()} for t in targets]
        # separate losses
        loss_dict = self.model(images, targets)
        # total loss
        losses = sum(loss for loss in loss_dict.values())

        return {'loss': losses, 'log': loss_dict, 'progress_bar': loss_dict}

    def validation_step(self, batch, batch_idx):
        images, targets, image_ids = batch
        targets = [{k: v for k, v in t.items()} for t in targets]
        outputs = self.model(images, targets)
        res = {target["image_id"].item(): output for target, output in zip(targets, outputs)}
#         self.coco_evaluator.update(res)

        return {}

    def validation_epoch_end(self, outputs):
#         self.coco_evaluator.accumulate()
#         self.coco_evaluator.summarize()
#         # coco main metric
#         metric = self.coco_evaluator.coco_eval['bbox'].stats[0]
        metric = 0
        tensorboard_logs = {'main_score': metric}
        return {'val_loss': metric, 'log': tensorboard_logs, 'progress_bar': tensorboard_logs}
