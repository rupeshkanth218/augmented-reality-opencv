import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np

cap =cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detector=HandDetector(detectionCon=0.8)
colorR=(255,0,255)


xp,yp=0,0
imgCanvas=np.zeros((720,1280,3), np.uint8)

while True:
    success, img =cap.read()
    img = cv2.flip(img, 1)
    

    hands ,img= detector.findHands(img, draw=True) #drawing all the hand points
    
    #hands= detector.findHands(img,draw=False)
    if hands:
        fingers=detector.fingersUp(hands[0])
        
        lmList = hands[0]['lmList']
        l, _=detector.findDistance((lmList[8][0],lmList[8][1]),(lmList[4][0],lmList[4][1]))
        
        if l<40:

            x=lmList[8][0]
            y=lmList[8][1]
            if xp==0 and yp==0:
                xp,yp=x,y
            cv2.line(img, (xp,yp),(x,y),(255,0,0),5)
            cv2.line(imgCanvas, (xp,yp),(x,y),(255,0,0),5)
            xp,yp = x,y
        else:
            xp,yp=0,0
        if fingers[4]:
            imgCanvas=np.zeros((720,1280,3), np.uint8)

    
    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)    
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)

    cv2.imshow("Image", img)
    #cv2.imshow("Image", imgCanvas)
    key=cv2.waitKey(1)
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()