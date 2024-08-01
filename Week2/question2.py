import cv2 as cv
import numpy as np

img = cv.imread('images/cat.jpg', 0)

img_float = img.astype(np.float32) # optional for accuracy


## THE FORMULA FOR LOG IS __output pixel__ = c * log(1+__input pixel__)
## c = __grayscale max__/ log(1+__grayscale max__)

c = 255 / np.log(1 + 255)

log_img = c * np.log(1 + img_float)

# clipping the values out of range
# converting back to int
log_img = np.clip(log_img, 0, 255).astype(np.uint8)

cv.imshow('Normal', img)
cv.imshow('Log Transform', log_img)

cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite('images/log_transformed_cat.jpg', log_img)
