import cv2
import os
import imutils

personaNAME= "Daniel"
dataPath = "C:/Users/AngelLv/Desktop/Biometria Proyecto/Faces"
personaPath = dataPath + "/"+ personaNAME


if not os.path.exists(personaPath):
    print("Carpeta creada :"+personaNAME)
    os.makedirs( personaPath )

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cont = 0

while  True:
    ret, frame= cap.read()
    if ret == False: break
    frame = imutils.resize(frame, width=640)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxframe = frame.copy()

    faces = faceClassif.detectMultiScale(gray, 1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,+h), (0,255,0),2)
        rostro= auxframe[y:y+h,x:x+w]
        rostro = cv2.resize(rostro, (150,150), interpolation= cv2.INTER_CUBIC)
        cv2.imwrite(personaPath+ "/rostro_{}.jpg".format(cont), rostro)  
        cont= cont+1
    cv2.imshow("frame", frame)

    k= cv2.waitKey(1)
    if k==27 or cont>=600:
        break

cap.release()
cv2.destroyAllWindows()

    
