import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
	ret, frame = cap.read()

	frame = cv2.resize(frame, (0,0), fx=2,fy= 2)
	cv2.imshow("Frame",frame)

	ch = cv2.waitKey(1)
	if ch == ord('f'):
		break

cap.release()
cv2.destroyAllWindows()