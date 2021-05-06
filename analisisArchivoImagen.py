from visionrostros import *
from reconocimiento import *
import cv2
import sys

def procesarImagen(rutaImagen):
    imagenAnalizar = cv2.imread(rutaImagen)
    [dataRostros, imagenesRostros] = detectarRostros(imagenAnalizar)

    print(type)

    crearRostros(imagenAnalizar,dataRostros)
    verRostosImagen(imagenAnalizar,dataRostros)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        rutaImagen = sys.argv[1]
    else:
        rutaImagen = "C:\Users\juanp\PycharmProjects\IdentificadorRostros\imagenesApoyo\caras.jpg"
    procesarImagen(rutaImagen)
