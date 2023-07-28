import cv2 as cv
import numpy  as np
import imutils
import matplotlib.pyplot as plt

image = cv.imread('coin.jpg', 0)
imageBlur = cv.GaussianBlur(image, (5,5), 0)
imageRes, imageThresh = cv.threshold(imageBlur, 240, 255, cv.THRESH_BINARY_INV)
#black and white
kernel = np.ones((3,3), np.uint8)
opening = cv.morphologyEx(imageThresh, cv.MORPH_OPEN, kernel)


dist_transform = cv.distanceTransform(opening, cv.DIST_L2,5)
rest, last_image = cv.threshold(dist_transform, 0.3*dist_transform.max(),255,0)
last_image = np.uint8(last_image)


cnts = cv.findContours(last_image.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cv.imshow("hh", last_image)


cv.waitKey(0)