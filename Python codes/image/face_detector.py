import cv2 as cv

wajah = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
mata = cv.CascadeClassifier('haarcascade_eye.xml')

img = cv.imread('face-eye.jpeg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny = cv.Canny(img_gray, 80, 90)
font = cv.FONT_HERSHEY_DUPLEX
jumlah = 0

deteksi_wajah = wajah.detectMultiScale(img, 1.3,5) 

for (x,y,w,h) in deteksi_wajah: 
	jumlah = jumlah + 1

	cv.putText(img, "Found!", (x,y-10), font, 0.8, (0, 0, 255),0, cv.LINE_AA)
	cv.rectangle(img,(x,y),(x+w,y+h),(255, 0, 0), 2)
	roi_gray = img_gray[y:y+h, x:x+w]
	roi_color = img[y:y+h, x:x+w]
	deteksi_mata= mata.detectMultiScale(roi_gray)
	
	for (ex, ey, ew, eh) in deteksi_mata:
		cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh), (0,255,0),2)

cv.putText(img, 'jumlah wajah ada '+ str(jumlah), (0,400),font,0.8,(0,100,255),2,cv.LINE_AA)
cv.imshow('img', img)
cv.waitKey(0)
