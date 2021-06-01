import cv2
import os
#Compara lo aprendido mediante el XML con Video/streaming y determina si lo reconoce o no
#Es necesario un entrenamiento con imagenes diversas de el personaje para mayor efectividad
ruta = 'C:/Users/juanp/Desktop/ReconocimientoFacial/Data'
listaPersonas = os.listdir(ruta)
print('Personas: ', listaPersonas)
#Metodo Eigen
loadFaceRecognizer = cv2.face.EigenFaceRecognizer_create()

Axml = 'C:/Users/juanp/PycharmProjects/IdentidicadorRostros/Machinevision/EntrenamientoEigenn.xml'
loadFaceRecognizer.read(Axml)

#Webcam
#cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#Video Luisito, persona que RECONOCE porque fue entrenado
cam = cv2.VideoCapture('C:/Users/juanp/Desktop/ReconocimientoFacial/luisc.mp4')

#Video Auronplay, Persona que RECONOCE porque fue entrenado
#cam = cv2.VideoCapture('C:/Users/juanp/Desktop/ReconocimientoFacial/auronplay1.mp4')

#Video de Mujer, Persona que DESCONOCE
#cam = cv2.VideoCapture('C:/Users/juanp/Desktop/ReconocimientoFacial/mujer.mp4')

entrenamiento = 'haarcascade_frontalface_default.xml'
cap = cv2.CascadeClassifier(entrenamiento)

while True:
    #Configuraciones esteticas de el cuadro, porcentajes de reconocimiento y nombre
    capture,frame = cam.read()
    if capture == False: break
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gris.copy()

    caritas = cap.detectMultiScale(gris,1.3,5)

    for (x,y,w,h) in caritas:
        cara = auxFrame[y:y+h,x:x+w]
        cara = cv2.resize(cara,(150,150),interpolation= cv2.INTER_CUBIC)
        resultado = loadFaceRecognizer.predict(cara)

        cv2.putText(frame,'{}'.format(resultado),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)


        if resultado[1] < 5700:
            cv2.putText(frame, '{}'.format(listaPersonas[resultado[0]]), (x, y - 25), 2, 1.1, (0, 255, 0), 1, cv2.LINE_AA)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        else:
            cv2.putText(frame, 'Quien sos?', (x, y - 20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)



    cv2.imshow('frame',frame)
    j = cv2.waitKey(1)
    if j == 27:
        break

cam.release()
cv2.destroyAllWindows()


