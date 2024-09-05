# getting the gradient of an image

import cv2
import numpy as np

image = cv2.imread('images/cat.jpg', cv2.IMREAD_GRAYSCALE)

# parameters(src, data_type of image, dx, dy, kernel_size)
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  # x direction
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)  # y direction

magnitude = np.sqrt(sobelx**2 + sobely**2)

# we do the below operations to convert image to an 8-bit format (0-255 range)
sobelx_abs = cv2.convertScaleAbs(sobelx)
sobely_abs = cv2.convertScaleAbs(sobely)
magnitude_abs = cv2.convertScaleAbs(magnitude)

cv2.imshow('Original Image', image)
cv2.imshow('Sobel X Gradient', sobelx_abs)
cv2.imshow('Sobel Y Gradient', sobely_abs)
cv2.imshow('Gradient Magnitude', magnitude_abs)

cv2.imwrite('images/gradient_magnitude.jpg', magnitude_abs)

cv2.waitKey(0)
cv2.destroyAllWindows()
