import cv2
import numpy as np

img = cv2.imread('olives.jpg')

kernel = np.ones((5,5), np.float32)/30
img=cv2.filter2D(src=image, ddepth=-1, kernel=kernek1)
cv2.imageshow('original',image)
cv2.imageshow('kernel blur',img)
cv2.waitKey()
cv2.destroyAllWindows()