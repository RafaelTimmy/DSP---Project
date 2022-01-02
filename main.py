import time
import os

wCam, hCam = 648, 488  

vid = cv2.VideoCapture(0)  
vid.set(3, wCam)
vid.set(4, hCam) 

while True:
    success, img = vid.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1)
