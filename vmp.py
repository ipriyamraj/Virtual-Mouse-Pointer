import cv2
import numpy as np
import HandTrackingModule as htm
import time
import pyautogui
import autopy
from pynput.mouse import Button, Controller

mouse = Controller()

wCam, hCam = 640, 480
frameR = 100 # Frame Reduction
smoothening = 7

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()
# print(wScr, hScr)

while True:
    # For hand Landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    # To get the tip of the index and middle fingers
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        # print(x1, y1, x2, y2)

         # To Check which fingers are up
        fingers = detector.fingersUp()
        # print(fingers)
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)

        #  Only Index Finger -> Moving Mode
        if fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0 and fingers[0] == 0:

            # Convert Coordinates
            x3 = np.interp(x1, (frameR, wCam - frameR-54), (0, wScr))
            print(wCam - frameR)
            y3 = np.interp(y1, (frameR, hCam - frameR-38), (0, hScr))
            print(hCam - frameR)

            # Smoothen Values
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            # Move Mouse
            autopy.mouse.move(wScr - clocX, clocY)
            # autopy.mouse.move(wScr-x3, y3)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY
            cv2.putText(img, "moving mode", (10, 70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 70, 25), 3)

        # Both Index and middle fingers are up : Clicking Mode
        if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0 and fingers[4] == 0 and fingers[0] == 0:

            # 9. Find distance between fingers
            length, img, lineInfo = detector.findDistance(8, 12, img)
            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]),15, (0, 255, 0), cv2.FILLED)
                # mouse.scroll(0, 2)
                autopy.mouse.click(button=autopy.mouse.Button.LEFT)
                cv2.putText(img, "left click", (10, 70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 70, 25), 3)

        # When middle finger is up : Scroll down
        if fingers[1] == 0 and fingers[2] == 1 and fingers[3] == 0 and fingers[4] == 0 and fingers[0] == 0:
            mouse.scroll(0, -2)
            cv2.putText(img, "scroll down", (10, 70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 70, 25), 3)

        # When ring and little fingers are up : Scroll up
        if fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 1 and fingers[0] == 0:
            mouse.scroll(0, 2)
            cv2.putText(img, "scroll up", (10, 70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 70, 25), 3)

        # Both Index and middle fingers are up : Right Click Mode
        if fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0 and fingers[0] == 1:
            lengthi, img, lineInfo = detector.findDistance(4, 8, img)
            if lengthi < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click(button=autopy.mouse.Button.RIGHT)
                cv2.putText(img, "right click", (10, 70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 70, 25), 3)

        if fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 1 and fingers[0] == 1:
            pyautogui.click(clicks=2, interval=0.25)
            cv2.putText(img, "double click", (10, 70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 70, 25), 3)

    # 11. Frame Rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,(255, 0, 0), 3)

    # 12. Display
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
