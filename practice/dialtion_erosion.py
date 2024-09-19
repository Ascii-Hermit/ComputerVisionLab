import cv2
import numpy as np

# Load an image (replace 'image.jpg' with the path to your image)
image = cv2.imread('images/text.png')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply binary thresholding to convert the grayscale image to binary
_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY_INV)

# Define a kernel (structuring element) for the morphological operations
# A 5x5 rectangular kernel is commonly used
kernel = np.ones((5, 5), np.uint8)

# ===== Dilation =====
# Dilation adds pixels to the boundary of objects in the image
dilated_image = cv2.dilate(binary_image, kernel, iterations=1)

# ===== Erosion =====
# Erosion removes pixels on object boundaries
eroded_image = cv2.erode(binary_image, kernel, iterations=1)

# ===== Display Results =====
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)
cv2.imshow('Binary Image', binary_image)
cv2.imshow('Dilated Image', dilated_image)
cv2.imshow('Eroded Image', eroded_image)

# Wait until a key is pressed and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
