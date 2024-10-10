import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image_path = r"C:\Users\OSLAB\Downloads\014_png.rf.6b86c8afeb3ebca92872fd966d076adc.jpg"  # Replace with your image path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Step 1: Increase contrast using histogram equalization
equalized_image = cv2.equalizeHist(image)

# Step 2: Apply a Gaussian blur to reduce noise
blurred_image = cv2.GaussianBlur(equalized_image, (35, 35), 8)
cv2.imshow("t", blurred_image)

# Step 3: Use Canny edge detection to emphasize crater edges
edges = cv2.Canny(blurred_image, 50, 150)
cv2.imshow("c", edges)

# Step 4: Use HoughCircles to detect craters
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1.2, minDist=30,
                           param1=100, param2=30, minRadius=10, maxRadius=100)

# Convert the grayscale image to BGR for visualization
output_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

# Step 5: Draw the detected circles on the image
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        # Draw the outer circle
        cv2.circle(output_image, (x, y), r, (0, 255, 0), 3)
        # Draw the center of the circle
        cv2.circle(output_image, (x, y), 2, (0, 128, 255), 3)

# Show the result
plt.figure(figsize=(10,10))
plt.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
plt.axis('off')  # Hide axes for better visualization
plt.show()

cv2.destroyAllWindows()