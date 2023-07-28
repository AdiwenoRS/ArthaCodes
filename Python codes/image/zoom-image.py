import cv2 as cv

img = cv.imread('spd.jpg', 1)
ukuranx, ukurany = img.shape[1]*2, img.shape[0]*2
imgr = cv.resize(img, (ukuranx, ukurany))
cv.imshow('lala', imgr)
cv.waitKey(0)