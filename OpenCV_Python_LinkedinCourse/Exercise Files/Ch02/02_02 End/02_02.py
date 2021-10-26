#Import library
import numpy as np
import cv2

#Read the colored images
img = cv2.imread("opencv-logo.png", 1)

#Show image
img

#Show the image type
type(img)

#Show the number of rows
len(img)

#Show the number of columns
len(img[0])

#Show the number of channels for each pixel (rgb)
len(img[0][0])

#Show the same information easier
img.shape

#Show the type of each pixel (unint8 means unsigned int 8 bit, which means that each channel has a range of 256 value)
img.dtype

#Show the pixel at row 10 and columns 5
img[10, 5]

#Show the layer 0 for all the image
img[:, :, 0]

#Total size of pixels
img.size
