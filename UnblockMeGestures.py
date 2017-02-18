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
	fist_cascade = cv2.CascadeClassifier('aGest.xml')
	mask = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	fists = fist_cascade.detectMultiScale(mask, 1.3, 5)
	for (x,y,w,h) in fists:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
		centroid_x = (x + x+w)/2
		centroid_y = (y + y+h)/2
		cv2.circle(frame, (centroid_x, centroid_y), 2, (0,0,255), 2)
		
	if centroid_x<=160 and centroid_y<=160:
		if centroid_x<=80 and centroid_y<=80:
			if move == 2:
				mouse.moveTo(360,190)
				# mouse.mouseDown()
				mouse.dragTo(320,190,button="left")
				# mouse.mouseUp()
			if move == 7:
				mouse.moveTo(320,230)
				mouse.dragTo(320,190,button="left")
			move = 1
		elif centroid_x>80 and centroid_y<=80:
			if move == 1:
				mouse.moveTo(320,190)
				mouse.dragTo(360,190,button="left")
			if move == 8:
				mouse.moveTo(360,230)
				mouse.dragTo(360,190,button="left")
			if move == 3:
				mouse.moveTo(400,190)
				mouse.dragTo(360,190,button="left")
			move = 2
		elif centroid_x<=80 and centroid_y>80:
			if move == 1:
				mouse.moveTo(320,190)
				mouse.dragTo(320,230,button="left")
			if move == 8:
				mouse.moveTo(360,230)
				mouse.dragTo(320,230,button="left")
			if move == 13:
				mouse.moveTo(320,275)
				mouse.dragTo(320,230,button="left")
			move = 7
		else:
			if move == 2:
				mouse.moveTo(360,190)
				mouse.dragTo(360,230,button="left")
			if move == 7:
				mouse.moveTo(320,230)
				mouse.dragTo(360,230,button="left")
			if move == 9:
				mouse.moveTo(400,230)
				mouse.dragTo(360,230,button="left")
			if move == 14:
				mouse.moveTo(360,275)
				mouse.dragTo(360,230,button="left")
			move = 8
	elif centroid_x<=320 and centroid_y<=160:
		if centroid_x<=240 and centroid_y<=80:
			if move == 2:
				mouse.moveTo(360,190)
				mouse.dragTo(400,190,button="left")
			if move == 4:
				mouse.moveTo(445,190)
				mouse.dragTo(400,190,button="left")
			if move == 9:
				mouse.moveTo(400,230)
				mouse.dragTo(400,190,button="left")
			move = 3
		elif centroid_x>240 and centroid_y<=80:
			if move == 3:
				mouse.moveTo(400,190)
				mouse.dragTo(445,190,button="left")
			if move == 5:
				mouse.moveTo(490,190)
				mouse.dragTo(445,190,button="left")
			if move == 10:
				mouse.moveTo(445,230)
				mouse.dragTo(445,190,button="left")
			move = 4
		elif centroid_x<=240 and centroid_y>80:
			if move == 3:
				mouse.moveTo(400,190)
				mouse.dragTo(400,230,button="left")
			if move == 8:
				mouse.moveTo(360,230)
				mouse.dragTo(400,230,button="left")
			if move == 10:
				mouse.moveTo(445,230)
				mouse.dragTo(400,230,button="left")
			if move == 15:
				mouse.moveTo(400,275)
				mouse.dragTo(400,230,button="left")
			move = 9
		else:
			if move == 4:
				mouse.moveTo(445,190)
				mouse.dragTo(445,230,button="left")
			if move == 9:
				mouse.moveTo(400,230)
				mouse.dragTo(445,230,button="left")
			if move == 11:
				mouse.moveTo(490,230)
				mouse.dragTo(445,230,button="left")
			if move == 16:
				mouse.moveTo(445,275)
				mouse.dragTo(445,230,button="left")
			move = 10
	elif centroid_x<=480 and centroid_y<=160:
		if centroid_x<=400 and centroid_y<=80:
			if move == 4:
				mouse.moveTo(445,190)
				mouse.dragTo(490,190,button="left")
			if move == 6:
				mouse.moveTo(530,190)
				mouse.dragTo(490,190,button="left")
			if move == 11:
				mouse.moveTo(490,230)
				mouse.dragTo(490,190,button="left")
			move = 5
		elif centroid_x>400 and centroid_y<=80:
			if move == 5:
				mouse.moveTo(490,190)
				mouse.dragTo(530,190,button="left")
			if move == 12:
				mouse.moveTo(530,230)
				mouse.dragTo(530,190,button="left")
			move = 6
		elif centroid_x<=400 and centroid_y>80:
			if move == 5:
				mouse.moveTo(490,190)
				mouse.dragTo(490,230,button="left")
			if move == 10:
				mouse.moveTo(445,230)
				mouse.dragTo(490,230,button="left")
			if move == 12:
				mouse.moveTo(530,230)
				mouse.dragTo(490,230,button="left")
			if move == 17:
				mouse.moveTo(490,275)
				mouse.dragTo(490,230,button="left")
			move = 11
		else:
			if move == 6:
				mouse.moveTo(530,190)
				mouse.dragTo(530,230,button="left")
			if move == 11:
				mouse.moveTo(490,230)
				mouse.dragTo(530,230,button="left")
			if move == 18:
				mouse.moveTo(530,275)
				mouse.dragTo(530,230,button="left")
			move = 12
	elif centroid_x<=160 and centroid_y<=320:
		if centroid_x<=80 and centroid_y<=240:
			if move == 7:
				mouse.moveTo(320,230)
				mouse.dragTo(320,275,button="left")
			if move == 14:
				mouse.moveTo(360,275)
				mouse.dragTo(320,275,button="left")
			if move == 19:
				mouse.moveTo(320,320)
				mouse.dragTo(320,275,button="left")
			move = 13
		elif centroid_x>80 and centroid_y<=240:
			if move == 8:
				mouse.moveTo(360,230)
				mouse.dragTo(360,275,button="left")
			if move == 13:
				mouse.moveTo(320,275)
				mouse.dragTo(360,275,button="left")
			if move == 15:
				mouse.moveTo(400,275)
				mouse.dragTo(360,275,button="left")
			if move == 20:
				mouse.moveTo(360,320)
				mouse.dragTo(360,275,button="left")
			move = 14
		elif centroid_x<=80 and centroid_y>240:
			if move == 13:
				mouse.moveTo(320,275)
				mouse.dragTo(320,320,button="left")
			if move == 20:
				mouse.moveTo(360,320)
				mouse.dragTo(320,320,button="left")
			if move == 25:
				mouse.moveTo(320,360)
				mouse.dragTo(320,320,button="left")
			move = 19
		else:
			if move == 14:
				mouse.moveTo(360,275)
				mouse.dragTo(360,320,button="left")
			if move == 19:
				mouse.moveTo(320,320)
				mouse.dragTo(360,320,button="left")
			if move == 21:
				mouse.moveTo(400,320)
				mouse.dragTo(360,320,button="left")
			if move == 26:
				mouse.moveTo(360,360)
				mouse.dragTo(360,320,button="left")
			move = 20
	elif centroid_x<=320 and centroid_y<=320:
		if centroid_x<=240 and centroid_y<=240:
			if move == 9:
				mouse.moveTo(400,230)
				mouse.dragTo(400,275,button="left")
			if move == 14:
				mouse.moveTo(360,275)
				mouse.dragTo(400,275,button="left")
			if move == 16:
				mouse.moveTo(445,275)
				mouse.dragTo(400,275,button="left")
			if move == 21:
				mouse.moveTo(400,320)
				mouse.dragTo(400,275,button="left")
			move = 15
		elif centroid_x>240 and centroid_y<=240:
			if move == 10:
				mouse.moveTo(445,230)
				mouse.dragTo(445,275,button="left")
			if move == 15:
				mouse.moveTo(400,275)
				mouse.dragTo(445,275,button="left")
			if move == 17:
				mouse.moveTo(490,275)
				mouse.dragTo(445,275,button="left")
			if move == 22:
				mouse.moveTo(445,320)
				mouse.dragTo(445,275,button="left")
			move = 16
		elif centroid_x<=240 and centroid_y>240:
			if move == 15:
				mouse.moveTo(400,275)
				mouse.dragTo(400,320,button="left")
			if move == 20:
				mouse.moveTo(360,320)
				mouse.dragTo(400,320,button="left")
			if move == 22:
				mouse.moveTo(445,320)
				mouse.dragTo(400,320,button="left")
			if move == 27:
				mouse.moveTo(400,360)
				mouse.dragTo(400,320,button="left")
			move = 21
		else:
			if move == 16:
				mouse.moveTo(445,275)
				mouse.dragTo(445,320,button="left")
			if move == 21:
				mouse.moveTo(400,320)
				mouse.dragTo(445,320,button="left")
			if move == 23:
				mouse.moveTo(490,320)
				mouse.dragTo(445,320,button="left")
			if move == 28:
				mouse.moveTo(445,360)
				mouse.dragTo(445,320,button="left")
			move = 22
	elif centroid_x<=480 and centroid_y<=320:
		if centroid_x<=400 and centroid_y<=240:
			if move == 11:
				mouse.moveTo(490,230)
				mouse.dragTo(490,275,button="left")
			if move == 16:
				mouse.moveTo(445,275)
				mouse.dragTo(490,275,button="left")
			if move == 18:
				mouse.moveTo(530,275)
				mouse.dragTo(490,275,button="left")
			if move == 23:
				mouse.moveTo(490,320)
				mouse.dragTo(490,275,button="left")
			move = 17
		elif centroid_x>400 and centroid_y<=240:
			if move == 12:
				mouse.moveTo(530,230)
				mouse.dragTo(530,275,button="left")
			if move == 17:
				mouse.moveTo(490,275)
				mouse.dragTo(530,275,button="left")
			if move == 24:
				mouse.moveTo(530,320)
				mouse.dragTo(530,275,button="left")
			move = 18
		elif centroid_x<=400 and centroid_y>240:
			if move == 17:
				mouse.moveTo(490,275)
				mouse.dragTo(490,320,button="left")
			if move == 22:
				mouse.moveTo(445,320)
				mouse.dragTo(490,320,button="left")
			if move == 24:
				mouse.moveTo(530,320)
				mouse.dragTo(490,320,button="left")
			if move == 29:
				mouse.moveTo(490,360)
				mouse.dragTo(490,320,button="left")
			move = 23
		else:
			if move == 18:
				mouse.moveTo(530,275)
				mouse.dragTo(530,320,button="left")
			if move == 23:
				mouse.moveTo(490,320)
				mouse.dragTo(530,320,button="left")
			if move == 30:
				mouse.moveTo(530,360)
				mouse.dragTo(530,320,button="left")
			move = 24
	elif centroid_x<=160 and centroid_y<=480:
		if centroid_x<=80 and centroid_y<=400:
			if move == 19:
				mouse.moveTo(320,320)
				mouse.dragTo(320,360,button="left")
			if move == 26:
				mouse.moveTo(360,360)
				mouse.dragTo(320,360,button="left")
			if move == 31:
				mouse.moveTo(320,405)
				mouse.dragTo(320,360,button="left")
			move = 25
		elif centroid_x>80 and centroid_y<=400:
			if move == 20:
				mouse.moveTo(360,320)
				mouse.dragTo(360,360,button="left")
			if move == 25:
				mouse.moveTo(320,360)
				mouse.dragTo(360,360,button="left")
			if move == 27:
				mouse.moveTo(400,360)
				mouse.dragTo(360,360,button="left")
			if move == 32:
				mouse.moveTo(360,405)
				mouse.dragTo(360,360,button="left")
			move = 26
		elif centroid_x<=80 and centroid_y>400:
			if move == 25:
				mouse.moveTo(320,360)
				mouse.dragTo(320,405,button="left")
			if move == 32:
				mouse.moveTo(360,405)
				mouse.dragTo(320,405,button="left")
			move = 31
		else:
			if move == 26:
				mouse.moveTo(360,360)
				mouse.dragTo(360,405,button="left")
			if move == 31:
				mouse.moveTo(320,405)
				mouse.dragTo(360,405,button="left")
			if move == 33:
				mouse.moveTo(400,405)
				mouse.dragTo(360,405,button="left")
			move = 32
	elif centroid_x<=320 and centroid_y<=480:
		if centroid_x<=240 and centroid_y<=400:
			if move == 21:
				mouse.moveTo(400,320)
				mouse.dragTo(400,360,button="left")
			if move == 26:
				mouse.moveTo(360,360)
				mouse.dragTo(400,360,button="left")
			if move == 28:
				mouse.moveTo(445,360)
				mouse.dragTo(400,360,button="left")
			if move == 33:
				mouse.moveTo(400,405)
				mouse.dragTo(400,360,button="left")
			move = 27
		elif centroid_x>240 and centroid_y<=400:
			if move == 22:
				mouse.moveTo(445,320)
				mouse.dragTo(445,360,button="left")
			if move == 27:
				mouse.moveTo(400,360)
				mouse.dragTo(445,360,button="left")
			if move == 29:
				mouse.moveTo(490,360)
				mouse.dragTo(445,360,button="left")
			if move == 34:
				mouse.moveTo(445,405)
				mouse.dragTo(445,360,button="left")
			move = 28
		elif centroid_x<=240 and centroid_y>400:
			if move == 27:
				mouse.moveTo(400,360)
				mouse.dragTo(400,405,button="left")
			if move == 32:
				mouse.moveTo(360,405)
				mouse.dragTo(400,405,button="left")
			if move == 34:
				mouse.moveTo(445,405)
				mouse.dragTo(400,405,button="left")
			move = 33
		else:
			if move == 28:
				mouse.moveTo(445,360)
				mouse.dragTo(445,405,button="left")
			if move == 33:
				mouse.moveTo(400,405)
				mouse.dragTo(445,405,button="left")
			if move == 35:
				mouse.moveTo(490,405)
				mouse.dragTo(445,405,button="left")
			move = 34
	elif centroid_x<=480 and centroid_y<=480:
		if centroid_x<=400 and centroid_y<=400:
			if move == 23:
				mouse.moveTo(490,320)
				mouse.dragTo(490,360,button="left")
			if move == 28:
				mouse.moveTo(445,360)
				mouse.dragTo(490,360,button="left")
			if move == 30:
				mouse.moveTo(530,360)
				mouse.dragTo(490,360,button="left")
			if move == 35:
				mouse.moveTo(490,405)
				mouse.dragTo(490,360,button="left")
			move = 29
		elif centroid_x>400 and centroid_y<=400:
			if move == 24:
				mouse.moveTo(530,320)
				mouse.dragTo(530,360,button="left")
			if move == 29:
				mouse.moveTo(490,360)
				mouse.dragTo(530,360,button="left")
			if move == 36:
				mouse.moveTo(530,405)
				mouse.dragTo(530,360,button="left")
			move = 30
		elif centroid_x<=400 and centroid_y>400:
			if move == 29:
				mouse.moveTo(490,360)
				mouse.dragTo(490,405,button="left")
			if move == 34:
				mouse.moveTo(445,405)
				mouse.dragTo(490,405,button="left")
			if move == 36:
				mouse.moveTo(530,405)
				mouse.dragTo(490,405,button="left")
			move = 35
		else:
			if move == 30:
				mouse.moveTo(530,360)
				mouse.dragTo(530,405,button="left")
			if move == 35:
				mouse.moveTo(490,405)
				mouse.dragTo(530,405,button="left")
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
