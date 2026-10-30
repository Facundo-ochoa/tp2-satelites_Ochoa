import json
from funciones_base import obtener_posicion
from satelite import Satelite

def cargar_json(ruta_json):
    with open(ruta_json, "r") as archivo:
        datos = json.load(archivo)

    return datos


def crear_catalogo(datos):
    satelites=[]
    for dato in datos:
        latitud, longitud, altitud = obtener_posicion(dato)
        nombre= dato["OBJECT_NAME"]
        N_catalogo=dato["NORAD_CAT_ID"]
        
        try:
            satelite = Satelite(nombre, N_catalogo, latitud, longitud, altitud)
            satelites.append(satelite)
        except ValueError:
            continue

    return satelites


def agrupar_satelites(satelites):
     
     grupos = {
        "LEO": [],
        "MEO": [],
        "GEO": [],
        "HEO": []
     }

     for satelite in satelites:
        tipo = satelite.altura()
        grupos[tipo].append(satelite.altitud)

     resumen = {}

     for clave, valores in grupos.items():
        cantidad = len(valores)

        if cantidad > 0:
            minimo = min(valores)
            maximo = max(valores)
            promedio = sum(valores) / cantidad
        else:
            minimo = None
            maximo = None
            promedio = None

        resumen[clave] = {
            "cantidad": cantidad,
            "minimo": minimo,
            "maximo": maximo,
            "promedio": promedio
        }

     return resumen

def satelites_zona(satelites, longitud_min, latitud_min, longitud_max, latitud_max):
    encontrados = []

    for satelite in satelites:
        if satelite.zonas(longitud_min, latitud_min, longitud_max, latitud_max):
            encontrados.append(satelite)

    return encontrados

