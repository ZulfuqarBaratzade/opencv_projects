import cv2
import numpy as np



cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height= int(cap.get(4))
    #blue line
    img = cv2.line(frame,(0,0),(width,height),(255,0,0))
    #another line
    img = cv2.line(img,(0,height),(width,0),(255,0,0),5)
    #rectange line
    img = cv2.rectangle(img,(100,100),(200,200),(0,0,255),5)
    #circle
    img = cv2.circle(img,(300,300),60,(0,0,255),-1)
    #text
    font = cv2.FONT_HERSHEY_COMPLEX
    img=cv2.putText(img,'Zulfugar',(5,height - 10),font,2,(0,0,0),5,cv2.LINE_AA)
    cv2.imshow("frame",img)


    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()