import cv2 as cv


img = cv.imread('spd.jpg', 1)

#rotate
lebar, tinggi = img.shape[1], img.shape[0]
imgr = cv.getRotationMatrix2D((lebar/2, tinggi/2),90,1)
imgrotate = cv.warpAffine(img, imgr,(lebar,tinggi))
cv.namedWindow('foto', cv.WINDOW_NORMAL)
cv.imshow('foto', imgrotate)

#flip
flip = cv.flip(img,-1)
cv.namedWindow('flip', cv.WINDOW_NORMAL)
cv.imshow('flip', flip)


cv.waitKey(0)
cv.destroyAllWindows()