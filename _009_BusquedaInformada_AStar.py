
def ao_estrella(grafo, inicio, objetivo):
    visitados = set() # Conjunto para almacenar los nodos visitados
    frontera = [(inicio, [inicio], 0)] # Lista de prioridad para almacenar los nodos, el camino seguido hasta el momento y sus costos

    while frontera:
        # Seleccionamos el nodo de la frontera con el menor costo estimado
        nodo_actual, camino_actual, costo_actual = min(frontera, key=lambda x: x[2])
        frontera.remove((nodo_actual, camino_actual, costo_actual))
        
        if nodo_actual == objetivo:
            print("Objetivo alcanzado:", nodo_actual)
            print("Camino seguido:", " -> ".join(camino_actual))
            return True
        
        visitados.add(nodo_actual)
        # Expandimos el nodo actual y añadimos los nodos vecinos a la frontera
        for vecino, costo in grafo[nodo_actual]:
            if vecino not in visitados:
                nuevo_camino = camino_actual + [vecino]
                nuevo_costo = costo_actual + costo
                frontera.append((vecino, nuevo_camino, nuevo_costo))
    print("No se encontro el objetivo.")
    return False

grafo = {
    'A': [('B', 7), ('C', 5), ('D', 8)],
    'B': [('E', 4), ('F', 6), ('G', 3)],
    'C': [('G', 3)],
    'D': [('H', 2), ('I', 5)],
    'E': [('J', 9)],
    'F': [('K', 3), ('L', 4)],
    'G': [('M', 7)],
    'H': [('N', 1)],
    'I': [('N', 8)],
    'J': [],
    'K': [],
    'L': [],
    'M': [],
    'N': []
}

# Llamamos a la función de búsqueda con el nodo de inicio 'A' y el nodo objetivo 'N'
ao_estrella(grafo, 'A', 'N')