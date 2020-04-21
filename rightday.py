import numpy as np
import cv2

cap = cv2.VideoCapture('C:\\Users\\ROHAN\\Desktop\\IMG_7322 (1).MOV')


while(cap.isOpened()):
    ret, frame = cap.read()
    print(frame.shape)
    cv2.circle(frame,(510,405),5,(0,0,255),-1)
    cv2.circle(frame, (915, 405), 5, (0, 0, 255), -1)
    cv2.circle(frame, (350,725 ), 5, (0, 0, 255), -1)
    cv2.circle(frame, (1080, 725), 5, (0, 0, 255), -1)
    pts1=np.float32([[510,405],[915,405],[350,725],[1080,725]])
    pts2=np.float32([[0,0],[700,0],[80,500],[620,500]])
    matrix=cv2.getPerspectiveTransform(pts1,pts2)
    result=cv2.warpPerspective(frame, matrix, (1000,700))
    cv2.imshow("frame",frame)
    cv2.imshow("transfrom",result)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)



    cv2.imshow('frame',gray)
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
