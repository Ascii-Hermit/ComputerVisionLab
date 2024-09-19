import cv2
import numpy as np

# Load an image (replace 'image.jpg' with the path to your image)
image = cv2.imread('images/cat.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ===== Basic Thresholding =====
# Apply basic thresholding
# The second argument is the threshold value
# The third argument is the maximum value to use for the output image
# The type of thresholding is cv2.THRESH_BINARY
_, basic_threshold = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# ===== Adaptive Thresholding =====
# Apply adaptive thresholding
# Parameters:
#  - Block size: Size of the local region used to calculate the threshold
#  - C: Constant subtracted from the mean or weighted mean
adaptive_threshold = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# ===== Otsu's Thresholding =====
# Apply Otsu's thresholding
# The second argument cv2.THRESH_OTSU tells OpenCV to use Otsu's method to determine the optimal threshold value
_, otsu_threshold = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# ===== Display Results =====s
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)
cv2.imshow('Basic Thresholding', basic_threshold)
cv2.imshow('Adaptive Thresholding', adaptive_threshold)
cv2.imshow('Otsu Thresholding', otsu_threshold)

# Wait until a key is pressed and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
