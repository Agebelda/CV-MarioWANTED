# Wanted Vision – Visión por Computador para resolver el minijuego *Wanted!*

Proyecto universitario de visión por computador para resolver el minijuego **Wanted** de *New Super Mario Bros (Nintendo DS)*.  
El objetivo es detectar en tiempo real la cara buscada dentro de un conjunto de personajes, automatizando la resolución del juego mediante técnicas de procesamiento de imágenes.

---

## Objetivos
- Detectar automáticamente la cara objetivo dentro del mapa del minijuego.
- Explorar distintas versiones de algoritmos de visión:
  - **Versión 1** → Detección básica con binarización e IoU.
  - **Versión 2** → Uso de descriptores SIFT y FLANN/BFMatcher.
  - **Versión Final** → Integración en tiempo real con emulador y control automático del ratón.
- Optimizar precisión y velocidad para alcanzar puntuaciones más altas.

---

## Tecnologías utilizadas
- ![Python](https://img.shields.io/badge/python-3.10-blue.svg)
- [OpenCV](https://opencv.org/) → Procesamiento de imágenes (SIFT, ORB, thresholding…)
- [NumPy](https://numpy.org/) → Operaciones matriciales
- [PyAutoGUI](https://pyautogui.readthedocs.io/) → Control del ratón y capturas de pantalla
- [DeSmuMe](https://desmume.org/) → Emulador de Nintendo DS

---

## Ejecución

### Versión Final
```bash
git clone https://github.com/tuusuario/wanted-vision.git
cd wanted-vision
pip install -r requirements.txt
python src/main.py
```

Antes de ejecutar:  
- Configura correctamente las coordenadas de captura en `properties.py` según tu pantalla.  
- Abre el emulador con el juego, navega hasta:  
  `Minijuegos > Un jugador > Puzzles > Wanted!`  
- Pulsa **Begin** en la ventana emergente.  

Para detener la ejecución:  
- Arrastra el ratón hacia la esquina superior izquierda de la pantalla.  
- O bien usa `CTRL + C` en la terminal/bas h.  

---

## Resultados
- **Versión 1:** Correcta detección en mapas fijos, pero lenta para escenarios complejos.  
- **Versión 2:** SIFT + BFMatcher → detecciones más rápidas y robustas, incluso con solapamientos.  
- **Versión Final:** Integración en tiempo real con PyAutoGUI, alcanzando niveles avanzados en el minijuego.  

[Ejemplo detección](https://drive.google.com/file/d/1a6yYK_s6JROzloKP87mlKnbLAB-5CZV7/view?usp=sharing)

---

## Autores
- Martín Cámara Moral  
- Adrián Gea García  
- Daniel Burgos Espinar  
- Alejandro Gea Belda

Estudiantes del Grado en Ingeniería Robótica de la Universidad de Alicante
