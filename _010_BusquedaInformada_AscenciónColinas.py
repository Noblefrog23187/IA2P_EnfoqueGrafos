
class Grafo:
    def __init__(self, grafo_dict):
        self.grafo_dict = grafo_dict

    def obtener_vecinos(self, nodo):
        #Obtiene los vecinos de un nodo en el grafo.
        return self.grafo_dict.get(nodo, [])

# Función heurística (en este caso, simplemente devuelve la distancia entre dos nodos)
def heuristica(nodo, objetivo):
   #Calcula la heurística (distancia) entre un nodo y el objetivo.
    return abs(nodo - objetivo)

# Implementación del algoritmo Hill Climbing
def busqueda_hill_climbing(grafo, inicio, objetivo):
    #Realiza la búsqueda Hill Climbing en el grafo.
    nodo_actual = inicio
    visitados = [nodo_actual]  # Lista para rastrear el camino tomado

    while nodo_actual != objetivo:
        vecinos = grafo.obtener_vecinos(nodo_actual)
        if not vecinos:
            # No hay vecinos, no se puede continuar
            return None, visitados  

        # Seleccionar el mejor vecino (el más cercano al objetivo)
        mejor_vecino = min(vecinos, key=lambda x: heuristica(x, objetivo))
        if heuristica(mejor_vecino, objetivo) >= heuristica(nodo_actual, objetivo):
            # No hay mejora, se detiene la búsqueda
            return None, visitados  
        else:
            # Avanzar al mejor vecino y registrar en el camino
            nodo_actual = mejor_vecino
            visitados.append(nodo_actual)

    return nodo_actual, visitados

# Ejemplo de uso
if __name__ == "__main__":
    # Definir el grafo
    grafo_dict = {
        1: [2, 3],
        2: [4],
        3: [5],
        4: [6],
        5: [6],
        6: []
    }

    grafo = Grafo(grafo_dict)
    nodo_inicio = 1
    nodo_objetivo = 6

    resultado, camino = busqueda_hill_climbing(grafo, nodo_inicio, nodo_objetivo)
    if resultado:
        print("Camino encontrado:", camino)
    else:
        print("No se encontro un camino desde el nodo inicial al nodo objetivo.")
