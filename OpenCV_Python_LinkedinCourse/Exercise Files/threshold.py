import numpy as np
import cv2

#Load image in 01
baw = cv2.imread("index.jpeg",0)
#Load image in colors
color = cv2.imread("index.jpeg",1)
b = color[:,:,0]
g = color[:,:,1]
r = color[:,:,2]

#Create mask from the baw
ret,thresh2 = cv2.threshold(baw,150,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Mask",thresh2)


fin = cv2.merge((thresh2,thresh2,thresh2,thresh2))
#ret,res2 = cv2.threshold(res,127,255,cv2.THRESH_BINARY)
#ret,res3 = cv2.threshold(res2,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Fin",fin)
cv2.waitKey(0)


cv2.imwrite("rgba2.png",fin)