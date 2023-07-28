import cv2 as cv

cap = cv.VideoCapture(0)

if not (cap.isOpened()):
	print('Couldn\'t open video device')

#set resolution
