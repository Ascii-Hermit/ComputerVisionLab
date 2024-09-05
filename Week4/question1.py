# unsharp masking

import cv2
import numpy as np

# Load the image
image = cv2.imread('images/cat.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Original', image)
kernel_size=(5, 5)
sigma=1.0
amount=1.0
threshold=0

# Step 1: Apply Gaussian Blur to the image
# Step 2: Subtract the blurred image from the original image (the mask)
# Step 3: Add the mask back to the original image

blurred = cv2.GaussianBlur(image, kernel_size, sigma) # remember the parameters

mask = cv2.subtract(image, blurred)

sharpened_image = cv2.addWeighted(image, 1.0 , mask, amount, 0) # this function is used to merge two images
# Parameters (src1, weight_src1, src2, weight_src2, gamma) , Note that gamma is used to add a constant to the final weighted sum


cv2.imwrite('sharpened_image.jpg', sharpened_image)
cv2.imshow('Unsharp Masking', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
