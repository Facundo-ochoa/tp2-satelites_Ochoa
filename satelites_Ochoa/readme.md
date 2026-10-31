Función:
---
El actual conjunto de archivos se encargara de procesar un archivo JSON proveniente de CelesTrak el cual contendrá información de los distintos satélites que se encuentran rondando de manera activa. 
El trabajo se dividirá en 3 partes que trabajarn en cojunto.

Primera parte: La etapa 1 será la encargada de obtener los datos extraídos del JSON, para esto se creara una clase denominada "Satelite", para luego clasificarlos según su altura y ubicación.

Segunda parte: La etapa 2 será la encarga de utilizar todas las funciones de clasificación creadas anteriormente y utilizarla de manera cojunta.
También será la encargada de interactuar con el usuario permitiéndole elegir que desea saber con respecto a los satelites.

Tercera parte: La ultima etapa se encargara de verificar todas las líneas de código que se ultimaron anteriormente y verificar que cumplan de una manera adecuada. 

instalacion:
---
Para su utilización se necesitara:
- Tener instalado python3
- instalar 3 librerías externas ("skyfield","pytest","pytest-cov"), y se utilizar algunas librerías internas como ("json", "sys","datetime").

Requirements.txt 
---
Para obtener dichas librería, vamos a descargar el contenido que se encuentra dentro del archivo "requirements.txt".
Para esto nos centraremos en la carpeta "satélites" y escribiremos:

python -m pip install -r requirements.txt

Orden de archivos
---
para el correcto funcionamiento se tendra que disponer el siguiente orden en las carpetas:
```
satelites/
│
├── datos/
│   └── satelites.json
│
├── .gitignore
├── catalogo.py
├── consultar_satelites.py
├── funciones_base.py
├── satelite.py
├── test_catalogo.py
├── test_satelite.py
├── README.md
└── requirements.txt
```

Proceso de Ejecucion por consola:
---

Para ejecutar las indicaciones tenemos 3 opciones, la cuales colocaran en la consola al previamente ubicarnos en la carpeta "satelites":

En caso de querer ejecutar la opciones "resumen" , la cual nos mostrara un resumen de las estadísticas de los diversos satelites:

"python consultar_satelites.py datos/satelites.json resumen"

En caso de seleccionar la opcion zona, la cual nos permitira consultar los satelites en una zona deliberada.
Para esto tendremos que elegir las cordenadas con el siguiente orden "longitud mínima, latitud mínima, longitud máxima y latitud máxima"

ej: 
"python consultar_satelites.py datos/satelites.json zona -76.30 -46.13 -66.30 -36.13"

Por ultimo en caso de querer verificar las coberturas de seguridad ejecutadas a los archivos tenemos 2 opciones:

pruebas unitaria (comprobación de pruebas en el archivo):
"python -m pytest -v"

cobertura general (comprobación de coberturas posibles):
"python -m pytest --cov=satelite --cov=catalogo --cov-report=term-missing"

Archivo de entrada (json):
---
El archivo de entrada será proveniente del sitio CelesTrak, y contara con una lista de diccionarios, cada uno ofreciendo información de un satélite. 
El mismo contara con el siguiente formato 

```
{
    "OBJECT_NAME": "ISS (ZARYA)",
    "OBJECT_ID": "1998-067A",
    "EPOCH": "2026-10-14T08:06:39.057984",
    "MEAN_MOTION": 15.48861773,
    "ECCENTRICITY": 0.00067245,
    "INCLINATION": 51.6325,
    ...
    "NORAD_CAT_ID": 25544,
    ...
}
```

Primera etapa
---

funciones_base.py
---
Este archivo proporcionado por el profesor, utilizara las librerías "datetime" y "skyfield.api", para obtener la ubicación de los satélites en un momento preciso.

Con esto creara una función que nos devolverá la latitud, longitud y altitud en formato float.

satelite.py
---

Este archivo será el encargado de crear la clase "Satelite", que contara con 5 atributos., siendo estos: nombre, numero de catalogo, latitud, longitud, altitud

Los mismos se verificaran mediante validaciones para ser condiciones razonables.

Por ultimo se crearon 3 métodos para clasificar, comprobar y  mostrar de manera ordenada los distintos satelites.

catalogo.py
---
Este contara con la tarea de crear las diversas funciones que se utilizaran.

Las primeras se encargaran de analizar el json y convertirlo en un elemento con el que Python pueda interactuar, y convertirlos en objetos "Satelite"

Posteriormente se creara una función para agrupar los satélites según su altura, filtrar satélites según una zona geográfica, y mostrar información especifica de cada grupo. Un ejemplo seria la altura máxima. 

consultar_satelites.py
---
Este archivo será el encargado de invocar las funciones creadas anteriormente, e interactuar con el usuario mediante la librería "sys".

test_satelite.py y test_catalogo.py
---

Estos 2 archivos utilizaran la librería "pytest" para crear diversas funcione de verificación para su respectivo archivo. 

Los mismos bucarán cubrir la mayor cantidad errores posibles y verificar que las funciones anteriores cumplan con su objetivo al dar un ejemplo de uso y al resultado esperado.

resultado
--- 
Después de ejecutar el comando 
"python -m pytest --cov=satelite --cov=catalogo --cov-report=term-missing"

se obtuvo una cobertura total del 93%
con catalogo.py obteniendo un 93% y satelite.py un 94%.
