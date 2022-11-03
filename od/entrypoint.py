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
from od.utils.data import wheat

@hydra.main(config_path = "./", config_name = "config.yaml", version_base= None)
def main(config: DictConfig):
    logging.info(pformat(dict(config)))
    train = wheat.load_csv_annotations(config)
    logging.info(pformat(train.head()))

    


if __name__ ==  "__main__":
    main()
