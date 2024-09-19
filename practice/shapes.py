import cv2
import numpy as np

# blank image
image = np.zeros((500, 500), dtype="uint8")

# -1 will fill the shape
# Draw a line (start_point, end_point, color, thickness)
cv2.line(image, (50, 50), (450, 50), (255, 0, 0), 5)

# Draw a rectangle (top-left corner, bottom-right corner, color, thickness)
cv2.rectangle(image, (100, 100), (400, 300), (255, 0, 0), 50)

# Draw a circle (center, radius, color, thickness)
cv2.circle(image, (250, 400), 50, (255, 0, 255), -1)  # -1 thickness fills the shape

# Draw an ellipse (center, axes, angle, startAngle, endAngle, color, thickness)
cv2.ellipse(image, (250, 250), (150, 75), 30, 0, 360, (255, 0, 0), 4)

# Display the image with shapes
cv2.imshow('Shapes', image)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
