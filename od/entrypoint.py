import hydra
from omegaconf import DictConfig
from PIL import Image
import numpy as np
from torch.utils.data import DataLoader
import torchvision
import torch
import matplotlib.pyplot as plt
import pandas as pd
import logging
from pprint import pformat
from utils.data import wheat
from utils.viz import plot_image_bboxes
import utils.config
from utils.basic import load_obj
from omegaconf import OmegaConf
import albumentations as A
from utils.data.wheat import WheatDataset

# store annotations in pandas
@hydra.main(config_path="./", config_name="config.yaml", version_base=None)
def main(config: DictConfig):
    if config.get("print_config"):
        utils.config.print_config(config, resolve=True)
    train = wheat.load_csv_annotations(config)
    logging.info("\n" + pformat(train.head()))
    logging.info(f"There are {train['image_id'].nunique()} unique images in train data")
    logging.info(f"There are {train.shape[0]} bboxes in train data")
    plt.hist(train["area"], bins=50)
    plt.title("Area value distribution")
    plt.show()
    plot_image_bboxes(train)
    valid_augs_list = [
        load_obj(i["class_name"])(**i["params"])
        for i in config["augmentation"]["valid"]["augs"]
    ]
    valid_bbox_params = OmegaConf.to_container(
        (config["augmentation"]["valid"]["bbox_params"])
    )
    valid_augs = A.Compose(valid_augs_list, bbox_params=valid_bbox_params)
    print(valid_augs)
    test_img_dir = f"{config.data.folder_path}/test"
    test_dataset = WheatDataset(None, "test", test_img_dir, config, valid_augs)
    print(test_dataset)


if __name__ == "__main__":
    main()
