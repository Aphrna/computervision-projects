import cv2
cap = cv2.VideoCapture(0)  # default cam 0
while True:
    key, img = cap.read()
    cv2.imshow("test_vedio", img)  # open camera
    cv2.waitKey(1)  # close
