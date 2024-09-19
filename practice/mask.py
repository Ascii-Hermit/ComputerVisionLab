import cv2 as cv
import numpy as np

# Load the image
image = cv.imread("images/cat.jpg")

# Ensure the image was loaded
if image is None:
    print("Error: Image not found.")
    exit()

# Create a blank mask of the same size as the image, initialized to zero (black)
mask = np.zeros(image.shape[:2], dtype=np.uint8)

# Define the top-left and bottom-right corners of the rectangle
top_left = (50, 50)  # Example coordinates (x, y)
bottom_right = (250, 150)  # Example coordinates (x, y)

# Draw the rectangle on the mask (white rectangle)
cv.rectangle(mask, top_left, bottom_right, 255, -1)  # -1 fills the rectangle

# Apply the mask to the image using bitwise AND
masked_image = cv.bitwise_and(image, image, mask=mask)

# Display the results
cv.imshow("Original Image", image)
cv.imshow("Mask", mask)
cv.imshow("Masked Image", masked_image)

cv.waitKey(0)
cv.destroyAllWindows()
