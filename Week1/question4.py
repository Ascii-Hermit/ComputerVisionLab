import cv2 as cv

img = cv.imread('flower.png')

if img is None:
    print("Error")
else:
    start_point = (100, 100)  # top-left corner
    end_point = (200, 300)    # bottom-right corner
    color = (0, 255, 0)       # bgr format
    thickness = 2

    img_with_rectangle = cv.rectangle(img, start_point, end_point, color, thickness)

    cv.imshow('Image with Rectangle', img_with_rectangle)

    cv.waitKey(0)
    cv.destroyAllWindows()
