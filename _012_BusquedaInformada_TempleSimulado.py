
import random
import math

# Definimos las coordenadas de las ciudades (puedes modificarlas según tus necesidades)
ciudades = {
    'A': (1, 0),
    'B': (1, 3),
    'C': (4, 2),
    'D': (6, 5),
    'E': (8, 1)
}

# Función para calcular la distancia entre dos ciudades
def distancia(ciudad1, ciudad2):
    x1, y1 = ciudades[ciudad1]
    x2, y2 = ciudades[ciudad2]
    return math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))

# Función para calcular la longitud total de una ruta
def longitud_ruta(ruta):
    longitud = 0
    for i in range(len(ruta) - 1):
        longitud += distancia(ruta[i], ruta[i + 1])
    longitud += distancia(ruta[-1], ruta[0])  # Regreso al punto de partida
    return longitud

# Algoritmo de Temple Simulado
def temple_simulado(ruta_inicial, temperatura_inicial, iteraciones):
    mejor_ruta = ruta_inicial
    mejor_longitud = longitud_ruta(mejor_ruta)
    temperatura_actual = temperatura_inicial

    for _ in range(iteraciones):
        ciudad1, ciudad2 = random.sample(mejor_ruta, 2)
        nueva_ruta = mejor_ruta.copy()
        nueva_ruta[nueva_ruta.index(ciudad1)], nueva_ruta[nueva_ruta.index(ciudad2)] = ciudad2, ciudad1
        nueva_longitud = longitud_ruta(nueva_ruta)

        if nueva_longitud < mejor_longitud or random.random() < math.exp((mejor_longitud - nueva_longitud) / temperatura_actual):
            mejor_ruta = nueva_ruta
            mejor_longitud = nueva_longitud

        temperatura_actual *= 0.995  # Enfriamiento gradual

    return mejor_ruta, mejor_longitud

# Parámetros
ruta_inicial = ['A', 'B', 'C', 'D', 'E']
temperatura_inicial = 100
iteraciones = 10000

# Ejecutamos el algoritmo
ruta_optima, longitud_optima = temple_simulado(ruta_inicial, temperatura_inicial, iteraciones)

print("Ruta optima:", ruta_optima)
print("Longitud optima:", longitud_optima)