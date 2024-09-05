# color segmentation

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('images/cat.jpg')

# This makes it easier to focus on color segmentation without being affected by lighting or intensity
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_bound = np.array([0, 100, 100])   # red lower bound
upper_bound = np.array([10, 255, 255])  # red upper bound

# binsry mask to see the values within range 
mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

# apply and to suppress unimportant regions
segmented_image = cv2.bitwise_and(image, image, mask=mask)

plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(mask, cmap='gray')
plt.title('Mask')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGB))
plt.title('Segmented Image')
plt.axis('off')

plt.tight_layout()
plt.show()
