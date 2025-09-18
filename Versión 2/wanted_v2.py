import cv2 as cv
import numpy as np
import time
from matplotlib import pyplot as plt

# Cargamos las imágenes en escala de grises
icono = cv.imread("icono/Luigi_Icon.png", cv.IMREAD_GRAYSCALE)
testMap = cv.imread("mapas/map4_luigi.jpg", cv.IMREAD_GRAYSCALE)

# Comprobamos que se han podido leer
if icono is None or testMap is None:
    print('Error al cargar la imagen')
    quit()


# Creamos el descriptor SIFT y ORB con sus valores por defecto
sift = cv.SIFT_create()

# Usamos SIFT para detectar los keypoints y calcular sus descriptores
icono_keypoints, icono_descriptors = sift.detectAndCompute(icono, None)
testMap_keypoints, testMap_descriptors = sift.detectAndCompute(testMap, None)

# Realizar la coincidencia para descriptores SIFT
matcher_sift = cv.BFMatcher(cv.NORM_L1)

# match sift icono con sift mapa
matches_sift = matcher_sift.knnMatch(icono_descriptors, testMap_descriptors, k=2)

# Nos quedamos sólo los matches "buenos" y los guardamos en good
# En el artículo original de SIFT, si dos puntos tienen una distancia menor de 0.7 se consideran un match
good_sift = list()
for m, n in matches_sift:
    if m.distance < 0.85 * n.distance:
        good_sift.append(m)


draw_params = dict(matchColor=(0, 255, 0), singlePointColor=(255, 0, 0))

# Dibujar coincidencias para SIFT
imageMatches_sift = cv.drawMatches(icono, icono_keypoints, testMap, testMap_keypoints, good_sift, None, **draw_params)

# Mostrar ambas imágenes resultantes
plt.subplot(), plt.imshow(imageMatches_sift), plt.title('Matches SIFT')
plt.show()
