# Proyecto de Reconocimiento Facial con Arduino y Python

## Descripción
Este proyecto combina el uso de Arduino y Python para implementar un sistema de reconocimiento facial que permite el acceso a un cuarto (maqueta). Además, registra quién entra en una base de datos MySQL.

## Características
Reconocimiento Facial: Utiliza Python y OpenCV para identificar a las personas.
Control de Acceso: Arduino controla el acceso físico al cuarto (maqueta).
Registro de Accesos: Los registros de quién entra y sale se almacenan en una base de datos MySQL.


## Requisitos
### Hardware:

Arduino (cualquier modelo compatible)
Cámara compatible con OpenCV
Servomotor (para controlar la puerta de la maqueta)
Cables y protoboard

### Software:

Python 3.x
OpenCV
MySQL
Librerías de Arduino

## Uso
Ejecuta el script de Python para iniciar el reconocimiento facial.
El sistema identificará a la persona y controlará el acceso mediante el Arduino.
Los registros de acceso se almacenarán en la base de datos MySQL.
