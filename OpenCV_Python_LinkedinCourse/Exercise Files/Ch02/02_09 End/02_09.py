import numpy as np
import cv2

# Define the cap object - camera
cap = cv2.VideoCapture(0)

# Circle colo - line_width - radius and origin
color = (0,255,0)
line_width = 3
radius = 100
point = (0,0)

# Define a function to set the mouse left click input 
def click(event, x, y, flags, param):
	global point, pressed
	#Events: {EVENT_LBUTTONDOWN}
	if event == cv2.EVENT_MOUSEMOVE:
		print("Pressed",x,y)
		point = (x,y)

# Callback
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame",click)


while(True):
    #Take a frame from the cap
	ret, frame = cap.read()

	#Work on the frame
	frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)

	#Draw the circle 
	cv2.circle(frame, point, radius, color, line_width)

	#Show the frame
	cv2.imshow("Frame",frame)

	#Wait the q key
	ch = cv2.waitKey(1)
	if ch & 0xFF == ord('q'):
		break

#Close all
cap.release()
cv2.destroyAllWindows()