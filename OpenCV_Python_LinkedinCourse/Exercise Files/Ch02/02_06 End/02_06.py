import numpy as np
import cv2
#FIltering function useful to reduce noise and highlight certain spots 
# - Gaussian Blur : It blurs a picture by averaging the pixel with its neighbours. 
#                   It is called Gaussian because pixels closer to the main one have a bigger weight.
#                   It is usually used to smooth noise before other operations

image = cv2.imread("thresh.jpg")
cv2.imshow("Original",image)

blur = cv2.GaussianBlur(image, (5,55),0)
cv2.imshow("Blur",blur)

# - Erosion : It is used to remove small pixel in order to highlight deltails. It changes white pixels in black pixels and the result is obtained by moving
#             a mask over the figure.

kernel = np.ones((5,5),'uint8')
erode = cv2.erode(image,kernel,iterations=2)


# - Dilation : It is used to remove small pixel in order to highlight deltails. It changes black pixels in white pixels and the result is obtained by moving
#             a mask over the figure.

dilate = cv2.dilate(erode,kernel,iterations=1)

# Show figures
cv2.imshow("Dilate",dilate)
cv2.imshow("Erode",erode)

cv2.waitKey(0)
cv2.destroyAllWindows()