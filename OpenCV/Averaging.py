import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Screenshot from 2020-04-25 22-41-14.png')

blur = cv2.blur(img,(6,6))

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()