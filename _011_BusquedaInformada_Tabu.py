
def busqueda_tabu(inicial, objetivo, graf, tabu_lista, max_iter):
    frontera = [(heuristica(inicial, objetivo), inicial, 0, [inicial])]
    frontera.sort()
    iteracion = 0

    while frontera:
        (_, estado_actual, costo_actual, camino) = frontera.pop(0)
        if estado_actual == objetivo:
            return estado_actual, costo_actual, camino

        if iteracion >= max_iter:
            return None, None, None

        for estado_vecino, costo in graf[estado_actual]:
            if estado_vecino not in tabu_lista:
                nuevo_costo = costo_actual + costo
                nuevo_camino = camino + [estado_vecino]
                frontera.append((heuristica(estado_vecino, objetivo) + nuevo_costo, estado_vecino, nuevo_costo, nuevo_camino))
                frontera.sort()
                tabu_lista.append(estado_vecino)
                if len(tabu_lista) > 10:  # Longitud máxima de la lista tabú
                    tabu_lista.pop(0)
        iteracion += 1

    return None, None, None

def heuristica(estado, objetivo):
    # Aquí puedes definir tu propia heurística
    return abs(estado - objetivo)

# Ejemplo de uso con grafo de nodos numéricos
graf = {
    1: [(2, 5), (3, 10)],
    2: [(4, 3), (5, 7)],
    3: [(6, 8)],
    4: [],
    5: [(6, 2)],
    6: []
}

inicial = 1
objetivo = 6
tabu_lista = []
max_iter = 20

objetivo_encontrado, costo_camino, camino = busqueda_tabu(inicial, objetivo, graf, tabu_lista, max_iter)

if objetivo_encontrado:
    print("Se encontro el objetivo:", objetivo_encontrado)
    print("Costo del camino:", costo_camino)
    print("Camino seguido:", camino)
else:
    print("No se encontro el objetivo dentro del limite de iteraciones.")
