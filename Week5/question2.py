# Hough transform

import cv2
import numpy as np

image = cv2.imread('images/cat.jpg',0)

# The parameters are (src, low_threshold, high_threshold, kernel_size for sobel operator)
edges = cv2.Canny(image, 50, 150, apertureSize=3)

# parameters ( edge_image, distance_resolution, degree fro angular res, votes, less pixels than this will be rejected, max gap will be fillled)
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, minLineLength=100, maxLineGap=10)

if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2) 

cv2.imshow('Hough Lines', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('images/detected_lines.jpg', image) 