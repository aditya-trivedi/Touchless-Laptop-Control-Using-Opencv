import cv2
import numpy as np
import pyautogui
pyautogui.FAILSAFE = False


def nothing(x):
    pass

prevx = 2000
prevy = 2000
count= 0

cap = cv2.VideoCapture(0)

cv2.namedWindow("Trackbars")
cv2.createTrackbar("L-H","Trackbars",0,180,nothing)
cv2.createTrackbar("L-S","Trackbars",195,255,nothing)
cv2.createTrackbar("L-V","Trackbars",108,255,nothing)
cv2.createTrackbar("U-H","Trackbars",180,180,nothing)
cv2.createTrackbar("U-S","Trackbars",255,255,nothing)
cv2.createTrackbar("U-V","Trackbars",255,255,nothing)
cv2.resizeWindow('Frame', 1920,1080)

while True:
    _,frame = cap.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_h =  cv2.getTrackbarPos("L-H","Trackbars")
    l_s =  cv2.getTrackbarPos("L-S","Trackbars")
    l_v =  cv2.getTrackbarPos("L-V","Trackbars")
    u_h =  cv2.getTrackbarPos("U-H","Trackbars")
    u_s =  cv2.getTrackbarPos("U-S","Trackbars")
    u_v =  cv2.getTrackbarPos("U-V","Trackbars")

    lower_red = np.array([l_h,l_s,l_v])
    upper_red = np.array([u_h,u_s,u_v])

    mask = cv2.inRange(hsv,lower_red , upper_red)
    kernel = np.ones((5,5),np.uint8)
    mask = cv2.erode(mask,kernel)

    contours , _ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) != 0:
        c = max(contours,key = cv2.contourArea)
        area = cv2.contourArea(c)
        if area > 200:
            x,y,w,h = cv2.boundingRect(c)
            cv2.circle(frame, (x+int(w/2), y+int(h/2)), 2, (0, 255, 0), -1)
            x3 = x*3.2
            y3 = y*3.2
            if x3 > 1919 :
                x3 = 1919
            if y3 >1079:
                y3 = 1079
            if abs(prevx - x3) > 30 and abs(prevy - y3) > 30:
                pyautogui.moveTo(1920-x3,y3,0)
                prevx = x3
                prevu = y3
                count = 0
            else:
                count = count+1
                if count==30:
                    pyautogui.click(1920-x3,y3)
                    count = 0


    #cv2.imshow("Frame",frame)
    #cv2.imshow("Mask" ,mask)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
