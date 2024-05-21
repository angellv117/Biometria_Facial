import cv2
import os
import serial
import time
import pymysql
import datetime


import pyttsx3





serialPort = 'COM4'
rate = 9600
##################################   coneccion con el arduino ###################################
try:
    serialConnecion = serial.Serial(serialPort,rate, timeout=1)
    time.sleep(2)
except:
    print("No se puede conectar")

##################################   coneccion la base de datos ###################################


dataPath = "C:/Users/AngelLv/Desktop/Biometria Proyecto/Faces"
imagePaths = os.listdir(dataPath)

print('Face =',imagePaths)

face_recognizer = cv2.face.LBPHFaceRecognizer_create()


face_recognizer.read('modeloLBPHFace.xml')

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')


#-----------------FUNCION PARA REPRODUCIR---------------#
engine = pyttsx3.init()
def reproducir(self):
    text = self
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()

#------------------- FUNCION PARA GUARDAR EN LA BASE DE DATOS ---------------#
def insertar(name):
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                database='accesos',
                                port = 3306,
                                cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            fecha = datetime.datetime.now()
            sql = "INSERT INTO `accesos`.`ingresos` (`nombre`, `fecha_a`) VALUES ('"+name+"', '"+str(fecha)+"');"
            cursor.execute(sql)
            connection.commit()

cont = 0
while True:
    ret,frame = cap.read()
    if ret == False: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()
    faces = faceClassif.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
        result = face_recognizer.predict(rostro)
        cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)

        # FisherFace
        if result[1] < 80:
            cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)

            if cont >20:
                serialConnecion.write(b'S')
                reproducir("Autorizado, pase pórfavor")
                insertar(str(imagePaths[result[0]]))
                cont = 0
                
        else:
            cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
            if cont >20:
                serialConnecion.write(b'N')
                reproducir("No autorizado")
                insertar("Desconcido")
                cont = 0
        cont += 1

    cv2.imshow('ANALISIS DE ROSTROS', frame)
    k = cv2.waitKey(1)
    if k == 27:
        break
    
cap.release()
cv2.destroyAllWindows()