# compare box and gaussian blur


import cv2
import numpy as np

# Load the image
image = cv2.imread('images/cat.jpg', 0)

kernel_size = (9, 9)  # we'll keep the kernel size same

# parameter (src, kernel_size)
box_filtered = cv2.blur(image, kernel_size)

# parameter (src, kernel_size ,sigma)
gaussian_filtered = cv2.GaussianBlur(image, kernel_size, 0)

cv2.imshow('Original Image', image)
cv2.imshow('Box Filter Output', box_filtered)
cv2.imshow('Gaussian Filter Output', gaussian_filtered)

cv2.imwrite('images/box_filtered.jpg', box_filtered)
cv2.imwrite('images/gaussian_filtered.jpg', gaussian_filtered)

cv2.waitKey(0)
cv2.destroyAllWindows()
