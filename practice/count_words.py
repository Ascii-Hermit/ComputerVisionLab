# import cv2
# import numpy as np

# # Load the image
# image = cv2.imread('images/text.png')

# # Convert the image to grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Apply GaussianBlur to reduce noise
# blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# # Apply thresholding to get a binary image (background is white, text is black)
# _, thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow("Threshold",thresh)

# # Dilate the image to connect text regions
# kernel = np.ones((5, 5), np.uint8)  # Kernel size (5, 5) can be adjusted depending on text size
# dilated = cv2.dilate(thresh, kernel, iterations=1)
# cv2.imshow('Dilated Mask', dilated)

# # Find contours (blobs) in the dilated image
# contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Filter contours based on size (to remove noise and non-text blobs)
# word_contours = []
# for contour in contours:
#     area = cv2.contourArea(contour)
#     # Filter based on area (these values can be adjusted based on your image)
#     if 100 < area < 5000:
#         word_contours.append(contour)

# # Draw the filtered contours on the original image for visualization
# image = image.copy()
# cv2.drawContours(image, word_contours, -1, (255, 0, 0), 2)

# # Count the number of word blobs (contours)
# num_words = len(word_contours)
# print(f'Number of words detected: {num_words}')

# # Display the dilated mask and the image with detected words
# cv2.imshow('Detected Words', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2 as cv
import numpy as np

image = cv.imread("images/text.png", 0) # only works in grayscale
  
_, binary = cv.threshold(image, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("mask", binary)

kernel = np.ones((5,5))

dilated = cv.dilate(binary, kernel, iterations=1) # only works for white regions
cv.imshow("dilated", dilated)

contours, _  = cv.findContours(dilated, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
print(f"The number of strings are {len(contours)}")

cv.waitKey(0)
cv.destroyAllWindows()


