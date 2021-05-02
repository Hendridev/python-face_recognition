import cv2
cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)
faceDect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
    retV, frame = cam.read()
    cgrade = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDect.detectMultiScale(cgrade, 1.3, 5) #fr,scale
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('Mywebcam', frame)
    # cv2.imshow('Mywebcam 2', cgrade)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()