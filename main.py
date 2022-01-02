import cv2
import time
import os
import HandTracking as htm

wCam, hCam = 720, 480
pTime = 0

vid = cv2.VideoCapture(0)
vid.set(3, wCam)
vid.set(4, hCam)


folderPath = "numbers"
number_list = os.listdir(folderPath)
overlayList = []
for impath in number_list:
    image = cv2.imread(f"{folderPath}/{impath}")
    print(f"{folderPath}/{impath}")
    overlayList.append(image)

detector = htm.handDetector(detectionCon=1)

tipnumbers = [4, 8, 12, 16, 20]

while True:
    success, img = vid.read()
    detector.findHands(img)
    lmList = detector.findPosition(img,draw=False)
    #print(lmList)

    if len(lmList) != 0:
        fingers = []

        #thumb
        if lmList[tipnumbers[0]][1] > lmList[tipnumbers[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        #4 fingers
        for num in range(1,5):
            if lmList[tipnumbers[num]][2] < lmList[tipnumbers[num]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        #print(fingers)

        ##counting fingers <fingers> list
        fingersUp = fingers.count(1)
        print(fingersUp)

        h, w, c = overlayList[fingersUp].shape
        img[0:h, 0:w] = overlayList[fingersUp]

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    #cv2.putText(img, f"FPS: {int(fps)}", (400,70), cv2.FONT_HERSHEY_PLAIN,
    #           3, (255, 0, 0), 3)     #if you want to display FPS

    cv2.imshow("FINGER TRACKER", img)
    cv2.waitKey(1)

