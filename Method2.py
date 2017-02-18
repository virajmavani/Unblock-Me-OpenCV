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
  cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cap.destroyAllWindows()
