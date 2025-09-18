Para la correcta ejecucción del código es necesario cambiar los valores del archivo properties.py y ejecutar el 
codigo en pantalla completa si al poner la pantalla completa la imagen del juego se duplica, cerrar la rom mediante
File -> Close Rom y luego abrirla de nuevo con File -> Recent Rom -> La opcion que salga

Pantalla resolución 2K:
self.mainScreen = [0, 333, 1080, 810] 
self.mainScreenScale = 4.25 
self.subScreen = [1080, 333, 1080, 810] 
self.subScreenScale = 4.0

Pantalla resolución FullHD:
self.mainScreen = [0, 199, 959, 720] 
self.mainScreenScale = 4.25 
self.subScreen = [959, 199, 959, 720] 
self.subScreenScale = 4.0
