import numpy as np
import cv2

# Circle color - line_width - radius and origin
color = (0,255,0)
line_width = 3
radius = 100
canvas = np.ones([500,500,3],'uint8')*255
selected_color = 0

# click callback
def click(event, x, y, flags, param):
	global canvas
	global color
	global selected_color
	# DRAW SMALL CIRCLE
	if event == cv2.EVENT_LBUTTONDOWN:
		print("LButton Down")
		#Draw the circle 
		point = (x,y)
		cv2.circle(canvas, point, 50 , color, line_width)

	# CHANGE COLOR
	elif event == cv2.EVENT_MBUTTONDOWN:
		print("Change Color")
		color = (255,255,0)
		
	
    					
		
    					
	#DRAW BIG CIRCLE
	elif event == cv2.EVENT_RBUTTONDOWN:
		print("RButton Down")
		#Draw the circle
		color = (0,255,0)
		


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
	

cv2.destroyAllWindows()