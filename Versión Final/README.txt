## Configuración necesaria

Para la correcta ejecución del código es necesario **ajustar los valores del archivo `properties.py`** según la resolución de tu pantalla.  
Además, el emulador debe ejecutarse en **pantalla completa**.  

Nota: si al poner la pantalla completa la imagen del juego se **duplica**, cierra la ROM desde:  
`File -> Close Rom`  
y vuelve a abrirla desde:  
`File -> Recent Rom -> (la opción que aparezca)`  

### Ejemplo de configuraciones

#### Pantalla resolución 2K
```python
self.mainScreen = [0, 333, 1080, 810] 
self.mainScreenScale = 4.25 
self.subScreen = [1080, 333, 1080, 810] 
self.subScreenScale = 4.0
```

#### Pantalla resolución FullHD
```python
self.mainScreen = [0, 199, 959, 720] 
self.mainScreenScale = 4.25 
self.subScreen = [959, 199, 959, 720] 
self.subScreenScale = 4.0
```

---

