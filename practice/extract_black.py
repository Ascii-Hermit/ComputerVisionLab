import cv2 as cv
import numpy as np

# extract black parts
image = cv.imread("images/color.jpg")
h,w,c = image.shape
print(image.shape)

for y in range(h) :
    for x in range(w):
        if np.all(image[y, x] < (100,100,100)):
            image[y, x] = (0,0,0)
        else:
            image[y, x] = (255,255,255)

cv.imshow("mask",image)
cv.waitKey(0)
cv.destroyAllWindows()

