import numpy as np
import cv2

cap = cv2.VideoCapture('C:\\Users\\ROHAN\\Desktop\\IMG_7318.MOV')


while(cap.isOpened()):
    ret, frame = cap.read()
   # print(frame.shape)
    cv2.circle(frame,(690,200),5,(0,0,255),-1)
    cv2.circle(frame, (1100, 200), 5, (0, 0, 255), -1)
    cv2.circle(frame, (520,425 ), 5, (0, 0, 255), -1)
    cv2.circle(frame, (1240, 425), 5, (0, 0, 255), -1)
    pts1 = np.float32([[700, 200], [1080, 200], [520, 425], [1240, 425]])
    pts2=np.float32([[0,0],[400,0],[50,400],[380,400]])
    matrix=cv2.getPerspectiveTransform(pts1,pts2)
    result=cv2.warpPerspective(frame, matrix, (500,800))
    cv2.imshow("frame",frame)
    cv2.imshow("transfrom",result)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)



    cv2.imshow('frame',gray)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
