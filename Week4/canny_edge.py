import cv2
import numpy as np

def gaussian_blur(image, kernel_size, sigma):
    return cv2.GaussianBlur(image, kernel_size, sigma)

def sobel_edges(image):
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    angle = np.arctan2(sobel_y, sobel_x) * (180.0 / np.pi)  # this is in degrees
    angle[angle < 0] += 180  # Normalize angles to [0, 180)
    return magnitude, angle

def non_max_suppression(magnitude, angle):
    height, width = magnitude.shape
    suppressed = np.zeros_like(magnitude)
    
    angle = angle / 180.0 * np.pi  # Convert to radians

    for i in range(1, height-1):
        for j in range(1, width-1):
            try:
                q = 255
                r = 255

                # Angle 0 degrees
                if (0 <= angle[i, j] < np.pi/8) or (15 * np.pi/8 <= angle[i, j] <= 2 * np.pi):
                    q = magnitude[i, j + 1]
                    r = magnitude[i, j - 1]
                # Angle 45 degrees
                elif (np.pi/8 <= angle[i, j] < 3 * np.pi/8):
                    q = magnitude[i + 1, j + 1]
                    r = magnitude[i - 1, j - 1]
                # Angle 90 degrees
                elif (3 * np.pi/8 <= angle[i, j] < 5 * np.pi/8):
                    q = magnitude[i + 1, j]
                    r = magnitude[i - 1, j]
                # Angle 135 degrees
                elif (5 * np.pi/8 <= angle[i, j] < 7 * np.pi/8):
                    q = magnitude[i - 1, j + 1]
                    r = magnitude[i + 1, j - 1]

                if (magnitude[i, j] >= q) and (magnitude[i, j] >= r):
                    suppressed[i, j] = magnitude[i, j]
                else:
                    suppressed[i, j] = 0

            except IndexError as e:
                pass

    return suppressed

def thresholding(image, threshold):
    strong_edges = (image >= threshold)
    result = np.zeros_like(image, dtype=np.uint8)
    result[strong_edges] = 255

    return result

def canny_edge_detection(image, gaussian_kernel_size=(5, 5), sigma=1.0, threshold=150):
    blurred = gaussian_blur(image, gaussian_kernel_size, sigma)
    magnitude, angle = sobel_edges(blurred)
    suppressed = non_max_suppression(magnitude, angle)
    edges = thresholding(suppressed, threshold)
    return edges

image = cv2.imread('images/cat.jpg', 0)

edges = canny_edge_detection(image)

cv2.imshow('Original Image', image)
cv2.imshow('Canny Edges', edges)

cv2.imwrite('images/canny_edge.jpg', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
