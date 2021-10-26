import numpy as np
import cv2

#Create a new picture of 4 channel (alpha channel)
#Alpha channels are masks through which you can display images. The alpha channel is an 8-bit channel, which means it has 256 levels of gray from 0
#(black) to 255 (white). White acts as the visible area; black acts as the transparent area (you see the background behind the image when displayed).
#The level of gray in between determines the level of visibility

color = cv2.imread("unnamed.jpg",1)

#Gray scale picture
#gray = cv2.cvtColor(color, cv2.COLOR_RGB2GRAY)
#cv2.imwrite("gray.jpg",gray)

#Split the channels - this method is faster than the cv2.split() function
b = color[:,:,0]
g = color[:,:,1]
r = color[:,:,2]

#Create a channel to merge, it is a mask
height,width,channel = color.shape
alpha_channel = np.ones([height,width])



for row in range(height):
    for col in range(width):
        if color[row][col][0] == 255 and color[row][col][1] == 255 and color[row][col][2] == 255:
            alpha_channel[row][col] = 0

cv2.imshow("Alpha Channel", alpha_channel)
print(alpha_channel.shape)
print(b.shape)           

#A second way to create a rgba figure is:
rgba2 = cv2.cvtColor(color, cv2.COLOR_RGB2RGBA)
rgba2[:, :, 3] = alpha_channel

#Create a new figure merging the 4th channel
rgba2 = cv2.merge((b,g,r,alpha_channel))

#Show the mask
cv2.imshow("Result", rgba2)
cv2.moveWindow("Alpha Channel", 200 , 20)

cv2.waitKey(0)

#Save figures
#cv2.imwrite("rgba.png",rgba)
cv2.imwrite("rgba2.png",alpha_channel)
