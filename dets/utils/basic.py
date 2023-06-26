import importlib
from typing import Any, List, Dict
import torch
import shutil
from omegaconf import DictConfig
import numpy as np 
import os
import random
import hydra
from itertools import product
from od.utils.data.wheat import WheatDataset

from typing import List
# https://github.com/quantumblacklabs/kedro/blob/9809bd7ca0556531fa4a2fc02d5b2dc26cf8fa97/kedro/utils.py
def load_obj(obj_path: str, default_obj_path: str = "") -> Any:
    """Extract an object from a given path.
    Args:
        obj_path: Path to an object to be extracted, including the object name.
        default_obj_path: Default object path.
    Returns:
        Extracted object.
    Raises:
        AttributeError: When the object does not have the given named attribute.
    """
    obj_path_list = obj_path.rsplit(".", 1)
    obj_path = obj_path_list.pop(0) if len(obj_path_list) > 1 else default_obj_path
    obj_name = obj_path_list[0]
    module_obj = importlib.import_module(obj_path)
    if not hasattr(module_obj, obj_name):
        raise AttributeError(f"Object `{obj_name}` cannot be loaded from `{obj_path}`.")
    return getattr(module_obj, obj_name)


def set_seed(seed: int = 666):
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def save_useful_info():
    shutil.copytree(
        os.path.join(hydra.utils.get_original_cwd(), "src"),
        os.path.join(os.getcwd(), "code/src"),
    )
    shutil.copy2(
        os.path.join(hydra.utils.get_original_cwd(), "hydra_run.py"),
        os.path.join(os.getcwd(), "code"),
    )


def collate_fn(batch):
    return tuple(zip(*batch))

def product_dict(**kwargs):
    """
    Convert dict with lists in values into lists of all combinations

    This is necessary to convert config with experiment values
    into format usable by hydra
    Args:
        **kwargs:

    Returns:
        list of lists

    ---
    Example:
        >>> list_dict = {'a': [1, 2], 'b': [2, 3]}
        >>> list(product_dict(**list_dict))
        >>> [['a=1', 'b=2'], ['a=1', 'b=3'], ['a=2', 'b=2'], ['a=2', 'b=3']]

    """
    keys = kwargs.keys()
    vals = kwargs.values()
    for instance in product(*vals):
        zip_list = list(zip(keys, instance))
        yield [f"{i}={j}" for i, j in zip_list]


def config_to_hydra_dict(cfg: DictConfig) -> Dict:
    """
    Convert config into dict with lists of values, where key is full name of parameter

    This fuction is used to get key names which can be used in hydra.

    Args:
        cfg:

    Returns:

    """
    experiment_dict = {}
    for k, v in cfg.items():
        for k1, v1 in v.items():
            experiment_dict[f"{k}.{k1}"] = v1

    return experiment_dict



from omegaconf import OmegaConf
import collections
import pandas as pd


def flatten_omegaconf(d, sep="_"):

    d = OmegaConf.to_container(d)

    obj = collections.OrderedDict()

    def recurse(t, parent_key=""):

        if isinstance(t, list):
            for i in range(len(t)):
                recurse(t[i], parent_key + sep + str(i) if parent_key else str(i))
        elif isinstance(t, dict):
            for k, v in t.items():
                recurse(v, parent_key + sep + k if parent_key else k)
        else:
            obj[parent_key] = t

    recurse(d)
    obj = {k: v for k, v in obj.items() if type(v) in [int, float]}
    # obj = {k: v for k, v in obj.items()}

    return obj




from sklearn.model_selection import train_test_split

def get_training_datasets(cfg: DictConfig) -> dict:
    """
    Get datases for modelling

    Args:
        cfg: config

    Returns:

    """

    train = pd.read_csv(f"{cfg.data.folder_path}/train.csv")

    train[["x", "y", "w", "h"]] = pd.DataFrame(
        np.stack(train["bbox"].apply(lambda x: ast.literal_eval(x)))
    ).astype(np.float32)

    # precalculate some values
    train["x1"] = train["x"] + train["w"]
    train["y1"] = train["y"] + train["h"]
    train["area"] = train["w"] * train["h"]
    train_ids, valid_ids = train_test_split(
        train["image_id"].unique(), test_size=0.1, random_state=cfg.training.seed
    )

    # for fast training
    if cfg.training.debug:
        train_ids = train_ids[:10]
        valid_ids = valid_ids[:10]

    train_df = train.loc[train["image_id"].isin(train_ids)]
    valid_df = train.loc[train["image_id"].isin(valid_ids)]

    train_img_dir = f"{cfg.data.folder_path}/train"

    # initialize augmentations
    train_augs_list = [
        load_obj(i["class_name"])(**i["params"])
        for i in cfg["augmentation"]["train"]["augs"]
    ]
    train_bbox_params = OmegaConf.to_container(
        (cfg["augmentation"]["train"]["bbox_params"])
    )
    train_augs = A.Compose(train_augs_list, bbox_params=train_bbox_params)

    valid_augs_list = [
        load_obj(i["class_name"])(**i["params"])
        for i in cfg["augmentation"]["valid"]["augs"]
    ]
    valid_bbox_params = OmegaConf.to_container(
        (cfg["augmentation"]["valid"]["bbox_params"])
    )
    valid_augs = A.Compose(valid_augs_list, bbox_params=valid_bbox_params)

    train_dataset = WheatDataset(train_df, "train", train_img_dir, cfg, train_augs)

    valid_dataset = WheatDataset(valid_df, "valid", train_img_dir, cfg, valid_augs)

    return {"train": train_dataset, "valid": valid_dataset}
