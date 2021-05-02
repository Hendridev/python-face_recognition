import cv2
cam = cv2.VideoCapture(2)
while True:
    retV, frame = cam.read()
    cgrade = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('Mywebcam', frame)
    cv2.imshow('Mywebcam 2', cgrade)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()