import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('images/cat.jpg', 0)

histogram = np.zeros(256)
for pixel in img.flatten():
    histogram[pixel] += 1

height, weight = img.shape

cdf = np.cumsum(histogram) # this is an array
cdf = cdf/cdf[-1] # normalise the array by dividing it by the last element

equalized_cdf = np.round(cdf * 255).astype(np.uint8) # make the array of proper size
equalized_img = equalized_cdf[img]  # each element is mapped to the equalised cdf

cv.imshow('Original Image', img)
cv.imshow('Equalized Image', equalized_img)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite('images/equalized_cat.jpg', equalized_img)
histogram2 = np.zeros(256)
for pixel in equalized_img.flatten():
    histogram2[pixel] += 1

plt.figure(figsize=(10, 6))
plt.plot(histogram, color='black')
plt.plot(histogram2, color='blue')
plt.xlim([0, 255])
plt.grid(True)
plt.show()
