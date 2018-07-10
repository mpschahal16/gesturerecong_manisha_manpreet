import cv2
import numpy as np


cap= cv2.VideoCapture(0)
labels = list()
example_contour = list()
images= list()
imname=  0
while (cap.isOpened()):
	ret, img= cap.read()
	img= cv2.flip(img, 1)
	cv2.rectangle(img,(150,50),(450,350),(0,255,0),0)




	roi= img[50:349, 150:449]
	gray= cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (41,41), 1)
	#blurred=gray
	cv2.imshow('Blurred ', blurred)

	_, edges= cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	_, contours, hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	y=len(contours)
	area= np.zeros(y)
	for i in range(0, y):
		area[i] = cv2.contourArea(contours[i])


	index= area.argmax()
	hand = contours[index]
	x,y,w,h = cv2.boundingRect(hand)
	cv2.rectangle(roi,(x,y),(x+w,y+h),(0,0,255),0)
	temp = np.zeros(roi.shape, np.uint8)
	

	#M = cv2.moments(hand)

	#cv2.drawContours(img, [hand], -1, (0, 255,0), -1)
	cv2.drawContours(temp, [hand], -1, (0, 255,0), -1)

	key = cv2.waitKey(1)


	

	if key & 0xFF== 27:
		c = np.asarray(example_contour)
		np.save('gestures/composite_list.npy', c)
		np.save('gestures/composite_list_labels.npy', labels)
		for img in images:
			i = str(imname)
			cv2.imwrite('gestures/'+i.zfill(6)+'.jpg', img)
			imname+=1
		break	 
	elif key & 0xFF == ord('0'):
		example_contour.append(hand)
		images.append(temp)
		labels.append(0)
		print(len(example_contour))
	elif key & 0xFF == ord('1'):
		example_contour.append(hand)
		images.append(temp)
		labels.append(1)
		print(len(example_contour))
	elif key & 0xFF == ord('2'):
		example_contour.append(hand)
		images.append(temp)
		labels.append(2)
		print(len(example_contour))
	elif key & 0xFF == ord('3'):
		example_contour.append(hand)
		images.append(temp)
		labels.append(3)
		print(len(example_contour))
	elif key & 0xFF == ord('4'):
		example_contour.append(hand)
		images.append(temp)
		labels.append(4)
		print(len(example_contour))
	elif key & 0xFF == ord('5'):
		example_contour.append(hand)
		images.append(temp)
		labels.append(5)
		print(len(example_contour))
	elif key & 0xFF == ord('6'):
		example_contour.append(hand)
		images.append(temp)
		labels.append(6)
		print(len(example_contour))
	elif key & 0xFF == ord('7'):
		example_contour.append(hand)
		images.append(temp)
		labels.append(7)
		print(len(example_contour))
	elif key & 0xFF == ord('8'):
		example_contour.append(hand)
		images.append(temp)
		labels.append(8)
		print(len(example_contour))
	elif key & 0xFF == ord('9'):
		example_contour.append(hand)
		images.append(temp)
		labels.append(9)
		print(len(example_contour))
	elif key & 0xFF == ord('a'):
		example_contour.append(hand)
		images.append(temp)
		labels.append('a')
		print(len(example_contour))
	elif key & 0xFF == ord('b'):
		example_contour.append(hand)
		images.append(temp)
		labels.append('b')
		print(len(example_contour))
	elif key & 0xFF == ord('c'):
		example_contour.append(hand)
		images.append(temp)
		labels.append('c')
		print(len(example_contour))
	elif key & 0xFF == ord('d'):
		example_contour.append(hand)
		images.append(temp)
		labels.append('d')
		print(len(example_contour))
	elif key & 0xFF == ord('e'):
		example_contour.append(hand)
		images.append(temp)
		labels.append('e')
		print(len(example_contour))
	elif key & 0xFF == ord('f'):
		example_contour.append(hand)
		images.append(temp)
		labels.append('f')
		print(len(example_contour))
	elif key & 0xFF == ord('g'):
		example_contour.append(hand)
		images.append(temp)
		labels.append('g')
		print(len(example_contour))
	elif key & 0xFF == ord('h'):
		example_contour.append(hand)
		images.append(temp)
		labels.append('h')
		print(len(example_contour))
	elif key & 0xFF == ord('i'):
		example_contour.append(hand)
		images.append(temp)
		labels.append('i')
		print(len(example_contour))
	elif key & 0xFF == ord('j'):
		example_contour.append(hand)
		images.append(temp)
		labels.append('j')
		print(len(example_contour))
	elif key & 0xFF == ord('k'):
		example_contour.append(hand)
		images.append(temp)
		labels.append('k')
		print(len(example_contour))
	elif key & 0xFF == ord('l'):
		example_contour.append(hand)
		images.append(temp)
		labels.append('l')
		print(len(example_contour))
	elif key & 0xFF == ord('m'):
		example_contour.append(hand)
		images.append(temp)
		labels.append('m')
		print(len(example_contour))
	elif key & 0xFF == ord('n'):
		example_contour.append(hand)
		images.append(temp)
		labels.append('n')
		print(len(example_contour))
	elif key & 0xFF == ord('o'):
		example_contour.append(hand)
		images.append(temp)
		labels.append('o')
		print(len(example_contour))
	elif key & 0xFF == ord('p'):
		example_contour.append(hand)
		images.append(temp)
		labels.append('p')
		print(len(example_contour))
	elif key & 0xFF == ord('q'):
		example_contour.append(hand)
		images.append(temp)
		labels.append('q')
		print(len(example_contour))
	elif key & 0xFF == ord('r'):
		example_contour.append(hand)
		images.append(temp)
		labels.append('r')
		print(len(example_contour))
	elif key & 0xFF == ord('s'):
		example_contour.append(hand)
		images.append(temp)
		labels.append('s')
		print(len(example_contour))
	elif key & 0xFF == ord('t'):
		example_contour.append(hand)
		images.append(temp)
		labels.append('t')
		print(len(example_contour))
	elif key & 0xFF == ord('u'):
		example_contour.append(hand)
		images.append(temp)
		labels.append('u')
		print(len(example_contour))
	elif key & 0xFF == ord('v'):
		example_contour.append(hand)
		images.append(temp)
		labels.append('v')
		print(len(example_contour))
	elif key & 0xFF == ord('w'):
		example_contour.append(hand)
		images.append(temp)
		labels.append('w')
		print(len(example_contour))
	elif key & 0xFF == ord('x'):
		example_contour.append(hand)
		images.append(temp)
		labels.append('x')
		print(len(example_contour))
	elif key & 0xFF == ord('y'):
		example_contour.append(hand)
		images.append(temp)
		labels.append('y')
		print(len(example_contour))
	elif key & 0xFF == ord('z'):
		example_contour.append(hand)
		images.append(temp)
		labels.append('z')
		print(len(example_contour))
			
	cv2.imshow('Place your hand in the rectangle', img)
	cv2.imshow('Contour', temp)


