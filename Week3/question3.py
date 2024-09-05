import cv2

def resize_image(image, new_size):
    # resizes the image
    return cv2.resize(image, new_size)

def crop_image(image, start_x, start_y, width, height):
    # crops the image 
    return image[start_y:start_y+height, start_x:start_x+width]

image_file = 'images\cat.jpg'  
image = cv2.imread(image_file)

new_size = (800, 600)  
resized_image = resize_image(image, new_size)

crop_x, crop_y, crop_width, crop_height = 100, 100, 400, 300  
cropped_image = crop_image(resized_image, crop_x, crop_y, crop_width, crop_height)

cv2.imwrite('images/resized_image.jpg', resized_image)
cv2.imwrite('images/cropped_image.jpg', cropped_image)

cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resized_image)
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
