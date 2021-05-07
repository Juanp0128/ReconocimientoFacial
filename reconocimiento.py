import cv2
import entrenar

imagen_duque = entrenar.load_image_file("duque1c.jpg")
imagen_trump = entrenar.load_image_file("trump1.jpg")



einstein_encodings = entrenar.face_encodings(imagen_duque)[0]
paul_encodings = entrenar.face_encodings(imagen_trump)[0]


encodings_conocidos = [
    einstein_encodings,
    paul_encodings,
]
nombres_conocidos = [
    "Duque",
    "Trump",
]
font = cv2.FONT_HERSHEY_COMPLEX

img = entrenar.load_image_file('caras.jpg')

loc_rostros = []
encodings_rostros = []
nombres_rostros = []

loc_rostros = entrenar.face_locations(img)
encodings_rostros = entrenar.face_encodings(img, loc_rostros)

for encoding in encodings_rostros:


    coincidencias = entrenar.compare_faces(encodings_conocidos, encoding)

    if True in coincidencias:
        nombre = nombres_conocidos[coincidencias.index(True)]

    else:
        nombre = "???"

    nombres_rostros.append(nombre)

for (top, right, bottom, left), nombre in zip(loc_rostros, nombres_rostros):

    if nombre != "???":
        color = (0, 255, 0)  # Verde
    else:
        color = (0, 0, 255)  # Rojo

    cv2.rectangle(img, (left, top), (right, bottom), color, 2)
    cv2.rectangle(img, (left, bottom - 20), (right, bottom), color, -1)
    cv2.putText(img, nombre, (left, bottom - 6), font, 0.6, (0, 0, 0), 1)

cv2.imshow('Output', img)
print("\nResultado!! ESC para salir\n")
cv2.waitKey(0)
cv2.destroyAllWindows()
