import random  # Importa el modulo random para generar numeros aleatorios

def generar_solucion(n):  # Define una funcion para generar una solucion aleatoria
    return [random.randint(1, n) for _ in range(n)]  # Retorna una lista de longitud n con valores aleatorios entre 1 y n

def generar_vecinos(solucion):  # Define una funcion para generar vecinos de una solucion
    vecinos = []  # Inicializa una lista para almacenar los vecinos
    n = len(solucion)  # Obtiene la longitud de la solucion

    for i in range(n):  # Itera sobre cada posicion de la solucion
        for j in range(1, n + 1):  # Itera sobre cada posible valor para esa posicion
            if j != solucion[i]:  # Verifica si el valor es diferente al valor actual en esa posicion
                vecino = list(solucion)  # Crea una copia de la solucion actual
                vecino[i] = j  # Actualiza el valor en la posicion i con el nuevo valor j
                vecinos.append(vecino)  # Agrega el vecino a la lista de vecinos

    return vecinos  # Retorna la lista de vecinos generados

def evaluar_solucion(solucion):  # Define una funcion para evaluar una solucion
    # En este ejemplo, la funcion de evaluacion simplemente cuenta el numero de conflictos entre reinas en un tablero de ajedrez
    n = len(solucion)  # Obtiene la longitud de la solucion
    conflicts = 0  # Inicializa el contador de conflictos

    for i in range(n):  # Itera sobre cada par de reinas en la solucion
        for j in range(i + 1, n):
            if solucion[i] == solucion[j] or abs(solucion[i] - solucion[j]) == j - i:  # Verifica si hay un conflicto entre las reinas
                conflicts += 1  # Incrementa el contador de conflictos si se encuentra un conflicto

    return conflicts  # Retorna el numero de conflictos en la solucion

def local_beam_search(n, k, max_iter):  # Define la funcion de Busqueda de Haz Local
    # Genera k soluciones aleatorias como punto de partida
    soluciones = [generar_solucion(n) for _ in range(k)]

    for _ in range(max_iter):  # Realiza un numero maximo de iteraciones
        vecinos = []  # Inicializa una lista para almacenar los vecinos de todas las soluciones

        for solucion in soluciones:  # Itera sobre cada solucion en el haz
            vecinos.extend(generar_vecinos(solucion))  # Genera los vecinos de la solucion y los agrega a la lista

        vecinos.sort(key=evaluar_solucion)  # Ordena los vecinos segun su evaluacion (menos conflictos primero)

        if evaluar_solucion(vecinos[0]) == 0:  # Verifica si se ha encontrado una solucion optima
            return vecinos[0]  # Retorna la primera solucion optima encontrada

        soluciones = vecinos[:k]  # Selecciona las k mejores soluciones como nuevos puntos de partida

    return None  # Retorna None si no se encuentra una solucion optima dentro del numero maximo de iteraciones

# Parametros de la busqueda
n = 8  # Numero de reinas en el problema de las N reinas
k = 5  # Numero de soluciones en el haz
max_iter = 1000  # Numero maximo de iteraciones

# Realiza la busqueda de haz local
solucion_optima = local_beam_search(n, k, max_iter)

# Imprime la solucion optima encontrada
if solucion_optima:
    print("Solucion optima encontrada:", solucion_optima)
else:
    print("No se encontro una solucion optima dentro del numero maximo de iteraciones.")

