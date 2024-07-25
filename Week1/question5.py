import cv2 as cv

img = cv.imread('flower.png')

if img is None:
    print("Error: Could not open or find the image.")
else:
    new_width = 800
    new_height = 600

    # Resize the image using INTER_LINEAR interpolation
    resized_img = cv.resize(img, (new_width, new_height), interpolation=cv.INTER_LINEAR)

    cv.imshow('Original Image', img)
    cv.imshow('Resized Image', resized_img)

    cv.waitKey(0)
    cv.destroyAllWindows()
