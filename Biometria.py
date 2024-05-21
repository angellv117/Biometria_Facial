'''import cv2
import os
import serial
import time


import pyttsx3





serialPort = 'COM4'
rate = 9600

try:
    serialConnecion = serial.Serial(serialPort,rate, timeout=1)
    time.sleep(2)
except:
    print("No se puede conectar")


#-----------------FUNCION PARA REPRODUCIR---------------#
engine = pyttsx3.init()
def reproducir(self):
    text = self
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()


serialConnecion.write(b'S')
reproducir("Autorizado, pase pórfavor")
time.sleep(3)
serialConnecion.write(b'N')
reproducir("No autorizado")
           '''
import datetime
import time
fecha = datetime.datetime.now()
while True:
    print("Fecha 1:" +str(fecha.second))
    fecha2 = datetime.datetime.now()
    print("Fecha 1:" +str(fecha2.second))
    difereicnia =fecha2 - fecha
    print("Diferenica: "+str(difereicnia))
    time.sleep(1)