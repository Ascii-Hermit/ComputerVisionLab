import cv2
import numpy as np

# Load an image (replace 'image.jpg' with the path to your image)
image = cv2.imread('images/cat.jpg')

# ===== Resize the image =====
# Resize the image to 300x300 pixels
resized_image = cv2.resize(image, (300, 300))

# ===== Crop the image =====
# Crop a region from (100, 100) to (400, 400) in the original image
cropped_image = image[100:400, 100:400]

# ===== Rotate the image =====
# Get the image dimensions (height and width)
(h, w) = image.shape[:2]

# Define the center of the image for rotation
center = (w // 2, h // 2)

# Define the rotation matrix (rotate by 45 degrees)
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)  # 45 degrees, scale = 1.0

# Apply the rotation to the image
rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))

# Display all the images
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resized_image)
cv2.imshow('Cropped Image', cropped_image)
cv2.imshow('Rotated Image', rotated_image)

# Wait until a key is pressed and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
