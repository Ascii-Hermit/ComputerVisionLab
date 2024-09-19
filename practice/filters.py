import cv2
import numpy as np

# Load an image (replace 'image.jpg' with the path to your image)
image = cv2.imread('images/cat.jpg')

# Convert the image to grayscale (for Sobel and Laplacian filters)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ===== Gaussian Blur =====
# Applies Gaussian Blur to smooth the image and reduce noise
# The second argument (5, 5) is the kernel size, and the third is the standard deviation
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)

# ===== Median Filter =====
# Applies the median filter to remove salt-and-pepper noise
# The second argument 5 is the size of the kernel
median_filter = cv2.medianBlur(image, 5)

# ===== Sobel Operator =====
# Detects edges using the Sobel operator in both x and y directions
# We use cv2.CV_64F to capture negative slopes, dx=1 and dy=0 for x gradient
sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)  # Sobel X
sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)  # Sobel Y
# Combine the two gradients to get the overall edge magnitude
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# ===== Laplacian Filter =====
# The Laplacian filter enhances edges by calculating the second derivative
laplacian_filter = cv2.Laplacian(gray_image, cv2.CV_64F, ksize=3)

# ===== Unsharp Masking (Sharpening) =====
# First, apply a Gaussian blur to the image
blurred = cv2.GaussianBlur(image, (9, 9), 10.0)
# Then, subtract the blurred image from the original to create a mask
unsharp_mask = cv2.addWeighted(image, 1.5, blurred, -0.5, 0)

# ===== Box Filter =====
# The box filter blurs the image by averaging the values in the kernel
# The second argument (5, 5) is the size of the kernel
box_filter = cv2.boxFilter(image, -1, (5, 5))  # Alternatively: cv2.blur(image, (5, 5))

# ===== Display Results =====
cv2.imshow('Original Image', image)
cv2.imshow('Gaussian Blur', gaussian_blur)
cv2.imshow('Median Filter', median_filter)
cv2.imshow('Sobel Combined', sobel_combined / 255)  # Normalize for display
cv2.imshow('Laplacian Filter', np.abs(laplacian_filter) / 255)  # Normalize
cv2.imshow('Unsharp Masking', unsharp_mask)
cv2.imshow('Box Filter', box_filter)

# Wait until a key is pressed and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
