class Satelite:
    def __init__(self,nombre,N_catalogo,latitud,longitud,altitud):
        if nombre.strip():
            self.nombre= nombre
        else:
            raise ValueError ("El nombre no puede estar vacio")

        if type(N_catalogo) == int:
            self.N_catalogo=N_catalogo
        else:
            raise ValueError ("El numero de catalogo debe ser un numero entero")

        if -90<=latitud<=90:
            self.latitud=latitud
        else:
            raise ValueError ("La latitud debe ser mayor a -90 y menor a 90 inclusive")

        if -180<=longitud<=180:
            self.longitud=longitud
        else:
            raise ValueError ("La longitud debe ser mayor a -180 y menor a 180 inclusive")

        if altitud>=100:
            self.altitud=altitud
        else:
            raise ValueError ("La altitud debe ser minimamente 100km inclusive")

    def altura(self):
        if self.altitud<2000:
            return "LEO"
        
        elif 2000<=self.altitud<34000:
            return "MEO"

        elif 34000<=self.altitud<=37000:
            return "GEO"
        
        else:
            return "HEO"

        
    def informacion(self):
        altura=self.altura()
        return f"{self.nombre} | {self.N_catalogo} | {altura} | {self.altitud} km."
    

    def zonas(self, longitud_min, latitud_min, longitud_max, latitud_max):
        if longitud_min<=self.longitud<=longitud_max and latitud_min<=self.latitud<=latitud_max:
            return True
        return False
