import cv2 as cv 

img = cv.imread('spd.jpg', 1)
cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image',img)
cv.waitKey()
