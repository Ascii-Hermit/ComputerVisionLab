import cv2 as cv
import numpy as np

image = cv.imread("images/rot_text.jpg", 0)

image = cv.resize(image, (600,300))

image = image[:,0:300]


_, thresh = cv.threshold(image, 150, 255, cv.THRESH_BINARY)
cv.imshow("image", thresh)

edges = cv.Canny(thresh, 50, 150)

lines = cv.HoughLinesP(edges, 10, np.pi / 180, 50, minLineLength=100, maxLineGap=10)

sum = 0
count=0
line_image = image.copy()
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        sum += np.degrees(np.arctan((y2-y1)/(x2-x1)))
        count+=1
print(sum/count)

cv.imshow("lines", line_image)

cv.waitKey(0)
cv.destroyAllWindows()



# import cv2 as cv
# import numpy as np

# # Load the image
# image = cv.imread("images/rot_text.jpg")

# # Resize the image
# image = cv.resize(image, (600, 300))

# # Convert the image to grayscale
# gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# # Apply binary thresholding to the grayscale image
# _, thresh = cv.threshold(gray_image, 200, 255, cv.THRESH_BINARY)
# cv.imshow("Thresholded Image", thresh)

# # Apply Canny edge detection
# edges = cv.Canny(thresh, 50, 150)

# # Apply Hough Line Transform to detect lines
# lines = cv.HoughLinesP(edges, 1, np.pi / 180, 50, minLineLength=50, maxLineGap=10)

# # Create a copy of the original image to draw lines on
# line_image = image.copy()

# # Draw the detected lines on the image
# if lines is not None:
#     for line in lines:
#         x1, y1, x2, y2 = line[0]
#         cv.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Draw lines in green

# # Display the results
# cv.imshow("Detected Lines", line_image)

# # Wait until a key is pressed and close all windows
# cv.waitKey(0)
# cv.destroyAllWindows()
