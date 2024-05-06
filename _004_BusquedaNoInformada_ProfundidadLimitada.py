
def busq_prof_lim(grafo, inicio, objetivo, limite_profundidad):
    
    visitados = set()     # Conjunto para llevar un seguimiento de los nodos visitados
    stack = [(inicio, [inicio], 0)]     # Fila para realizar la búsqueda en profundidad

    while stack:
        
        nodo, camino, profundidad = stack.pop() # Extraer el nodo actual, su camino y su profundidad desde la fila
        if profundidad > limite_profundidad:
            continue  # Si se excede el límite de profundidad, pasa al siguiente nodo
        
        if nodo not in visitados:
            visitados.add(nodo)  # Marcar el nodo como visitado en caso de que no haya sido visitado

            if nodo == objetivo: 
                return camino  # Devolver el camino si se encuentra en el nodo objetivo
            
            # Extender la fila con los vecinos del nodo actual
            for vecino in grafo[nodo]:
                stack.append((vecino, camino + [vecino], profundidad + 1))

    # Si no se encuentra un camino dentro del límite de profundidad, devolver un mensaje
    return "No se encontro un camino dentro del limite de profundidad."

# Ejemplo de uso con un grafo más complejo
grafo = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E', 'G'],
         'G': ['H', 'I'],
         'H': ['G', 'J'],
         'I': ['G', 'K'],
         'J': ['H'],
         'K': ['I']}

inicio = 'A'
objetivo = 'H'
limite_profundidad = 3
print("Camino encontrado por Busqueda en Profundidad Limitada:", busq_prof_lim(grafo, inicio, objetivo, limite_profundidad))