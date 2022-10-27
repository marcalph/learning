import hydra
from omegaconf import DictConfig
from PIL import Image
import numpy as np
from utils.data.pennfudan import PennFudanDataset

@hydra.main(config_name = "config.yaml")
def main(config: DictConfig):
    print(config)

    ds = PennFudanDataset("/Users/marcalph/Projects/learning/data/PennFudanPed", transforms = None)
    ds[0][0].show()
    pass


if __name__ ==  "__main__":
    main()
