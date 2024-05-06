

def Busq_Cost_Unifo(graph, start, goal):
    
    visited = set()  # Conjunto de nodos visitados
    queue = [(0, start, [])]  # (costo acumulado, nodo actual, ruta hasta el nodo actual)
    
    
    while queue:
        
        cost, node, path = min(queue, key=lambda x: x[0]) # Extraemos el nodo con menor costo de la cola de prioridad
        queue.remove((cost, node, path))
        
        if node in visited:
            continue
       
        visited.add(node) # Agregamos el nodo a los nodos visitados
        
        path = path + [node]  # Actualizamos la ruta hasta el nodo actual
        
        if node == goal:
            return path
        
        for neighbor, neighbor_cost in graph[node].items():  # Exploramos los nodos vecinos del nodo actual
            if neighbor not in visited:
                
                total_cost = cost + neighbor_cost  # Calcula el costo total acumulado hasta el nodo vecino
                
                queue.append((total_cost, neighbor, path)) # Agregamos el nodo vecino a la cola de prioridad
    
    return None    # Si no se encuentra una ruta

graph = {
    'A': {'B': 1, 'C': 5},
    'B': {'A': 1, 'D': 3, 'E': 6},
    'C': {'A': 5, 'D': 2},
    'D': {'B': 3, 'C': 2, 'E': 4},
    'E': {'B': 6, 'D': 4}
}

# Nodo de inicio y nodo objetivo
start_node = 'A'
goal_node = 'E'

camino = Busq_Cost_Unifo(graph, start_node, goal_node)

if camino:
    print("Ruta mas corta de", start_node, "a", goal_node, ":", camino)
    total_cost = sum(graph[camino[i]][camino[i+1]] for i in range(len(camino)-1))
    print("Costo total de la ruta:", total_cost)
else:
    print("No se encontro una ruta de", start_node, "a", goal_node)