import cv2 as cv
import numpy as np

img_path = 'images/cat.jpg'
img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)

threshold_value = 200

_, binary_mask = cv.threshold(img, threshold_value, 255, cv.THRESH_BINARY)

# cv.findContours() function, first one is source image,
# second is contour retrieval mode, third is contour approximation method

# The cv.RETR_EXTERNAL mode retrieves only the external contours.
# The cv.CHAIN_APPROX_SIMPLE method removes all redundant points
# and compresses the contour, saving only the end points of each segment.

# list of contours found in the image. Each contour is represented as a list of points
# (usually a NumPy array) that form the boundary of the detected object.

# heirarchial It provides details about the relationship between contours, such as
# which contours are nested within others.

contours, _ = cv.findContours(binary_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

circle_color = (0, 255, 0)
circle_thickness = 2

for contour in contours:
    # The input array, which can be a binary image or a contour. If it's a binary image, it should be
    # in grayscale with object pixels typically set to 255 (or 1).
    # binaryImage: A boolean flag indicating whether the input is a binary image. If True, the moments
    # are calculated as if the image is binary; otherwise, the function will treat it as a grayscale image.

    M = cv.moments(contour, binaryImage= True)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        radius = int(np.sqrt(cv.contourArea(contour) / np.pi))  # Approximate radius

        cv.circle(img, (cX, cY), radius, circle_color, circle_thickness)


cv.imshow('Image with Bright Spots Marked', img)

cv.waitKey(0)
cv.destroyAllWindows()

output_path = 'images/bright_spots_marked.jpg'
cv.imwrite(output_path, img)
