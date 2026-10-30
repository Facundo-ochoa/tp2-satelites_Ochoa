import sys 
from catalogo import cargar_json, crear_catalogo , agrupar_satelites, satelites_zona

if len(sys.argv) < 3:
    print("Faltan argumentos")
    sys.exit()

Ruta_Json=sys.argv[1]
solicitud=sys.argv[2]

comando=solicitud.lower()

if comando == "zona":
    if len(sys.argv) != 7:
        print("Se necesitan cuatro coordenadas")
        sys.exit()

    longitud_min= float(sys.argv[3])
    latitud_min= float(sys.argv[4])
    longitud_max= float(sys.argv[5])
    latitud_max= float(sys.argv[6])

if comando not in ("zona", "resumen"):
    print("Consulta inválida")
    sys.exit()

datos=cargar_json(Ruta_Json)
satelites=crear_catalogo(datos)

if comando == "zona":
    zona_buscada=satelites_zona(satelites,longitud_min,latitud_min,longitud_max,latitud_max)
    print(f"La zona buscada contiene {len(zona_buscada)} satélites los cuales son:")
    for satelite in zona_buscada:
        print(satelite.informacion())

elif comando == "resumen":
    estadisticas=agrupar_satelites(satelites)

    for tipo, valores in estadisticas.items():
        print(f"Órbita: {tipo}")
        print(f"Cantidad: {valores['cantidad']}")
        print(f"Mínimo: {valores['minimo']}")
        print(f"Máximo: {valores['maximo']}")
        print(f"Promedio: {valores['promedio']}")
        print("___________________________________")
