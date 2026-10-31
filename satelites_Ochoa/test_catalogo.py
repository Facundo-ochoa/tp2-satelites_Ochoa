import pytest
from catalogo import cargar_json, crear_catalogo , agrupar_satelites, satelites_zona
from satelite import Satelite

#test json
def test_json():
    datos=cargar_json("datos/satelites.json")
    assert datos

def test_json2():
    with pytest.raises(FileNotFoundError):
        cargar_json("hola_mundo")

#test catalogo 

def test_vacio():
    datos = []
    satelites = crear_catalogo(datos)
    assert satelites == []


def test_type():
    datos = cargar_json("datos/satelites.json")
    satelites = crear_catalogo(datos)

    assert type(satelites[0]) == Satelite


#agrupacion 

def test_agrupar():
    datos = cargar_json("datos/satelites.json")
    satelites = crear_catalogo(datos)
    resumen = agrupar_satelites(satelites)

    assert len(resumen) == 4

def test_cantidad():
    datos = cargar_json("datos/satelites.json")
    satelites = crear_catalogo(datos)
    resumen = agrupar_satelites(satelites)

    total = 0

    for clave in resumen:
        total += resumen[clave]["cantidad"]

    assert total == len(satelites)

def test_claves():
    datos = cargar_json("datos/satelites.json")
    satelites = crear_catalogo(datos)
    resumen = agrupar_satelites(satelites)

    for clave in resumen:
        assert "cantidad" in resumen[clave]
        assert "minimo" in resumen[clave]
        assert "maximo" in resumen[clave]
        assert "promedio" in resumen[clave]


#test zona

def test_zona():
    satelites = [
        Satelite("ISS", 25544, -41.1, -71.3, 419.7)
    ]

    encontrados = satelites_zona(satelites, -76, -46, -66, -36)
    assert len(encontrados) == 1


def test_fuera():
    satelites = [
        Satelite("ISS", 25544, -41.1, -71.3, 419.7)
    ]

    encontrados = satelites_zona(satelites, -76, -35, -66, -25)
    assert len(encontrados) == 0


def test_zona_borde():
    satelites = [
        Satelite("ISS", 25544, -46, -76, 419.7)
    ]

    encontrados = satelites_zona(satelites, -76, -46, -66, -36)
    assert len(encontrados) == 1

def test_vacia():
    satelites = []

    encontrados = satelites_zona(satelites, -76, -46, -66, -36)
    assert encontrados == []