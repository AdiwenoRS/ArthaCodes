import cv2 as cv

img = cv.imread('coin.jpg', 1)
font = cv.FONT_HERSHEY_SIMPLEX 
cv.putText(img, 'There is 8 coins', (150, 270), font, 1 , (0,0,0), 2, cv.LINE_AA)
cv.imshow('gambar', img)
cv.waitKey(0)