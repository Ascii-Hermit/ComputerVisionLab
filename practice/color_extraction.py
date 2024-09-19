import cv2
import numpy as np

# Load an image (replace 'image.jpg' with the path to your image)
image = cv2.imread('images/cat.jpg',1)
# Convert the image from BGR to RGB format

# Get the RGB value of a specific pixel (e.g., pixel at row 100, column 150)
(b, g, r) = image[100, 150]
print(f"RGB value at pixel (100, 150): Red: {r}, Green: {g}, Blue: {b}")
cv2.imshow('Original',image)

zeros = np.zeros_like(image[:, :, 0]) # this is important

# Extract the R, G, and B channels for the entire image
red_image =  np.stack([zeros, zeros, image[:,:,0]], axis=2)
green_image =  np.stack([zeros, image[:,:,1], zeros], axis=2)
blue_image = np.stack([image[:,:,2], zeros, zeros], axis=2)

# Display the R, G, and B images separately
cv2.imshow('Red image', red_image)
cv2.imshow('Green image', green_image)
cv2.imshow('Blue image', blue_image)

# Example: Print the RGB value of the first pixel (top-left corner)
print(f"RGB value of the first pixel (0, 0): Red: {red_image[0, 0]}, Green: {green_image[0, 0]}, Blue: {blue_image[0, 0]}")

# Wait until a key is pressed and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
