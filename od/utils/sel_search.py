""" Slective search
Selective Search algorithm over-segments an image via:
    color similarity: 25-bin histogram for each channel of an image sim is histogram intersection dist.
    texture similarity:  Gaussian derivatives at 8 orientations per channel histogram intersection is once again used.
    size similarity: smaller regiuosn merge early on
    shape similarity: merge touching and compatible blocks (fitting togetehgr)
    meta-similarity measure: A final meta-similarity acts as a linear combination
"""

import skimage
import selective_search

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

image = skimage.data.astronaut()
fig, ax = plt.subplots(figsize=(6, 6))
ax.imshow(image)
plt.show()


boxes = selective_search.selective_search(image, mode="fast")

boxes_filter = selective_search.box_filter(
    boxes, min_size=20, topN=80
)  # drawing rectangles on the original image
fig, ax = plt.subplots(figsize=(6, 6))
ax.imshow(image)
for x1, y1, x2, y2 in boxes_filter:
    bbox = mpatches.Rectangle(
        (x1, y1), (x2 - x1), (y2 - y1), fill=False, edgecolor="green", linewidth=1
    )
    ax.add_patch(bbox)
plt.axis("off")
plt.show()
