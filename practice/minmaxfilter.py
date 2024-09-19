import cv2 as cv
import numpy as np

# Read the image
image = cv.imread("images/cat.jpg", cv.IMREAD_GRAYSCALE)

# Define a kernel size (the size of the neighborhood)
kernel_size = (5, 5)

# Apply the Min filter (erode)
min_filter = cv.erode(image, np.ones(kernel_size))

# Apply the Max filter (dilate)
max_filter = cv.dilate(image, np.ones(kernel_size))

# Display the results
cv.imshow("Original Image", image)
cv.imshow("Min Filter (Erosion)", min_filter)
cv.imshow("Max Filter (Dilation)", max_filter)

cv.waitKey(0)
cv.destroyAllWindows()
