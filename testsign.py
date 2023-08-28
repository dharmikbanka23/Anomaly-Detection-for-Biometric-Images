import cv2
import sys
import numpy as np

imagePath=sys.argv[1]
img=cv2.imread(imagePath)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
(thresh, bw) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

whitepix = np.sum(bw == 255)
blackpix = np.sum(bw == 0)

s = blackpix/(whitepix+blackpix)
if s <= 0.10 and s>=0.015:
	print("1")
else:
	print("0")

#print('Number of white pixels:', whitepix)
#print('Number of black pixels:', blackpix)
#cv2.imwrite("ok.jpg",bw)