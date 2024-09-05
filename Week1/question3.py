# import cv2 as cv
# import numpy as np
#
# img = cv.imread('flower.png', cv.IMREAD_COLOR)
#
# if img is None:
#     print("Error")
# else:
#     # Splitting the image into its RGB components
#     b, g, r = cv.split(img)
#
#     # Create an empty image of the same size as the original image
#     zeros = np.zeros_like(b)
#
#     # Merge each channel into a separate image
#     blue_img = cv.merge((b, zeros, zeros))
#     green_img = cv.merge((zeros, g, zeros))
#     red_img = cv.merge((zeros, zeros, r))
#
#     # Display each channel as separate images
#     cv.imshow('Blue Channel', blue_img)
#     cv.imshow('Green Channel', green_img)
#     cv.imshow('Red Channel', red_img)
#
#     # Wait for a key press and close all windows
#     cv.waitKey(0)
#     cv.destroyAllWindows()

import cv2 as cv

img = cv.imread('flower.png')

# Define the coordinates of the pixel you want to extract (x, y)
x = 100
y = 150

# Extract RGB values at the specified pixel
# remember the syntax
(b, g, r) = img[y, x]

# Print RGB values
print(f"RGB values at pixel ({x}, {y}):")
print(f"Red: {r}")
print(f"Green: {g}")
print(f"Blue: {b}")

