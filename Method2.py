import cv2
import numpy as np
import pyautogui as mouse
import math

cap = cv2.VideoCapture(0)

while(True):
	ret, frame = cap.read()
	frame = cv2.flip(frame,1)
	value = (35, 35)
	blurred = cv2.GaussianBlur(frame, value, 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
	# imgray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	# print 'hsv:',hsv
	# cv2.imshow('hsv1',hsv)
	lower_skin = np.array([120,50,50])
	upper_skin = np.array([180,180,200])
	mask = cv2.inRange(hsv, lower_skin, upper_skin)
	# ret,mask = cv2.threshold(imgray,70,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	cv2.imshow('mask',mask)
	# grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# value = (70, 255)
	# blurred = cv2.GaussianBlur(grey, value, 0)
	# _, thresh1 = cv2.threshold(grey, 70, 255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	# cv2.imshow('Thresholded', thresh1)
  	
	image, contours, hierarchy = cv2.findContours(mask.copy(),cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	if contours == []:
		continue
	cnt = max(contours, key = lambda x: cv2.contourArea(x))
	
	x,y,w,h = cv2.boundingRect(cnt)
	cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
	centroid_x = (x + x+w)/2
	centroid_y = (y + y+h)/2
	cv2.circle(frame, (centroid_x, centroid_y), 2, (0,0,255), 2)
	hull = cv2.convexHull(cnt)
	# drawing = np.zeros(frame.shape,np.uint8)
	# cv2.drawContours(drawing,[cnt],0,(0,255,0),0)
	# cv2.drawContours(drawing,[hull],0,(0,0,255),0)
	# hull = cv2.convexHull(cnt,returnPoints = False)
	final_d = 480
	j=0
	d=hull.shape[0]		
	for i in range(0,d):
		v = hull[i][0][1]
		# dist = np.sqrt(np.power(hull[i][0][0]-centroid_x,2)+np.power(hull[i][0][1]-centroid_y,2))
		if v < final_d:
			final_d = v
			j=i
	
	cv2.circle(frame, (hull[j][0][0], hull[j][0][1]), 2, (0,0,255), 2)
	
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cap.destroyAllWindows()
