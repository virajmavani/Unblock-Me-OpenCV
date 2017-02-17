import numpy as np
import cv2

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
	
	if w*h>=19600:
		if centroid_x<=210 and centroid_y<=160:
			if centroid_x<=105 and centroid_y<=80:
				move = 1
			elif centroid_x>105 and centroid_y<=80:
				move = 2
			elif centroid_x<=105 and centroid_y>80:
				move = 7
			else:
				move = 8
		elif centroid_x<=420 and centroid_y<=160:
			if centroid_x<=315 and centroid_y<=80:
				move = 3
			elif centroid_x>315 and centroid_y<=80:
				move = 4
			elif centroid_x<=315 and centroid_y>80:
				move = 9
			else:
				move = 10
		elif centroid_x<=630 and centroid_y<=160:
			if centroid_x<=525 and centroid_y<=80:
				move = 5
			elif centroid_x>525 and centroid_y<=80:
				move = 6
			elif centroid_x<=525 and centroid_y>80:
				move = 11
			else:
				move = 12
		elif centroid_x<=210 and centroid_y<=320:
			if centroid_x<=105 and centroid_y<=240:
				move = 13
			elif centroid_x>105 and centroid_y<=240:
				move = 14
			elif centroid_x<=105 and centroid_y>240:
				move = 19
			else:
				move = 20
		elif centroid_x<=420 and centroid_y<=320:
			if centroid_x<=315 and centroid_y<=240:
				move = 15
			elif centroid_x>315 and centroid_y<=240:
				move = 16
			elif centroid_x<=315 and centroid_y>240:
				move = 21
			else:
				move = 22
		elif centroid_x<=630 and centroid_y<=320:
			if centroid_x<=525 and centroid_y<=240:
				move = 17
			elif centroid_x>525 and centroid_y<=240:
				move = 18
			elif centroid_x<=525 and centroid_y>240:
				move = 23
			else:
				move = 24
		elif centroid_x<=210 and centroid_y<=480:
			if centroid_x<=105 and centroid_y<=400:
				move = 25
			elif centroid_x>105 and centroid_y<=400:
				move = 26
			elif centroid_x<=105 and centroid_y>400:
				move = 31
			else:
				move = 32
		elif centroid_x<=420 and centroid_y<=480:
			if centroid_x<=315 and centroid_y<=400:
				move = 27
			elif centroid_x>315 and centroid_y<=400:
				move = 28
			elif centroid_x<=315 and centroid_y>400:
				move = 33
			else:
				move = 34
		elif centroid_x<=630 and centroid_y<=480:
			if centroid_x<=525 and centroid_y<=400:
				move = 29
			elif centroid_x>525 and centroid_y<=400:
				move = 30
			elif centroid_x<=525 and centroid_y>400:
				move = 35
			else:
				move = 36
	
	print "Move:", move
	
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
