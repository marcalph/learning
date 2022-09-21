""" torch typing example
"""

import torch

from torch import rand

from torchtyping import TensorType, patch_typeguard
from typeguard import typechecked

from pprint import pprint
patch_typeguard()  # use before @typechecked

@typechecked
def func(x: TensorType["batch", 2, torch.float32, torch.strided],
         y: TensorType["batch",-1]) -> TensorType["batch",-1]:
    return x + y

pprint(func(rand(3,2), rand(3,1)))  # works
# pprint(func(rand(3,2), rand(1)))  # failes purposely