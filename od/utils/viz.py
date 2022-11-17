import pandas as pd
import cv2
import matplotlib.pyplot as plt



def plot_image_bboxes(df:pd.DataFrame):
    img_id = df.image_id.sample(1)
    image = cv2.imread(f'/datasets/wheat/train/{img_id}.jpg', cv2.IMREAD_COLOR)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB).astype(np.float32)
    bboxes = df.loc[df['image_id'] == str(img_id), ['x', 'y1', 'x1', 'y']].values
    fig, ax = plt.subplots(1, 1, figsize=(16, 8))
    for box in bboxes:
        cv2.rectangle(image,
                      (box[0], box[1]),
                      (box[2], box[3]),
                      (220, 0, 0), 3)
    ax.set_axis_off()
    ax.imshow(image / 255)