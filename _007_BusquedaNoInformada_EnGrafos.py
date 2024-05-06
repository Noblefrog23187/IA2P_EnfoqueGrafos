
# Definimos la estructura del grafo como un diccionario donde las claves son los nodos y los valores son las listas de nodos vecinos.
grafo = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H', 'I'],
    'E': ['J'],
    'F': ['K', 'L'],
    'G': ['M'],
    'H': [],
    'I': ['N'],
    'J': [],
    'K': [],
    'L': [],
    'M': [],
    'N': []
}

# Función de búsqueda en amplitud
def busqueda_amplitud(grafo, inicio):
    visitados = set() # Conjunto para almacenar los nodos visitados
    cola = [inicio] # Lista para almacenar los nodos que se están explorando

    while cola:
        nodo_actual = cola.pop(0) # Tomamos el primer elemento de la lista
        if nodo_actual not in visitados:
            print("Visitando nodo:", nodo_actual)
            visitados.add(nodo_actual)
            # Agregamos los nodos vecinos no visitados a la cola
            for vecino in grafo[nodo_actual]:
                if vecino not in visitados:
                    cola.append(vecino)
    
    # Imprimir el grafo resultante
    print("\nGrafo encontrado:")
    for nodo, vecinos in grafo.items():
        print(f"Nodo {nodo}: Vecinos {vecinos}")

busqueda_amplitud(grafo, 'A')