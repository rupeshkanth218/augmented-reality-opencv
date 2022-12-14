import cv2
from cvzone.HandTrackingModule import HandDetector

cap =cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detector=HandDetector(detectionCon=0.8)
colorR=(255,0,255)
cx, cy, w, h= 100,100,200,200


class DragRect():
    def __init__(self, posCenter, size=[200,200]):
        self.posCenter = posCenter
        self.size=size
    
    def update(self, cursor):
        cx,cy=self.posCenter
        w,h=self.size
        # if the index finger tip is in the rectangle region
        if cx-w//2<cursor[0]<cx+w//2 and cy-h//2<cursor[1]<cy+h//2:
            self.posCenter=[cursor[0],cursor[1]]

rectlist=[]     
for x in range(5):
    rectlist.append(DragRect([x*250+150, 150],[w,h]))


while True:
    success, img =cap.read()
    img = cv2.flip(img, 1)
    

    hands ,img= detector.findHands(img, draw=True) #drawing all the hand points
    #hands= detector.findHands(img,draw=False)
    
    if hands:
        lmList = hands[0]['lmList']
        l, _, __=detector.findDistance((lmList[8][0],lmList[8][1]),(lmList[12][0],lmList[12][1]),img)
        
        if l<50:
            
            cursor = lmList[8]
            for rect in rectlist:
                rect.update(cursor)   
    for rect in rectlist:        
        cx,cy=rect.posCenter
        w,h=rect.size        
        cv2.rectangle(img, (cx-w//2,cy-h//2),(cx+w//2,cy+h//2), colorR ,cv2.FILLED)
    cv2.imshow("Image", img)
    key=cv2.waitKey(1)
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()