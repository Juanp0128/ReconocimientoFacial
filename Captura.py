from cv2 import cv2
import os
import imutils
#Crea una carpeta o la actualiza mientras captura rostros en tiempo real, sea mediante un video o webcam
persona1 = 'Auronplay' #El nombre de la persona que sera creada
ruta = 'C:/Users/juanp/Desktop/ReconocimientoFacial/Data'
rutaPersona = ruta + '/' + persona1

if not os.path.exists(rutaPersona):
    print('Persona Creada: ', rutaPersona)
    os.makedirs(rutaPersona)

#Captura por WebCam
#cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#Captura por Video
cam = cv2.VideoCapture('C:/Users/juanp/Desktop/ReconocimientoFacial/auronplay1.mp4')

entrenamiento = 'haarcascade_frontalface_default.xml'
cap = cv2.CascadeClassifier(entrenamiento)
count = 0

while True:
    capture, frame = cam.read()
    if capture == False: break
    frame = imutils.resize(frame, width=640)
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = frame.copy()

    rostros = cap.detectMultiScale(gris,1.3,5)

    for(x,y,w,h) in rostros:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        carita = auxFrame[y:y+h,x:x+w]
        carita = cv2.resize(carita,(150,150),interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(rutaPersona + '/cara{}.jpg'.format(count),carita)
        count = count + 1
        print('Rostro Creado!!')
    cv2.imshow('frame',frame)
#Crea 300 archivos JPG con los rostros capturados
    j = cv2.waitKey(1)
    if j == 27 or count >= 350:
        break

cam.release()
cv2.destroyAllWindows()
