import cv2 as cv

img = cv.imread('yosabi.png', 1)
edges = cv.Canny(img, 80, 90)
cv.namedWindow('edges', cv.WINDOW_NORMAL)
cv.imshow('edges', edges)

cv.namedWindow('foto', cv.WINDOW_NORMAL)
cv.imshow('foto', img)
cv.waitKey(0)