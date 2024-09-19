import cv2
import numpy as np

# Load an image (replace 'image.jpg' with the path to your image)
image = cv2.imread('images/road.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray_image, 50, 150)

# Apply Hough Transform to detect lines
# cv2.HoughLines() detects lines using the standard Hough Transform
# cv2.HoughLinesP() detects lines using the probabilistic Hough Transform

# Standard Hough Transform
lines = cv2.HoughLines(edges, 1, np.pi / 180, 100)

# Probabilistic Hough Transform
# The last argument (e.g., 50) is the minimum number of intersections to detect a line
lines_p = cv2.HoughLinesP(edges, 100, np.pi / 180, 50, minLineLength=50, maxLineGap=10)

# Draw detected lines on the original image
if lines is not None:
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

if lines_p is not None:
    for line in lines_p:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Display the results
cv2.imshow('Original Image with Lines', image)
cv2.imshow('Edges', edges)

# Wait until a key is pressed and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
