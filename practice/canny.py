import cv2
import numpy as np

# Load an image (replace 'image.jpg' with the path to your image)
image = cv2.imread('images/cat.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ===== Canny Edge Detection =====
# Apply Gaussian blur to the grayscale image to reduce noise
blurred = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Apply the Canny edge detector
# The two thresholds are for the hysteresis procedure
# The lower threshold is 50, and the higher threshold is 150
edges = cv2.Canny(blurred, 50, 150)

# ===== Display Results =====
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)
cv2.imshow('Canny Edges', edges)

# Wait until a key is pressed and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
