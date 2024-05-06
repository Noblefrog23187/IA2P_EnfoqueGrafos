
def busqueda_voraz(grafo, inicio, objetivo):
    visitados = set() # Conjunto para almacenar los nodos visitados
    cola = [(inicio, [inicio], 0)] # Lista de prioridad para almacenar los nodos, el camino seguido hasta el momento y sus costos

    while cola:
        nodo_actual, camino_actual, costo_actual = cola.pop(0) # Tomamos el primer elemento de la lista
        if nodo_actual == objetivo:
            print("Objetivo alcanzado:", nodo_actual)
            print("Camino seguido:", " -> ".join(camino_actual))
            return True
        if nodo_actual not in visitados:
            print("Visitando nodo:", nodo_actual)
            visitados.add(nodo_actual)
            # Agregamos los nodos vecinos, el camino y sus costos a la cola
            vecinos = grafo[nodo_actual]
            vecinos.sort(key=lambda x: x[1]) # Ordenamos los vecinos por sus costos
            for vecino, costo in vecinos:
                if vecino not in visitados:
                    cola.append((vecino, camino_actual + [vecino], costo))
    print("No se encontro el objetivo.")
    return False

grafo = {
    'A': [('B', 7), ('C', 5), ('D', 3)],
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
busqueda_voraz(grafo, 'A', 'N')