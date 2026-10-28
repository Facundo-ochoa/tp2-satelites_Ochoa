class Satelite:
    def _init_(self,nombre,N_catalogo,latitud,longitud,altitud):
        if nombre.strip():
            self.nombre= nombre
        else:
            raise ValueError ("El nombre no puede estar vacioc")

        if type(N_catalogo) == int:
            self.N_catalogo=N_catalogo
        else:
            raise ValueError ("El numero de catalogo debe ser un numero entero")

        if -90<=latitud<=90:
            self.latitud=latitud
        else:
            raise ValueError ("La latitud debe ser mayor a -90 y menor a 90")

        if -180<=longitud<=180:
            self.longitud=longitud
        else:
            raise ValueError ("La longuitud debe ser mayor a -180 y menor a 180")

        if altitud>=100:
            self.altitud=altitud
        else:
            raise ValueError ("La altitud debe ser minimamente 100km")
