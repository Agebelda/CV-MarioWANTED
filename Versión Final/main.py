import cv2 as cv
import numpy as np
import time
import pyautogui
from matplotlib import pyplot as plt

from image import *

refreshRate = 2 # Frecuencia con la que vamos a buscar las imagenesw
characterMatch = None # Personaje que hay que buscar
prvsCharacterMatch = None # Personaje que se buscaba anteriormente
characterMatchCounter = 0 # Variable temporal

def Search():
    global characterMatch, prvsCharacterMatch, characterMatchCounter

    # Realizar captura de pantalla a las dos screens
    mainScreen = getScreenshot()
    subScreen = getScreenshot(mainScreen=False)

    mainScreen.save("mainScreen.png")
    subScreen.save("subScreen.png")

    foundCharacter = None

    # Busqueda para encontrar al personaje wanted 
    for character in Character:
        try:
            # Utilizamos la función locate de pyautogui que busca una imagen dentro de otra
            characterWanted = pyautogui.locate(characterTextures[character.value], mainScreen, confidence=0.85)

            if characterWanted is not None:
                # Si se encontró el personaje
                foundCharacter = character
                # Se guarda el nombre
                characterName = foundCharacter.name
                characterMatchCounter += 60 / refreshRate
                break

        except pyautogui.ImageNotFoundException: 
            # Si no se encontró la imagen actual, intenta con la siguiente
            continue
    
    if foundCharacter is None or prvsCharacterMatch != characterMatch:
        # Si no se encontró ponemos variable temporal a 0 para no empezar a buscar aún
        characterMatchCounter = 0
        characterMatch = None
    else:
        # Empezar la busqueda después de un seg
        if characterMatchCounter >= 60:
            characterMatch = foundCharacter

    prvsCharacterMatch = characterMatch

    if characterMatch is not None:
        # Realizamos la busqueda del personaje wanted en la subScreen
        position = matchfind(characterName)

        # Si se encontró el icono se presiona
        if position and len(position) == 1:  # Asegúrate de que position tenga exactamente una tupla
            x, y = position[0]  # Extrae las coordenadas de la tupla
            pyautogui.moveTo(x, y)
            pyautogui.drag(0.0, 1.0, 0.15)
            

def matchfind(characterName):

    icon = cv.imread("assets/"+characterName+"Icon.png", cv.IMREAD_GRAYSCALE)
    map = cv.imread("subScreen.png", cv.IMREAD_GRAYSCALE)

    # Comprobamos que se han podido leer
    if icon is None or map is None:
        print('Error al cargar la imagen')
        exit()

    coordinates = keypointSearcher(icon, map)

    if coordinates:
        return coordinates

    else:
        icon = cv.imread("assets/"+characterName+".png", cv.IMREAD_GRAYSCALE)
        map = cv.imread("subScreen.png", cv.IMREAD_GRAYSCALE)

        # Comprobamos que se han podido leer
        if icon is None or map is None:
            print('Error al cargar la imagen')
            exit()

        coordinates = keypointSearcher(icon, map)

        if coordinates:
            return coordinates

        else:
            try:
                # Utilizamos la función locate de pyautogui que busca una imagen dentro de otra
                characterWanted = pyautogui.locate(icon, map, confidence=0.85)

                if characterWanted is not None:
                    return characterWanted

            except pyautogui.ImageNotFoundException: 
                return None
                # Si no se encontró la imagen actual, intenta con la siguiente

def keypointSearcher(icon, map2):
    # Crear el descriptor SIFT con parámetros ajustados
    sift = cv.SIFT_create()

    # Usar SIFT para detectar los keypoints y calcular sus descriptores
    keypoints1, descriptors1 = sift.detectAndCompute(icon, None)
    keypoints2, descriptors2 = sift.detectAndCompute(map2, None)

    if descriptors2 is None:
        return None

    # Convertir los descriptores a tipo np.float32 Quito esto?
    descriptors1 = descriptors1.astype(np.float32)
    descriptors2 = descriptors2.astype(np.float32)

    # Crear el objeto de coincidencia BFMatcher
    matcher = cv.BFMatcher(cv.NORM_L1)

    # Realizar la coincidencia
    matches = matcher.knnMatch(descriptors1, descriptors2, k=2)

    # Filtrar las coincidencias usando ratio test
    good = list()
    for m, n in matches:
        if m.distance < 0.65 * n.distance:
            good.append(m)

    # Obtener las coordenadas de los keypoints correspondientes a los matches buenos
    keypoints_sift_coords= np.float32([keypoints2[m.trainIdx].pt for m in good])

    # Filtrar keypoints cercanos
    grouped_keypoints = []
    for kp in keypoints_sift_coords:
        added_to_group = False
        for group in grouped_keypoints:
            for existing_point in group:
                distance = np.linalg.norm(np.array(existing_point) - np.array(kp))
                if distance < 20:
                    group.append(kp)
                    added_to_group = True
                    break
            if added_to_group:
                break
        if not added_to_group:
            grouped_keypoints.append([kp])

    # Seleccionar el grupo con el mayor número de keypoints
    selected_group = max(grouped_keypoints, key=len, default=[])

    if selected_group:
        # Obtener las coordenadas del primer punto en el grupo
        first_keypoint = selected_group[0]

        # Ahora puedes acceder a las coordenadas x e y por separado
        adjusted_coordinates = [(int(first_keypoint[0]) * properties.subScreenScale + properties.subScreen[0], 
                                 int(first_keypoint[1]) * properties.subScreenScale + properties.subScreen[1])]
        return adjusted_coordinates
    else:
        return None


if __name__ == "__main__":
    try:
        loadCharacterTextures()
    except Exception as exception:
        print(exception)
        exit()

    # Mensaje emergente para iniciar el programa
    if pyautogui.confirm(
        "Mario Wanted Minigame Image Recognition",
        title="Wanted Minigame", buttons=["Start", "Cancel"]
    ) == "Cancel":
        exit()

    applicationClosed = False

    while not applicationClosed:

        Search()
        time.sleep(1.0 / refreshRate)

        # Para salir de la ejecucion del programa arrastrar el ratón a la esquina superior izquierda 
        mousex, mousey = pyautogui.position()
        applicationClosed = mousex + mousey == 0