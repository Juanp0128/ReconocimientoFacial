from visionrostros import *
import cv2
import sys


# Valores de entrada
rutaImagen = sys.argv[1]
imagenAnalizar = cv2.imread(rutaImagen)

[dataRostros, imagenesRostros] = detectarRostros(imagenAnalizar)

#verSubRostros(imagenesRostros)
crearRostros(imagenAnalizar, dataRostros)#
verRostosImagen(imagenAnalizar, dataRostros)
