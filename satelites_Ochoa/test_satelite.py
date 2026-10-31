from satelite import Satelite
import pytest


#test satelite

def test_satelite():
    sat = Satelite("ISS", 25544, -41.1, -71.3, 419.7)

    assert sat.nombre == "ISS"
    assert sat.N_catalogo == 25544
    assert sat.latitud == -41.1
    assert sat.longitud == -71.3
    assert sat.altitud == 419.7

def test_vacio():
    with pytest.raises(ValueError):
        Satelite("", 25544, 0, 0, 400)

def test_espacios():
    with pytest.raises(ValueError):
        Satelite("   ", 25544, 0, 0, 400)

def test_no_numero():
    with pytest.raises(ValueError):
        Satelite("ISS", "30000", 19, 32, 400)

def test_altitud_minima():
    sat = Satelite("ISS", 25544, 0, 0, 100)
    assert sat.altitud == 100

#test orbitas
def test_orbita_leo():
    sat = Satelite("ISS", 25544, -41.1, -71.3, 1999)
    assert sat.altura() == "LEO"


def test_orbita_MEO():
    sat = Satelite("ISS", 25544, -41.1, -71.3, 2000)
    assert sat.altura() == "MEO"

def test_orbita_MEO2():
    sat = Satelite("ISS", 25544, -41.1, -71.3, 33999)
    assert sat.altura() == "MEO"


def test_orbita_GEO():
    sat = Satelite("ISS", 25544, -41.1, -71.3, 36999)
    assert sat.altura() == "GEO"

def test_orbita_GEO2():
    sat = Satelite("ISS", 25544, -41.1, -71.3, 37000)
    assert sat.altura() == "GEO"

def test_orbita_GEO3():
    sat = Satelite("ISS", 25544, -41.1, -71.3, 34000)
    assert sat.altura() == "GEO"


def test_orbita_HEO():
    sat = Satelite("ISS", 25544, -41.1, -71.3, 37001)
    assert sat.altura() == "HEO"

def test_altitud_invalida():
    with pytest.raises(ValueError):
        Satelite("ISS", 25544, -41.1, -71.3, 50)


#test informacion

def test_informacion():
    sat = Satelite("ISS", 25544, -41.1, -71.3, 419.7)
    informacion = sat.informacion()

    assert informacion == "ISS | 25544 | LEO | 419.7 km."


#test zona


def test_zona_dentro():
    sat = Satelite("ISS", 25544, -41.1, -71.3, 419.7)
    assert sat.zonas(-76.30, -46.13, -66.30, -36.13) == True


def test_zona_fuera():
    sat = Satelite("ISS", 25544, 30, 50, 419.7)
    assert sat.zonas(-76.30, -46.13, -66.30, -36.13) == False


def test_zona_borde():
    sat = Satelite("ISS", 25544, -46.13, -76.30, 419.7)
    assert sat.zonas(-76.30, -46.13, -66.30, -36.13) == True