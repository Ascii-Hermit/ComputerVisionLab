# implement contrast stretching

import cv2 as cv
import numpy as np

img_path = 'Week2/images/cat.jpg'
img = cv.imread(img_path, 0)

# Define the (Rmin, Smin) minimum and (Rmax, Smax) maximum pixel values for the original and stretched image
R_min, R_max = 60, 180
S_min, S_max = 100, 110

# Apply contrast stretching
# Formula: S = ((R - R_min) * (S_max - S_min) / (R_max - R_min)) + S_min
stretched_img = ((img - R_min) * (S_max - S_min) / (R_max - R_min) + S_min).astype(np.uint8)

cv.imshow('Original Image', img)
cv.imshow('Contrast Stretched Image', stretched_img)

cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite('images/contrast_stretched_cat.jpg', stretched_img)


