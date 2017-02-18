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
				mouse.moveTo(125,245)
				mouse.dragTo(50,245,button="left")
			if move == 7:
				mouse.moveTo(50,315)
				mouse.dragTo(50,245,button="left")
			move = 1
		elif centroid_x>80 and centroid_y<=80:
			if move == 1:
				mouse.moveTo(50,245)
				mouse.dragTo(125,245,button="left")
			if move == 8:
				mouse.moveTo(125,315)
				mouse.dragTo(125,245,button="left")
			if move == 3:
				mouse.moveTo(190,245)
				mouse.dragTo(125,245,button="left")
			move = 2
		elif centroid_x<=80 and centroid_y>80:
			if move == 1:
				mouse.moveTo(50,245)
				mouse.dragTo(50,315,button="left")
			if move == 8:
				mouse.moveTo(125,315)
				mouse.dragTo(50,315,button="left")
			if move == 13:
				mouse.moveTo(50,385)
				mouse.dragTo(50,315,button="left")
			move = 7
		else:
			if move == 2:
				mouse.moveTo(125,245)
				mouse.dragTo(125,315,button="left")
			if move == 7:
				mouse.moveTo(50,315)
				mouse.dragTo(125,315,button="left")
			if move == 9:
				mouse.moveTo(190,315)
				mouse.dragTo(125,315,button="left")
			if move == 14:
				mouse.moveTo(125,385)
				mouse.dragTo(125,315,button="left")
			move = 8
	elif centroid_x<=320 and centroid_y<=160:
		if centroid_x<=240 and centroid_y<=80:
			if move == 2:
				mouse.moveTo(125,245)
				mouse.dragTo(190,245,button="left")
			if move == 4:
				mouse.moveTo(270,245)
				mouse.dragTo(190,245,button="left")
			if move == 9:
				mouse.moveTo(190,315)
				mouse.dragTo(190,245,button="left")
			move = 3
		elif centroid_x>240 and centroid_y<=80:
			if move == 3:
				mouse.moveTo(190,245)
				mouse.dragTo(270,245,button="left")
			if move == 5:
				mouse.moveTo(335,245)
				mouse.dragTo(270,245,button="left")
			if move == 10:
				mouse.moveTo(270,315)
				mouse.dragTo(270,245,button="left")
			move = 4
		elif centroid_x<=240 and centroid_y>80:
			if move == 3:
				mouse.moveTo(190,245)
				mouse.dragTo(190,315,button="left")
			if move == 8:
				mouse.moveTo(125,315)
				mouse.dragTo(190,315,button="left")
			if move == 10:
				mouse.moveTo(270,315)
				mouse.dragTo(190,315,button="left")
			if move == 15:
				mouse.moveTo(190,385)
				mouse.dragTo(190,315,button="left")
			move = 9
		else:
			if move == 4:
				mouse.moveTo(270,245)
				mouse.dragTo(270,315,button="left")
			if move == 9:
				mouse.moveTo(190,315)
				mouse.dragTo(270,315,button="left")
			if move == 11:
				mouse.moveTo(335,315)
				mouse.dragTo(270,315,button="left")
			if move == 16:
				mouse.moveTo(270,385)
				mouse.dragTo(270,315,button="left")
			move = 10
	elif centroid_x<=480 and centroid_y<=160:
		if centroid_x<=400 and centroid_y<=80:
			if move == 4:
				mouse.moveTo(270,245)
				mouse.dragTo(335,245,button="left")
			if move == 6:
				mouse.moveTo(410,245)
				mouse.dragTo(335,245,button="left")
			if move == 11:
				mouse.moveTo(335,315)
				mouse.dragTo(335,245,button="left")
			move = 5
		elif centroid_x>400 and centroid_y<=80:
			if move == 5:
				mouse.moveTo(335,245)
				mouse.dragTo(410,245,button="left")
			if move == 12:
				mouse.moveTo(410,315)
				mouse.dragTo(410,245,button="left")
			move = 6
		elif centroid_x<=400 and centroid_y>80:
			if move == 5:
				mouse.moveTo(335,245)
				mouse.dragTo(335,315,button="left")
			if move == 10:
				mouse.moveTo(270,315)
				mouse.dragTo(335,315,button="left")
			if move == 12:
				mouse.moveTo(410,315)
				mouse.dragTo(335,315,button="left")
			if move == 17:
				mouse.moveTo(335,385)
				mouse.dragTo(335,315,button="left")
			move = 11
		else:
			if move == 6:
				mouse.moveTo(410,245)
				mouse.dragTo(410,315,button="left")
			if move == 11:
				mouse.moveTo(335,315)
				mouse.dragTo(410,315,button="left")
			if move == 18:
				mouse.moveTo(410,385)
				mouse.dragTo(410,315,button="left")
			move = 12
	elif centroid_x<=160 and centroid_y<=320:
		if centroid_x<=80 and centroid_y<=240:
			if move == 7:
				mouse.moveTo(50,315)
				mouse.dragTo(50,385,button="left")
			if move == 14:
				mouse.moveTo(125,385)
				mouse.dragTo(50,385,button="left")
			if move == 19:
				mouse.moveTo(50,460)
				mouse.dragTo(50,385,button="left")
			move = 13
		elif centroid_x>80 and centroid_y<=240:
			if move == 8:
				mouse.moveTo(125,315)
				mouse.dragTo(125,385,button="left")
			if move == 13:
				mouse.moveTo(50,385)
				mouse.dragTo(125,385,button="left")
			if move == 15:
				mouse.moveTo(190,385)
				mouse.dragTo(125,385,button="left")
			if move == 20:
				mouse.moveTo(125,460)
				mouse.dragTo(125,385,button="left")
			move = 14
		elif centroid_x<=80 and centroid_y>240:
			if move == 13:
				mouse.moveTo(50,385)
				mouse.dragTo(50,460,button="left")
			if move == 20:
				mouse.moveTo(125,460)
				mouse.dragTo(50,460,button="left")
			if move == 25:
				mouse.moveTo(50,535)
				mouse.dragTo(50,460,button="left")
			move = 19
		else:
			if move == 14:
				mouse.moveTo(125,385)
				mouse.dragTo(125,460,button="left")
			if move == 19:
				mouse.moveTo(50,460)
				mouse.dragTo(125,460,button="left")
			if move == 21:
				mouse.moveTo(190,460)
				mouse.dragTo(125,460,button="left")
			if move == 26:
				mouse.moveTo(125,535)
				mouse.dragTo(125,460,button="left")
			move = 20
	elif centroid_x<=320 and centroid_y<=320:
		if centroid_x<=240 and centroid_y<=240:
			if move == 9:
				mouse.moveTo(190,315)
				mouse.dragTo(190,385,button="left")
			if move == 14:
				mouse.moveTo(125,385)
				mouse.dragTo(190,385,button="left")
			if move == 16:
				mouse.moveTo(270,385)
				mouse.dragTo(190,385,button="left")
			if move == 21:
				mouse.moveTo(190,460)
				mouse.dragTo(190,385,button="left")
			move = 15
		elif centroid_x>240 and centroid_y<=240:
			if move == 10:
				mouse.moveTo(270,315)
				mouse.dragTo(270,385,button="left")
			if move == 15:
				mouse.moveTo(190,385)
				mouse.dragTo(270,385,button="left")
			if move == 17:
				mouse.moveTo(335,385)
				mouse.dragTo(270,385,button="left")
			if move == 22:
				mouse.moveTo(270,460)
				mouse.dragTo(270,385,button="left")
			move = 16
		elif centroid_x<=240 and centroid_y>240:
			if move == 15:
				mouse.moveTo(190,385)
				mouse.dragTo(190,460,button="left")
			if move == 20:
				mouse.moveTo(125,460)
				mouse.dragTo(190,460,button="left")
			if move == 22:
				mouse.moveTo(270,460)
				mouse.dragTo(190,460,button="left")
			if move == 27:
				mouse.moveTo(190,535)
				mouse.dragTo(190,460,button="left")
			move = 21
		else:
			if move == 16:
				mouse.moveTo(270,385)
				mouse.dragTo(270,460,button="left")
			if move == 21:
				mouse.moveTo(190,460)
				mouse.dragTo(270,460,button="left")
			if move == 23:
				mouse.moveTo(335,460)
				mouse.dragTo(270,460,button="left")
			if move == 28:
				mouse.moveTo(270,535)
				mouse.dragTo(270,460,button="left")
			move = 22
	elif centroid_x<=480 and centroid_y<=320:
		if centroid_x<=400 and centroid_y<=240:
			if move == 11:
				mouse.moveTo(335,315)
				mouse.dragTo(335,385,button="left")
			if move == 16:
				mouse.moveTo(270,385)
				mouse.dragTo(335,385,button="left")
			if move == 18:
				mouse.moveTo(410,385)
				mouse.dragTo(335,385,button="left")
			if move == 23:
				mouse.moveTo(335,460)
				mouse.dragTo(335,385,button="left")
			move = 17
		elif centroid_x>400 and centroid_y<=240:
			if move == 12:
				mouse.moveTo(410,315)
				mouse.dragTo(410,385,button="left")
			if move == 17:
				mouse.moveTo(335,385)
				mouse.dragTo(410,385,button="left")
			if move == 24:
				mouse.moveTo(410,460)
				mouse.dragTo(410,385,button="left")
			move = 18
		elif centroid_x<=400 and centroid_y>240:
			if move == 17:
				mouse.moveTo(335,385)
				mouse.dragTo(335,460,button="left")
			if move == 22:
				mouse.moveTo(270,460)
				mouse.dragTo(335,460,button="left")
			if move == 24:
				mouse.moveTo(410,460)
				mouse.dragTo(335,460,button="left")
			if move == 29:
				mouse.moveTo(335,535)
				mouse.dragTo(335,460,button="left")
			move = 23
		else:
			if move == 18:
				mouse.moveTo(410,385)
				mouse.dragTo(410,460,button="left")
			if move == 23:
				mouse.moveTo(335,460)
				mouse.dragTo(410,460,button="left")
			if move == 30:
				mouse.moveTo(410,535)
				mouse.dragTo(410,460,button="left")
			move = 24
	elif centroid_x<=160 and centroid_y<=480:
		if centroid_x<=80 and centroid_y<=400:
			if move == 19:
				mouse.moveTo(50,460)
				mouse.dragTo(50,535,button="left")
			if move == 26:
				mouse.moveTo(125,535)
				mouse.dragTo(50,535,button="left")
			if move == 31:
				mouse.moveTo(50,605)
				mouse.dragTo(50,535,button="left")
			move = 25
		elif centroid_x>80 and centroid_y<=400:
			if move == 20:
				mouse.moveTo(125,460)
				mouse.dragTo(125,535,button="left")
			if move == 25:
				mouse.moveTo(50,535)
				mouse.dragTo(125,535,button="left")
			if move == 27:
				mouse.moveTo(190,535)
				mouse.dragTo(125,535,button="left")
			if move == 32:
				mouse.moveTo(125,605)
				mouse.dragTo(125,535,button="left")
			move = 26
		elif centroid_x<=80 and centroid_y>400:
			if move == 25:
				mouse.moveTo(50,535)
				mouse.dragTo(50,605,button="left")
			if move == 32:
				mouse.moveTo(125,605)
				mouse.dragTo(50,605,button="left")
			move = 31
		else:
			if move == 26:
				mouse.moveTo(125,535)
				mouse.dragTo(125,605,button="left")
			if move == 31:
				mouse.moveTo(50,605)
				mouse.dragTo(125,605,button="left")
			if move == 33:
				mouse.moveTo(190,605)
				mouse.dragTo(125,605,button="left")
			move = 32
	elif centroid_x<=320 and centroid_y<=480:
		if centroid_x<=240 and centroid_y<=400:
			if move == 21:
				mouse.moveTo(190,460)
				mouse.dragTo(190,535,button="left")
			if move == 26:
				mouse.moveTo(125,535)
				mouse.dragTo(190,535,button="left")
			if move == 28:
				mouse.moveTo(270,535)
				mouse.dragTo(190,535,button="left")
			if move == 33:
				mouse.moveTo(190,605)
				mouse.dragTo(190,535,button="left")
			move = 27
		elif centroid_x>240 and centroid_y<=400:
			if move == 22:
				mouse.moveTo(270,460)
				mouse.dragTo(270,535,button="left")
			if move == 27:
				mouse.moveTo(190,535)
				mouse.dragTo(270,535,button="left")
			if move == 29:
				mouse.moveTo(335,535)
				mouse.dragTo(270,535,button="left")
			if move == 34:
				mouse.moveTo(270,605)
				mouse.dragTo(270,535,button="left")
			move = 28
		elif centroid_x<=240 and centroid_y>400:
			if move == 27:
				mouse.moveTo(190,535)
				mouse.dragTo(190,605,button="left")
			if move == 32:
				mouse.moveTo(125,605)
				mouse.dragTo(190,605,button="left")
			if move == 34:
				mouse.moveTo(270,605)
				mouse.dragTo(190,605,button="left")
			move = 33
		else:
			if move == 28:
				mouse.moveTo(270,535)
				mouse.dragTo(270,605,button="left")
			if move == 33:
				mouse.moveTo(190,605)
				mouse.dragTo(270,605,button="left")
			if move == 35:
				mouse.moveTo(335,605)
				mouse.dragTo(270,605,button="left")
			move = 34
	elif centroid_x<=480 and centroid_y<=480:
		if centroid_x<=400 and centroid_y<=400:
			if move == 23:
				mouse.moveTo(335,460)
				mouse.dragTo(335,535,button="left")
			if move == 28:
				mouse.moveTo(270,535)
				mouse.dragTo(335,535,button="left")
			if move == 30:
				mouse.moveTo(410,535)
				mouse.dragTo(335,535,button="left")
			if move == 35:
				mouse.moveTo(335,605)
				mouse.dragTo(335,535,button="left")
			move = 29
		elif centroid_x>400 and centroid_y<=400:
			if move == 24:
				mouse.moveTo(410,460)
				mouse.dragTo(410,535,button="left")
			if move == 29:
				mouse.moveTo(335,535)
				mouse.dragTo(410,535,button="left")
			if move == 36:
				mouse.moveTo(410,605)
				mouse.dragTo(410,535,button="left")
			move = 30
		elif centroid_x<=400 and centroid_y>400:
			if move == 29:
				mouse.moveTo(335,535)
				mouse.dragTo(335,605,button="left")
			if move == 34:
				mouse.moveTo(270,605)
				mouse.dragTo(335,605,button="left")
			if move == 36:
				mouse.moveTo(410,605)
				mouse.dragTo(335,605,button="left")
			move = 35
		else:
			if move == 30:
				mouse.moveTo(410,535)
				mouse.dragTo(410,605,button="left")
			if move == 35:
				mouse.moveTo(335,605)
				mouse.dragTo(410,605,button="left")
			move = 36
	
	print "Move:", move
	
	cv2.rectangle(frame,(0,0),(80,80),(0,0,0))
	cv2.rectangle(frame,(81,0),(160,80),(0,0,0))
	cv2.rectangle(frame,(161,0),(240,80),(0,0,0))
	cv2.rectangle(frame,(241,0),(320,80),(0,0,0))
	cv2.rectangle(frame,(321,0),(400,80),(0,0,0))
	cv2.rectangle(frame,(401,0),(480,80),(0,0,0))
	cv2.rectangle(frame,(0,81),(80,160),(0,0,0))
	cv2.rectangle(frame,(81,81),(160,160),(0,0,0))
	cv2.rectangle(frame,(161,81),(240,160),(0,0,0))
	cv2.rectangle(frame,(241,81),(320,160),(0,0,0))
	cv2.rectangle(frame,(321,81),(400,160),(0,0,0))
	cv2.rectangle(frame,(401,81),(480,160),(0,0,0))
	cv2.rectangle(frame,(0,161),(80,240),(0,0,0))
	cv2.rectangle(frame,(81,161),(160,240),(0,0,0))
	cv2.rectangle(frame,(161,161),(240,240),(0,0,0))
	cv2.rectangle(frame,(241,161),(320,240),(0,0,0))
	cv2.rectangle(frame,(321,161),(400,240),(0,0,0))
	cv2.rectangle(frame,(401,161),(480,240),(0,0,0))
	cv2.rectangle(frame,(0,241),(80,320),(0,0,0))
	cv2.rectangle(frame,(81,241),(160,320),(0,0,0))
	cv2.rectangle(frame,(161,241),(240,320),(0,0,0))
	cv2.rectangle(frame,(241,241),(320,320),(0,0,0))
	cv2.rectangle(frame,(321,241),(400,320),(0,0,0))
	cv2.rectangle(frame,(401,241),(480,320),(0,0,0))
	cv2.rectangle(frame,(0,321),(80,400),(0,0,0))
	cv2.rectangle(frame,(81,321),(160,400),(0,0,0))
	cv2.rectangle(frame,(161,321),(240,400),(0,0,0))
	cv2.rectangle(frame,(241,321),(320,400),(0,0,0))
	cv2.rectangle(frame,(321,321),(400,400),(0,0,0))
	cv2.rectangle(frame,(401,321),(480,400),(0,0,0))
	cv2.rectangle(frame,(0,401),(80,480),(0,0,0))
	cv2.rectangle(frame,(81,401),(160,480),(0,0,0))
	cv2.rectangle(frame,(161,401),(240,480),(0,0,0))
	cv2.rectangle(frame,(241,401),(320,480),(0,0,0))
	cv2.rectangle(frame,(321,401),(400,480),(0,0,0))
	cv2.rectangle(frame,(401,401),(480,480),(0,0,0))
	
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cap.destroyAllWindows()
