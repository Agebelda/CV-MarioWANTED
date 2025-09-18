from os.path import exists
from character import *

class Properties(object):
    def __init__(self):
        # Definimos las propiedades de las pantallas del emulador
        self.mainScreen = [0, 333, 1080, 810]
        self.mainScreenScale = 4.25
        self.subScreen = [1080, 333, 1080, 810]
        self.subScreenScale = 4.0