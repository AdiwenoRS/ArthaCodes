import cv2 as cv
import numpy as np
img = np.zeros((640, 480), np.uint8)
white = img + 255            

font = cv.FONT_HERSHEY_SCRIPT_COMPLEX

cv.putText(white, 'halo dunia', (230, 50), font, 1, (0,0,0), 2, cv.LINE_AA)
cv.imshow('canvas', white)
cv.waitKey(0)