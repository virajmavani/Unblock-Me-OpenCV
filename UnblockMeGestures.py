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
	
	cv2.rectangle(frame,(0,0),(105,80),(0,0,0))
	cv2.rectangle(frame,(106,0),(210,80),(0,0,0))
	cv2.rectangle(frame,(211,0),(315,80),(0,0,0))
	cv2.rectangle(frame,(316,0),(420,80),(0,0,0))
	cv2.rectangle(frame,(421,0),(525,80),(0,0,0))
	cv2.rectangle(frame,(526,0),(630,80),(0,0,0))
	cv2.rectangle(frame,(0,81),(105,160),(0,0,0))
	cv2.rectangle(frame,(106,81),(210,160),(0,0,0))
	cv2.rectangle(frame,(211,81),(315,160),(0,0,0))
	cv2.rectangle(frame,(316,81),(420,160),(0,0,0))
	cv2.rectangle(frame,(421,81),(525,160),(0,0,0))
	cv2.rectangle(frame,(526,81),(630,160),(0,0,0))
	cv2.rectangle(frame,(0,161),(105,240),(0,0,0))
	cv2.rectangle(frame,(106,161),(210,240),(0,0,0))
	cv2.rectangle(frame,(211,161),(315,240),(0,0,0))
	cv2.rectangle(frame,(316,161),(420,240),(0,0,0))
	cv2.rectangle(frame,(421,161),(525,240),(0,0,0))
	cv2.rectangle(frame,(526,161),(630,240),(0,0,0))
	cv2.rectangle(frame,(0,241),(105,320),(0,0,0))
	cv2.rectangle(frame,(106,241),(210,320),(0,0,0))
	cv2.rectangle(frame,(211,241),(315,320),(0,0,0))
	cv2.rectangle(frame,(316,241),(420,320),(0,0,0))
	cv2.rectangle(frame,(421,241),(525,320),(0,0,0))
	cv2.rectangle(frame,(526,241),(630,320),(0,0,0))
	cv2.rectangle(frame,(0,321),(105,400),(0,0,0))
	cv2.rectangle(frame,(106,321),(210,400),(0,0,0))
	cv2.rectangle(frame,(211,321),(315,400),(0,0,0))
	cv2.rectangle(frame,(316,321),(420,400),(0,0,0))
	cv2.rectangle(frame,(421,321),(525,400),(0,0,0))
	cv2.rectangle(frame,(526,321),(630,400),(0,0,0))
	cv2.rectangle(frame,(0,401),(105,480),(0,0,0))
	cv2.rectangle(frame,(106,401),(210,480),(0,0,0))
	cv2.rectangle(frame,(211,401),(315,480),(0,0,0))
	cv2.rectangle(frame,(316,401),(420,480),(0,0,0))
	cv2.rectangle(frame,(421,401),(525,480),(0,0,0))
	cv2.rectangle(frame,(526,401),(630,480),(0,0,0))
	
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cap.destroyAllWindows()
