from torchvision import transforms  # type: ignore
import torch
import numpy as np
import numpy.typing as npt
from typing import Any
from PIL.Image import Image
import selective_search  # type: ignore

device = "cuda" if torch.cuda.is_available() else "cpu"
normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])


def preprocess_image(img: Image) -> torch.Tensor:
    img_t: torch.Tensor = torch.Tensor(img).permute(2, 0, 1)
    img_t = normalize(img_t)
    return img_t.to(device).float()


def decode(_y):
    _, preds = _y.max(-1)
    return preds


def extract_candidates(img):
    img_lbl, regions = selective_search.selective_search(img, mode="fast")
    img_area = np.prod(img.shape[:2])
    candidates = []
    for r in regions:
        if r["rect"] in candidates:
            continue
        if r["size"] < (0.05 * img_area):
            continue
        if r["size"] > (1 * img_area):
            continue
        x, y, w, h = r["rect"]
        candidates.append(list(r["rect"]))
    return candidates
