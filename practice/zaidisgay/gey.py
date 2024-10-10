import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the image in grayscale
image_path = r"C:\Users\OSLAB\Downloads\011_png.rf.8ac312b4898f0106d10b76952a55d237.jpg"  # Replace with your image path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

cv2.imshow("img", image)

# Compute the histogram of the image
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

# # Plot the histogram
# plt.figure(figsize=(8,6))
# plt.plot(hist, color='black')
# plt.title('Grayscale Image Histogram')
# plt.xlabel('Pixel Intensity')
# plt.ylabel('Frequency')
# plt.grid(True)
# plt.show()


low_thresh, high_thresh = 50,200

def mapping(value, low_thresh, high_thresh):
    if value < low_thresh:
        return 255
    elif value < high_thresh:
        return 0
    return 255

vectorized_mapping = np.vectorize(mapping)
result_image = vectorized_mapping(image, low_thresh, high_thresh).astype(np.uint8)

cv2.imshow("new", result_image)

med_img = cv2.medianBlur(result_image, 3)
cv2.imshow("md", med_img)

dil_img = cv2.dilate(med_img, np.ones((3,3)), iterations=2)
cv2.imshow("dil", dil_img)

er_img = cv2.erode(dil_img, np.ones((3,3)), iterations=2)
cv2.imshow("erode", er_img)

blurred_image = cv2.GaussianBlur(med_img, (5, 5), 2)

cv2.imshow("blurred", blurred_image)
# blurred_image = med_img

# Use HoughCircles to detect craters (circular shapes)
circles = cv2.HoughCircles(blurred_image, cv2.HOUGH_GRADIENT, dp=1.2, minDist=30,
                           param1=100, param2=25, minRadius=10, maxRadius=100)

# Convert grayscale image to BGR for visualization
output_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

# If circles are detected, draw them
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        # Draw the outer circle
        cv2.circle(output_image, (x, y), r, (0, 255, 0), 4)
        # Draw the center of the circle
        cv2.circle(output_image, (x, y), 2, (0, 128, 255), 3)

# Show the result
plt.figure(figsize=(10,10))
plt.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
plt.axis('off')  # Hide axes for better visualization
plt.show()