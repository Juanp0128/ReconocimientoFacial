import cv2
import os
import numpy as np
#Genera o actualiza un archivo XML para guardar los rostros
ruta = 'C:/Users/juanp/Desktop/ReconocimientoFacial/Data'
listaPersonas = os.listdir(ruta)
print('Personas: ', listaPersonas)

classifiers = []
caritas = []
clas = 0

for nDir in listaPersonas:
    personaRuta = ruta + '/' + nDir
    print('Procesando Rostros')

    for nombreFile in os.listdir(personaRuta):
        print('Caras: ', nDir + '/' + nombreFile)
        classifiers.append(clas)
        caritas.append(cv2.imread(personaRuta+'/'+nombreFile,0))
        imagen = cv2.imread(personaRuta+'/'+nombreFile,0)

    clas = clas + 1
#Metodo Eigen
loadFaceRecognizer = cv2.face.EigenFaceRecognizer_create()
print("Procesando...")
loadFaceRecognizer.train(caritas, np.array(classifiers))

loadFaceRecognizer.write('EntrenamientoEigenn.xml')
print("Entrenamiento Exitoso, Carita Almacenada...")
