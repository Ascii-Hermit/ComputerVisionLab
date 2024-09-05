import cv2 as cv

img = cv.imread('flower.png')

if img is None:
    print("Error: Could not open or find the image.")
else:
    angle = 45

    # get first 2 elements
    height, width = img.shape[:2]

    #standard functions for rotating
    rotation_matrix = cv.getRotationMatrix2D((width/2, height/2), angle, 1) # center, angle, scaling
    rotated_img = cv.warpAffine(img, rotation_matrix, (width, height))

    cv.imshow('Original Image', img)
    cv.imshow('Rotated Image', rotated_img)

    cv.waitKey(0)
    cv.destroyAllWindows()
