import os
from typing import Any
from pytorch_lightning.utilities.types import STEP_OUTPUT
import torch
from torch import nn
import torch.nn.functional as F
from torchvision import transforms
from torchvision.datasets import MNIST
from torch.utils.data import DataLoader
import pytorch_lightning as pl
import torchvision.models as models


class FlashClassifier(pl.LightningModule):
    def __init__(self):
        super().__init__()
        backbone = models.resnet18(weights="DEFAULT")
        layers = list(backbone.children())[:-1]
        num_filters = backbone.fc.in_features
        num_target_classes = 2
        self.feature_extractor = nn.Sequential(*layers)
        self.clf = nn.Linear(num_filters, num_target_classes)

    def forward(self, x):
        self.feature_extractor.eval()
        with torch.no_grad():
            representations = self.feature_extractor(x).flatten(1)
        x = self.clf(representations)
    
    def training_step(self, *args: Any, **kwargs: Any) -> STEP_OUTPUT:
        return super().training_step(*args, **kwargs)