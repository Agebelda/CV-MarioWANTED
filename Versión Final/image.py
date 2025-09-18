import pyautogui
from PIL import Image

from properties import *

characterTextures = []

def loadCharacterTextures():
    for character in Character:
        # Cargamos en una lista la dirección de los assets
        characterTextures.append(f"assets/{character.name}.png") 

properties = Properties() 

def getScreenshot(mainScreen=True) -> Image:
    # Realizamos una captura de pantalla de la mainScreen o de la subScreen dependiendo de los parametros
    screenshot = pyautogui.screenshot(region=properties.mainScreen if mainScreen else properties.subScreen)
    size = screenshot.size
    scale = properties.mainScreenScale if mainScreen else properties.subScreenScale
    # Escalamos la imagen para cuadrarla con el tamaño del asset de los iconos 
    screenshot = screenshot.resize( ( int(size[0] / scale), int(size[1] / scale) ), Image.NEAREST)
    return screenshot