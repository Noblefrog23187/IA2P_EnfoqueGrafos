
def Busq_Ancho(graph, start, goal):
    visited = set()  # Para poner los nodos visitados
    stack = [(start, [start])]  # Cantidad de nodos a explorar, con el nodo inicial y su camino hasta ese punto

    while stack:  # Mientras existan nodos por visitar
        node, path = stack.pop()  # Tomar el último nodo de la fila
        if node not in visited:  # Si el nodo no ha sido visitado
            visited.add(node)  # Marcar el nodo como visitado
            if node == goal:  # Si el nodo es el objetivo
                return path  # Devolver el camino hasta ese nodo
            # Extender la fila con los nodos vecinos y sus caminos
            stack.extend((neighbor, path + [neighbor]) for neighbor in graph[node])

    return None  # Si no se encuentra un camino hasta el objetivo, devolver None

# Ejemplo de uso
graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}
start = 'A'
goal = 'E'
camino = Busq_Ancho(graph, start, goal)

print("Camino encontrado por busqueda por anchura: ", camino )