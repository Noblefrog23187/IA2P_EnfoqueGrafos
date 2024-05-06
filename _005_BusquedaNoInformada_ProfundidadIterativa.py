
def busq_prof_iterativa(grafo, inicio, objetivo):
    
    def busq_prof_lim(grafo, inicio, objetivo, limite_profundidad):
        visitados = set()
        stack = [(inicio, [inicio])]  # Inicializar la pila con el nodo de inicio y su camino

        while stack:
            nodo, camino = stack.pop()  # Extraer el nodo actual y su camino desde la pila
            if nodo not in visitados:
                visitados.add(nodo)  # Marcar el nodo como visitado
                if nodo == objetivo:
                    return camino  # Devolver el camino si se encuentra el objetivo
                if len(camino) <= limite_profundidad:  # Verificar si se ha alcanzado el límite de profundidad
                    # Extender la pila con los vecinos del nodo actual y sus respectivos caminos
                    for vecino in grafo[nodo]:
                        stack.append((vecino, camino + [vecino]))

        return None  # Devolver None si no se encuentra un camino dentro del límite de profundidad

    # Iterar sobre los límites de profundidad crecientes
    for limite_profundidad in range(len(grafo)):
        resultado = busq_prof_lim(grafo, inicio, objetivo, limite_profundidad)  # Llamar a la búsqueda en profundidad limitada
        if resultado:
            return resultado  # Devolver el camino si se encuentra uno dentro del límite de profundidad

    return "No se encontro un camino"  # Devolver un mensaje si no se encuentra ningún camino

grafo = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E', 'I'],
         'G': ['H', 'I'],
         'H': ['G', 'J'],
         'I': ['G', 'K'],
         'J': ['H'],
         'K': ['I']}

inicio = 'A'
objetivo = 'H'
print("Camino encontrado por Busqueda en Profundidad Iterativa:", busq_prof_iterativa(grafo, inicio, objetivo))