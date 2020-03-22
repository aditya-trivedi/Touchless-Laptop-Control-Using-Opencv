# Touchless-Laptop-Control-Using-Opencv

A pen attached with a red circle paper is used to control a laptop. The Project uses Multiple Python libraries but primarily focuses on opencv(cv2) and pyautogui.

Before The user starts using the application , the user must :
1. Configure HSV values in the following lines:
    cv2.createTrackbar("L-H","Trackbars",0,180,nothing)
    cv2.createTrackbar("L-S","Trackbars",195,255,nothing)
    cv2.createTrackbar("L-V","Trackbars",108,255,nothing)
    cv2.createTrackbar("U-H","Trackbars",180,180,nothing)
    cv2.createTrackbar("U-S","Trackbars",255,255,nothing)
    cv2.createTrackbar("U-V","Trackbars",255,255,nothing)
2. L referes to lower hsv values, while U refers to upper HSV values.
3. The above step is performed to ensure the colour of pen is distinguished from background.
