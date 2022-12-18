import cv2
import numpy as np
img=cv2.imread('input.png',0)
kernel = np.ones((5,5),np.unit8)
img_erosion =cv2.erode(img,kernel,iterations=1)
img_dilation =cv2.dilate(img,kernek, iterations=1)
cv2.imshow('input',img)
cv2.imshow('erosion',img_erosion)
cv2.imshow('Dilation',img_dilation)
cv2.waitKey(0)
