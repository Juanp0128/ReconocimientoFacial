import numpy as np
import matplotlib.pyplot as plt

from skimage import data
from skimage.color import rgb2gray

original = data.astronaut()

print (type(original))


grayscale = rgb2gray(original)

fig, axes = plt.subplots(2, 2, figsize=(8, 4))
ax = axes.ravel()

ax[0].imshow(original[:, :, :])
ax[0].set_title("Original")
ax[1].imshow(original[:, :, 0])
ax[1].set_title("Original roja")
ax[2].imshow(original[:, :, 1])
ax[2].set_title("Original verde")
ax[3].imshow(original[:, :, 2])
ax[3].set_title("Original azul")
#ax[3].imshow(grayscale, cmap=plt.cm.gray)
#ax[3].set_title("Grayscale")

fig.tight_layout()
plt.show()
