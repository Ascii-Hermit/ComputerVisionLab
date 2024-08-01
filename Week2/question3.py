# implement power law transform (gamma transform)

import cv2 as cv
import numpy as np

gamma = 2
scaling_constant = 1

img = cv.imread('images/cat.jpg', 0)

img_float = img.astype(np.float32) # optional for accuracy

#REMEMBER TO NORMALIZE THE IMG_FLOAT VALUES FROM 0-1
gamma_img = scaling_constant * np.power(img_float / 255.0, gamma)

# change the number and clip irrelevant values
gamma_img = np.clip(gamma_img * 255, 0, 255).astype(np.uint8)

cv.imshow('Normal', img)
cv.imshow('Gamma Transform', gamma_img)

cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite('images/gamma_transformed_cat.jpg', gamma_img)