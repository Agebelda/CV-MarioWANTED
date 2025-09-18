import cv2
import numpy as np
import random
import os


# Crear un fondo nuevo

fondo = cv2.imread('fondo.png')
output_folder = 'mapas'
#h y w de fondo
hf,wf,_=fondo.shape



# Cargar las tres imágenes
M= cv2.imread('Mario_nf.png')
Y = cv2.imread('Yoshi_nf.png')
W= cv2.imread('Wario_nf.png')
L=cv2.imread('Luigi_nf.png')

list=[M, Y, W, L]
#h y w de las imagenes 
h,w,_=M.shape

# Número de imágenes a generar
num_images = 20
for img_num in range(num_images):
    buscado= random.randint(0, 3)

    wanted=list[buscado]
    idx=1
    for u in range(4):
        if u!=buscado:
            if idx==1:
                imagen1=list[u]
                idx=idx+1
                
            elif idx==2:
                imagen2=list[u]
                idx=idx+1
                
            elif idx==3:
                imagen3=list[u]
                idx=1
    # Lista de imágenes y posiciones
    imagenes = [imagen1, imagen2, imagen3]
    posiciones = []
    index=0
    wanted_pos=0
    
    for i in range(0,hf,h):
        for j in range(0,wf,w):
            a=(i,j)
            posiciones.insert(0,a)


            

    # Mezclar aleatoriamente las imágenes y posiciones
    # Cambiar la semilla aleatoria en cada ejecución
    random_seed = random.randint(1, 1000)
    random.seed(random_seed)
    random.shuffle(posiciones)

    
    # Colocar las imágenes en el fondo en posiciones aleatorias
    for i in range(len(posiciones)):
        x, y = posiciones[i]
        index= random.randint(0, 2)
        fondo[y:y + h, x:x + w] = imagenes[index]

    
    #se añade la imagen extra a buscar
    wanted_pos=random.randint(0, len(posiciones)-1)
    x, y = posiciones[wanted_pos]
    fondo[y:y + h, x:x + w] = wanted


    # Guardar el resultado como una nueva imagen en la carpeta de salida
    output_path = os.path.join(output_folder, f'mapa_{img_num + 1}.png')
    cv2.imwrite(output_path, fondo)


