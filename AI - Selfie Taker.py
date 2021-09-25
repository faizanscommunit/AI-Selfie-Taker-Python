#**** ---- Note --- ****#
# AI Selfie Taker - Python
# By Faizanscommunit
# MIT Licensed

#**** --- Source Code --- ****#
import cv2
cap = cv2.VideoCapture(0)
face_cacade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
while True:
    _, frame = cap.read()
    original_frame = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
    face = face_cacade.detectMultiScale(gray, 1.3, 5)
    for x, y, w, h in face:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        face_roi = frame[y:y+h, x:x+w]
        smile = smile_cascade.detectMultiScale(face_roi, 1.3, 25)
        for x1, y1, w1, h1 in smile:
            cv2.rectangle(face_roi, (x1, y1), (x1+w1, y1+h1), (0, 0, 225), 2)
            cv2.imwrite('selfie.png', original_frame)
    cv2.imshow('Selfie Project', frame)
    if cv2.waitKey(10) == ord('q'):
        break

#**** --- Social Links --- ****#
#  Github: https://github.com/faizanscommunit
#  Fiverr: https://fvrr.co/3iZIX0L
#  Website: https://faizanscommunit.pythonanywhere.com/
#  Instagram: https://www.instagram.com/faizanscommunit/
