import numpy as np
import cv2
import pyautogui as mouse

centroid_x = 0
centroid_y = 0
move=0
cap = cv2.VideoCapture(0)

while(True):
	ret, frame = cap.read()
	frame = cv2.flip(frame,1)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	# cv2.imshow('hsv1',hsv)
	lower_red = np.array([120,100,100])
	upper_red = np.array([130,255,255])
	mask = cv2.inRange(hsv, lower_red, upper_red)
	
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cap.destroyAllWindows()
