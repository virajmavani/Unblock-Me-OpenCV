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
	lower_red = np.array([160,100,100])
	upper_red = np.array([179,255,255])
	mask = cv2.inRange(hsv, lower_red, upper_red)
	
	im2, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	max_area = 0
	last_x = centroid_x
	last_y = centroid_y
	if contours == []:
		continue
	cnt = max(contours, key = lambda x: cv2.contourArea(x))
	
	x,y,w,h = cv2.boundingRect(cnt)
	cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
	centroid_x = (x + x+w)/2
	centroid_y = (y + y+h)/2
	cv2.circle(frame, (centroid_x, centroid_y), 2, (0,0,255), 2)
	
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cap.destroyAllWindows()
