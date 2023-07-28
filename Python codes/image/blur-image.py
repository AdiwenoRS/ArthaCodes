from ast import While
import cv2 as cv
img = cv.imread('spd.jpg', 1)

blur = cv.blur(img,(10,10))
cv.namedWindow('blur', cv.WINDOW_NORMAL)
cv.imshow('blur', blur)
cv.waitKey(0)

