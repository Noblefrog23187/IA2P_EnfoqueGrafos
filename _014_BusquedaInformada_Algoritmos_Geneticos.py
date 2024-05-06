import random  # Importa el modulo random para generar numeros aleatorios

def generar_poblacion(tamano_poblacion, longitud_cromosoma):  
    """
    Genera una poblacion inicial de cromosomas aleatorios.

    Args:
        tamano_poblacion (int): Tamano de la poblacion.
        longitud_cromosoma (int): Longitud de cada cromosoma.

    Returns:
        list: Lista de cromosomas generados.
    """
    poblacion = []  # Inicializa una lista para almacenar la poblacion
    for _ in range(tamano_poblacion):  # Itera sobre el tamano de la poblacion
        cromosoma = [random.randint(0, 1) for _ in range(longitud_cromosoma)]  # Genera un cromosoma aleatorio
        poblacion.append(cromosoma)  # Agrega el cromosoma a la poblacion
    return poblacion

def evaluar_poblacion(poblacion, funcion_objetivo):  
    """
    Evalua la poblacion de acuerdo a una funcion objetivo dada.

    Args:
        poblacion (list): Lista de cromosomas a evaluar.
        funcion_objetivo (function): Funcion objetivo que asigna un valor a cada cromosoma.

    Returns:
        list: Lista de tuplas (cromosoma, valor) con la evaluacion de cada cromosoma.
    """
    evaluacion = []  # Inicializa una lista para almacenar la evaluacion de la poblacion
    for cromosoma in poblacion:  # Itera sobre cada cromosoma en la poblacion
        valor = funcion_objetivo(cromosoma)  # Evalua el cromosoma usando la funcion objetivo
        evaluacion.append((cromosoma, valor))  # Agrega la evaluacion a la lista de evaluacion
    return evaluacion

def seleccionar_padres(poblacion_evaluada, num_padres):  
    """
    Selecciona los padres para la proxima generacion.

    Args:
        poblacion_evaluada (list): Lista de tuplas (cromosoma, valor) con la evaluacion de cada cromosoma.
        num_padres (int): Numero de padres a seleccionar.

    Returns:
        list: Lista de cromosomas seleccionados como padres.
    """
    # Ordena la poblacion evaluada por valor de evaluacion
    poblacion_ordenada = sorted(poblacion_evaluada, key=lambda x: x[1])
    # Selecciona los num_padres mejores cromosomas como padres
    padres = [individuo[0] for individuo in poblacion_ordenada[:num_padres]]
    return padres

def cruzar(padres, tamano_poblacion):  
    """
    Cruza los padres para producir descendencia.

    Args:
        padres (list): Lista de cromosomas padres.
        tamano_poblacion (int): Tamano deseado de la poblacion descendiente.

    Returns:
        list: Lista de cromosomas descendientes.
    """
    descendencia = []  # Inicializa una lista para almacenar la descendencia
    while len(descendencia) < tamano_poblacion:  # Repite hasta que se alcance el tamano deseado de la poblacion
        padre1, padre2 = random.sample(padres, 2)  # Selecciona dos padres aleatorios
        punto_cruce = random.randint(1, len(padre1) - 1)  # Elige un punto de cruce aleatorio
        hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]  # Crea el primer hijo combinando partes de los padres
        hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]  # Crea el segundo hijo combinando partes de los padres
        descendencia.append(hijo1)  # Agrega el primer hijo a la descendencia
        descendencia.append(hijo2)  # Agrega el segundo hijo a la descendencia
    return descendencia

def mutar(poblacion, tasa_mutacion):  
    """
    Muta la poblacion dada con una cierta tasa de mutacion.

    Args:
        poblacion (list): Lista de cromosomas a mutar.
        tasa_mutacion (float): Tasa de mutacion (probabilidad de que un bit mute).

    Returns:
        list: Lista de cromosomas mutados.
    """
    for i in range(len(poblacion)):  # Itera sobre cada cromosoma en la poblacion
        for j in range(len(poblacion[i])):  # Itera sobre cada bit en el cromosoma
            if random.random() < tasa_mutacion:  # Determina si se produce una mutacion para este bit
                poblacion[i][j] = 1 - poblacion[i][j]  # Realiza la mutacion (cambia 0 a 1 o 1 a 0)
    return poblacion

def algoritmo_genetico(funcion_objetivo, tamano_poblacion, longitud_cromosoma, num_generaciones, tasa_mutacion):
    """
    Implementa el algoritmo genetico para encontrar una solucion optima para un problema dado.

    Args:
        funcion_objetivo (function): Funcion objetivo a optimizar.
        tamano_poblacion (int): Tamano de la poblacion.
        longitud_cromosoma (int): Longitud de cada cromosoma.
        num_generaciones (int): Numero de generaciones a evolucionar.
        tasa_mutacion (float): Tasa de mutacion.

    Returns:
        tuple: Tupla con el mejor cromosoma encontrado y su valor.
    """
    poblacion = generar_poblacion(tamano_poblacion, longitud_cromosoma)  # Genera una poblacion inicial aleatoria
    for _ in range(num_generaciones):  # Evoluciona la poblacion a lo largo de un numero de generaciones
        poblacion_evaluada = evaluar_poblacion(poblacion, funcion_objetivo)  # Evalua la poblacion actual
        padres = seleccionar_padres(poblacion_evaluada, tamano_poblacion // 2)  # Selecciona los padres
        descendencia = cruzar(padres, tamano_poblacion)  # Cruza los padres para producir descendencia
        poblacion = mutar

