# apply thresholding

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('images/cat.jpg', 0)

# Histogram is optional to check the best value for the threshold

# hist = np.zeros(256)
# for pixel in image.flatten():
#     hist[pixel]+=1

# plt.plot(hist,color = "Blue")
# plt.show()

threshold = 150

thresh_img = np.zeros_like(image)

thresh_img[image>threshold] = 255

cv2.imshow("Original",image)
cv2.imshow("Binary",thresh_img)
cv2.imwrite('images/binary_thresh.jpg',thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows
