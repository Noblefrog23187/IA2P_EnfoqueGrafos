
def busqueda_bidireccional(grafo, inicio, objetivo):
    # Funcion para expandir un nodo en el grafo
    def expandir_nodo(nodo, direccion):
        if direccion == 'adelante':
            return grafo[nodo]
        elif direccion == 'atras':
            return grafo[nodo]

    # Inicializacion de los conjuntos de nodos visitados en ambas direcciones
    visitados_adelante = {inicio}
    visitados_atras = {objetivo}

    # Inicializacion de las fronteras de busqueda en ambas direcciones
    frontera_adelante = [inicio]
    frontera_atras = [objetivo]

    while frontera_adelante and frontera_atras:
        # Expandir un paso hacia adelante
        nuevo_nivel_adelante = []
        for nodo_actual in frontera_adelante:
            for vecino in expandir_nodo(nodo_actual, 'adelante'):
                if vecino not in visitados_adelante:
                    if vecino in visitados_atras:
                        # Se ha encontrado un nodo comun, la busqueda ha terminado
                        return reconstruir_camino(inicio, vecino, visitados_adelante), True
                    visitados_adelante.add(vecino)
                    nuevo_nivel_adelante.append(vecino)
        frontera_adelante = nuevo_nivel_adelante

        # Expandir un paso hacia atras
        nuevo_nivel_atras = []
        for nodo_actual in frontera_atras:
            for vecino in expandir_nodo(nodo_actual, 'atras'):
                if vecino not in visitados_atras:
                    if vecino in visitados_adelante:
                        # Se ha encontrado un nodo comun, la busqueda ha terminado
                        return reconstruir_camino(inicio, vecino, visitados_adelante), True
                    visitados_atras.add(vecino)
                    nuevo_nivel_atras.append(vecino)
        frontera_atras = nuevo_nivel_atras

    # No se encontro un camino entre los nodos
    return [], False

def reconstruir_camino(inicio, nodo_comun, visitados_adelante):
    camino_adelante = []
    nodo_actual = nodo_comun
    while nodo_actual != inicio:
        camino_adelante.append(nodo_actual)
        for vecino in grafo[nodo_actual]:
            if vecino in visitados_adelante:
                nodo_actual = vecino
                break
    camino_adelante.append(inicio)
    camino_adelante.reverse()
    return camino_adelante

# Ejemplo de uso
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['C', 'G'],
    'F': ['D'],
    'G': ['E']
}

inicio = 'A'
objetivo = 'F'

camino, resultado = busqueda_bidireccional(grafo, inicio, objetivo)
if resultado:
    print("Se encontro un camino entre", inicio, "y", objetivo)
    print("Camino encontrado:", camino)
else:
    print("No se encontro un camino entre", inicio, "y", objetivo)
