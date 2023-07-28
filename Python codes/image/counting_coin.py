import cv2 as cv
import numpy
import imutils

img = cv.imread('coin.jpg', 0)
edges = cv.Canny(img, 50, 60)
hitung = cv.findContours(edges.copy(), cv.RETR_LIST , cv.CHAIN_APPROX_SIMPLE)
print('Jumlah koin {} dalam gambar' . format(len(hitung)))
cv.imshow('gambar', edges)
cv.waitKey(0)                                       