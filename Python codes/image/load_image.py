import cv2 as cv

#processing

	#image1
img1 = cv.imread('spd.jpg', 1)
imgs1 = cv.resize(img1, (940,540))
cv.namedWindow('Foto normal dengan ukuran sesuai window', cv.WINDOW_NORMAL)
cv.imshow('Foto normal dengan ukuran sesuai window', imgs1)
	#image2
img2 = cv.imread('spd.jpg', cv.IMREAD_GRAYSCALE)
imgs2= cv.resize(img2, (940, 560))
cv.namedWindow('Foto dengan warna gray', cv.WINDOW_NORMAL)
cv.imshow('Foto dengan warna gray', imgs2)
	#image3
img3= cv.imread('spd.jpg', 1)
imgs3= cv.resize(img3, (940,540))
cv.imshow('Foto dengan ukuran konstan (940,540)', imgs3)

#image info
print('first tuple resolution:' ,img1.shape[0])
print('Resolution:', img1.shape)
print('Size in byte:', img1.size)

#wait key 
cv.waitKey(0)
