# implementing negative transform

import cv2 as cv

img = cv.imread('images/cat.jpg', 0)
negative_img = abs(255 - img) # subtracts from the whole matrix

cv.imshow('Normal', img)
cv.imshow('Negative', negative_img)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite('images/negative_cat.jpg', img)


