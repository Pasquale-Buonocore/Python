import numpy as np
import cv2

# Global variables
canvas = np.ones([500,500,3],'uint8')*255
radius = 3
color = (0,255,0)
pressed = True
point_ini = (0,0)
point_end = (0,0)
point_act = (0,0)


def click(event, x, y, flags, param):
	global canvas, pressed, point_ini, point_end, point_act

	if event == cv2.EVENT_LBUTTONDOWN:
		pressed = True
		point_ini = (x,y)
	elif event == cv2.EVENT_MOUSEMOVE and pressed == True:
		point_act = (x,y)
	elif event == cv2.EVENT_LBUTTONUP:
    		point_end = (x,y)
		cv2.line(canvas,point_ini,point_end,(255,0,0),5)
		pressed = False


# window initialization and callback assignment
cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas", click)

# Forever draw loop
while True:

	cv2.imshow("canvas",canvas)

	# key capture every 1ms
	ch = cv2.waitKey(1)
	if ch & 0xFF == ord('q'):
		break
	elif ch & 0xFF == ord('b'):
		color = (255,0,0)
	elif ch & 0xFF == ord('g'):
		color = (0,255,0)
	
cv2.destroyAllWindows()