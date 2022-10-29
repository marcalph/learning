import hydra
from omegaconf import DictConfig
from PIL import Image
import numpy as np
from utils.data.pennfudan import PennFudanDataset, get_transforms
from torch.utils.data import DataLoader
import torchvision
import torch
import torch.utils as utils
import matplotlib.pyplot as plt

@hydra.main(config_path = "./", config_name = "config.yaml", version_base= None)
def main(config: DictConfig):
    print(config)
    ds = PennFudanDataset("/Users/marcalph/Projects/learning/data/PennFudanPed", get_transforms(train=None))
    plt.imshow(ds[0][0].permute(1, 2, 0))  # type: ignore
    plt.show()
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(weights="DEFAULT")
    data_loader = DataLoader(
        ds, batch_size=1, shuffle=True, num_workers=4)
    # For Training
    images,targets = next(iter(data_loader))
    images = list(image for image in images)
    print(targets)
    # targets = [{k: v for k, v in t.items()} for t in targets]
    output = model(images,targets)   # Returns losses and detections
    print(output)
    # For inference
    model.eval()
    x = [torch.rand(3, 300, 400), torch.rand(3, 500, 400)]
    predictions = model(x)
    print(predictions)


if __name__ ==  "__main__":
    main()
