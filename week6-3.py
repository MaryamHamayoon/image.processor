import cv2
import numpy as np

img = cv2.imread('brain.jpg' )
median = cv2.medianBlur (img, 5)
compare = np.concatenate((img, median), axis=1) 
cV2. imshow('img1', compare)
cV2.waitKey(0)
cv2. destroyAllWindows