import numpy as np
import cv2

cap = cv2.VideoCapture('C:\\Users\\ROHAN\\Desktop\\IMG_7323 (1).MOV')


while(cap.isOpened()):
    ret, frame = cap.read()
    print(frame.shape)
    cv2.circle(frame,(710,305),5,(0,0,255),-1)
    cv2.circle(frame, (1085, 305), 5, (0, 0, 255), -1)
    cv2.circle(frame, (450,500 ), 5, (0, 0, 255), -1)
    cv2.circle(frame, (1280, 500), 5, (0, 0, 255), -1)
    pts1=np.float32([[650,305],[1250,305],[450,500],[1280,500]])
    pts2=np.float32([[0,0],[400,0],[0,500],[300,500]])
    matrix=cv2.getPerspectiveTransform(pts1,pts2)
    result=cv2.warpPerspective(frame, matrix, (400,600))
    cv2.imshow("frame",frame)
    cv2.imshow("transfrom",result)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)



    cv2.imshow('frame',gray)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
