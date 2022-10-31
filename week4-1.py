import cv2
import numpy as np 
img= cv2.imread("olives.jpg")
imgGri= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("zeytin fotosu",img)
cv2.imshow("zeytin fotosu Gri",imgGri)
size_y=imgGri.shape[o]
size_x=imgGri.shape[1]
print ("yükseklik:",size_y,"Genislik:", size_x)
print (img[ (100,100) ])
print (imgGri[(100,100)])
cv2.waitkey(0)
cv2. destroyAllwindows()