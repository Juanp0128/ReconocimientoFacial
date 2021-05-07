
import PySimpleGUI as gui
import os.path
import PIL.Image
import io
import base64

from loadFaceSegmentation import *


def convert2bytes(imagen, resize=None):
    cv2.imwrite(f'ROI_X.png', imagen)
    img = PIL.Image.open('ROI_X.png')

    cur_width, cur_height = img.size
    if resize:
        new_width, new_height = resize
        scale = min(new_height / cur_height, new_width / cur_width)
        img = img.resize((int(cur_width * scale), int(cur_height * scale)), PIL.Image.ANTIALIAS)
    bio = io.BytesIO()
    img.save(bio, format="PNG")
    del img
    return bio.getvalue()


def crearPlantillaGUI():
    # ---[Define la ventana]---------------------------------------------------------------
    ventana = [[gui.Text('Folder'), gui.In(size=(25, 1), enable_events=True, key='-FOLDER-'), gui.FolderBrowse()],
               [gui.Button('Anterior', key='-ANT-'), gui.Image(key='-IMAGE-'), gui.Button('Siguiente', key='-SIG-')],
               [gui.Button('Guardar', key='-ANT2-'), gui.In(size=(25, 1), key='-NOMBRE-'),
                gui.Button('Aprender', key='-APRENDER-')]
               ]
    return ventana


def guiEntrenamientoSupervisado():
    # --------------------------------- Create Window ---------------------------------
    window = gui.Window('Entrenador', crearPlantillaGUI(), resizable=True)

    # ----- Run the Event Loop -----
    # --------------------------------- Event Loop ---------------------------------
    folder = '/'
    # fnames = []
    imagenes = []
    i = 0
    while True:
        event, values = window.read()
        if event in (gui.WIN_CLOSED, 'Exit'):
            break
        if event == gui.WIN_CLOSED or event == 'Exit':
            break

        if event == '-FOLDER-':
            folder = values['-FOLDER-']
            imagenes = listaImagenes(folder)

        if event == '-SIG-':
            try:
                if i < len(imagenes) - 1:
                    i = i + 1
                else:
                    print('No hay más elementos')

                window['-IMAGE-'].update(data=convert2bytes(imagenes[i], resize=(200, 200)))
                print(imagenes[i])
            except Exception as E:
                print(f'** Error {E} **')
                pass

        if event == '-ANT-':
            try:
                if i > 0:
                    i = i - 1
                else:
                    print('No hay más elementos')

                window['-IMAGE-'].update(data=convert2bytes(imagenes[i], resize=(200, 200)))
            except Exception as E:
                print(f'** Error {E} **')
                pass

    # --------------------------------- Close & Exit ---------------------------------
    window.close()


if __name__ == '__main__':
    guiEntrenamientoSupervisado()
