import hydra
from omegaconf import DictConfig
from PIL import Image
import numpy as np
from torch.utils.data import DataLoader
import torchvision
import torch
import torch.utils as utils
import matplotlib.pyplot as plt
import pandas as pd
import logging
from pprint import pformat
from utils.data import wheat
from utils.viz import plot_image_bboxes

# store annotations in pandas
@hydra.main(config_path = "./", config_name = "config.yaml", version_base= None)
def main(config: DictConfig):
    logging.info(pformat(dict(config)))
    train = wheat.load_csv_annotations(config)
    logging.info("\n"+pformat(train.head()))
    logging.info(f"There are {train['image_id'].nunique()} unique images in train data")
    logging.info(f"There are {train.shape[0]} bboxes in train data")
    plt.hist(train['area'], bins=50)
    plt.title('Area value distribution')
    plt.show()
    plot_image_bboxes(train)






 


if __name__ ==  "__main__":
    main()
