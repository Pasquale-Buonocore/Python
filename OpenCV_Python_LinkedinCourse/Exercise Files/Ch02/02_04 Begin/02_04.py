import numpy as np
import cv2

color = cv2.imread("butterfly.jpg", 1)

#Show the picture and move the window on the top left corner
cv2.imshow("Image",color)
cv2.moveWindow("Image",1000,0)

#Show the height - width - channels of the picture 
print(color.shape)
height,width,channels = color.shape


#Split the picture in the three channels blue green red
b,g,r = cv2.split(color)

#Create an empty array
rgb_split = np.empty([height,width*3,3],'uint8')

#Fill in the empty array with the three channels r,g,b
rgb_split[:, 0:width] = cv2.merge([b,b,b])
rgb_split[:, width:width*2] = cv2.merge([g,g,g])
rgb_split[:, width*2:width*3] = cv2.merge([r,r,r])

#Show the image
cv2.imshow("Channels",rgb_split)
cv2.moveWindow("Channels",0,height)

#Now take a look at the hue,saturation,value space
hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
hsv_split = np.concatenate((h,s,v),axis=1)
cv2.imshow("Split HSV",hsv_split)

#Wait key - Press esc to close the program
cv2.waitKey(0)
cv2.destroyAllWindows()