#Load libraries
import numpy as np
import cv2

#Load the image in the img vector
img = cv2.imread("opencv-logo.png")

#for i in range(len(img)):
#    for j in range(300):
#        img[i,100+j] = [0,255,0]

#Open a Window and show the picture
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
cv2.imshow("Image",img)
#Wait the user to press any key
cv2.waitKey(0)
#Save the image as output.jpg
cv2.imwrite("output.jpg",img)
