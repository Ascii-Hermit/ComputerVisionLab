import cv2 as cv
'''
The following codes are the important codes for processing images in opencv

To read an image from the path, 
We use the following codes to read the image with the desired color setting
# cv2.IMREAD_UNCHANGED  or -1 this is the default
# cv2.IMREAD_GRAYSCALE  or 0
# cv2.IMREAD_COLOR  or 1

>>> imread('image_name', color_setting)
 
********************************************************
To display the read image, 
>>> imshow('window_name', read_image): 

We use two more functions while displaying
# waitKey() waits for a key press to close the window and 0 specifies indefinite loop
>>> cv.waitKey(0)
# cv2.destroyAllWindows() simply destroys all the windows we created.
>>> cv.destroyAllWindows()

*******************************************************
To write the image into a given path, (you can change the file type while renaming)
>>> imwrite('output_filename', read_image) 

*******************************************************
# It is possible to initialise an array of images and display them sequentially

>>> image_files = ['image1.jpg', 'image2.jpg', 'image3.jpg']

>>> for file in image_files:
>>>     img = cv.imread(file)
>>>     if img is None:
>>>         print(f'Error: {file} not found or unable to read')
>>>     else:
>>>         cv.imshow(file, img)
>>>         cv.waitKey(1000)  # Display each image for 1 second (1000 milliseconds)

******************************************************
To get the value of a singular pixel:
>>> # Define the coordinates of the pixel you want to extract (x, y)
>>> x = 100
>>> y = 150

>>> # Extract RGB values at the specified pixel
>>> # remember the syntax
>>> (b, g, r) = img[y, x]

******************************************************
To get the size of an image 
>>> image.shape

******************************************************
Inorder to resize an image: 
# Alters the size of the image

>>> new_width = 400
>>> new_height = 300

>>> resized_img = cv.resize(img, (new_width, new_height))

******************************************************
It rearranges the elements of the array to fit into a new shape,
which can be useful for preparing data for certain algorithms 
or frameworks that expect specific input shapes.

>>> height, width = img.shape

>>> # Reshape the image array to a new shape (e.g., flatten it)
>>> reshaped_img = img.reshape((height * width, some_variable))

******************************************************
To split an image into its RGB (Red, Green, Blue) channels 
using OpenCV in Python, you can use the cv.split() function. 

>>> b, g, r = cv.split(img) # keep this order in mind

>>> # Display each channel individually
>>> cv.imshow('Red Channel', r)
>>> cv.imshow('Green Channel', g)
>>> cv.imshow('Blue Channel', b)

*******************************************************
The are other color schemes also like HSV or Hue Saturation Value and Gray

>>> hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV) # from rgb to hsv
>>> gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # rgb to gray

*******************************************************
 Thresholding is a fundamental operation in image processing used 
 to create binary images from grayscale images based on pixel intensity values.

threshold_value = 127
max_value = 255
ret, thresh_img = cv.threshold(img, threshold_value, max_value, cv.THRESH_BINARY)

*******************************************************
Detecting edges in images using algorithms like Canny Edge Detection:

>>> edges = cv.Canny(img, threshold1, threshold2)

*******************************************************
To rotate a picture:  
>>> M = cv.getRotationMatrix2D(center, angle, scale)
>>> rotated_img = cv.warpAffine(img, M, (width, height))

*******************************************************
When you resize an image to make it larger or smaller, new pixel values need to be calculated for the resulting image.
Interpolation methods help in this calculation by estimating pixel values based on the surrounding pixels in the original image.

Extrapolation involves estimating values outside the range of known data points, which isn't directly provided by OpenCV 
for images but can be inferred in certain transformations and operation



'''