# importing the opencv library
import cv2 as cv

'''
The important functions are :- 

imread() helps us read an image
imshow() displays an image in a window
imwrite() writes an image into the file directory
waitKey() waits till a key is pressed
destroyAllWindows() closes all the creatded windows
'''

# The function cv2.imread() is used to read an image.
# use the folllowing guide to ensure the color setttings:
# cv2.IMREAD_UNCHANGED  or -1 this is the default
# cv2.IMREAD_GRAYSCALE  or 0
# cv2.IMREAD_COLOR  or 1

img = cv.imread('flower.png',0)

cv.imshow('image', img)

# waitKey() waits for a key press to close the window and 0 specifies indefinite loop
cv.waitKey(0)

# cv2.destroyAllWindows() simply destroys all the windows we created.
cv.destroyAllWindows()

# The function cv2.imwrite() is used to write an image.
cv.imwrite('grayscale_flower.jpg', img)
print(img.shape)
