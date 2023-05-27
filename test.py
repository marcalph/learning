import numpy as np
import matplotlib.pyplot as plt

image =np.random.rand(1280,720,3) * 255

print(image.shape)
plt.imshow(image)
plt.show()
