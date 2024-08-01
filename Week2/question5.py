# implement gray level slicing

import cv2 as cv
import numpy as np

img = cv.imread('images/cat.jpg', 0)

low_threshold = 100
high_threshold = 150

# Create a binary mask where pixel values in the specified range are set to 255
# and the rest are set to 0
mask = np.zeros_like(img)
mask[(img >= low_threshold) & (img <= high_threshold)] = 255

cv.imshow('Original Image', img)
cv.imshow('Gray Level Slicing', mask)

cv.waitKey(0)
cv.destroyAllWindows()

output_path = 'images/gray_level_sliced_cat.jpg'
cv.imwrite(output_path, mask)
