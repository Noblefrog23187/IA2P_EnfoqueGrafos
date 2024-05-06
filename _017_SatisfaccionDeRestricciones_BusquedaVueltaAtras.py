def backtracking_con_propagacion(variables, dominios, restricciones, asignaciones):
    """
    Realiza la busqueda con backtracking con propagacion de restricciones.

    Args:
        variables (list): Lista de variables.
        dominios (dict): Diccionario que mapea variables a sus dominios.
        restricciones (list): Lista de restricciones.
        asignaciones (dict): Diccionario que mapea variables asignadas a sus valores.

    Returns:
        dict or None: Las asignaciones que satisfacen todas las restricciones o None si no se encuentra ninguna asignacion.
    """
    if len(asignaciones) == len(variables):  # Verifica si todas las variables estan asignadas
        return asignaciones  # Retorna las asignaciones si todas las variables estan asignadas

    variable = seleccionar_variable_sin_asignar(variables, asignaciones)  # Selecciona una variable no asignada
    for valor in ordenar_valores(dominios[variable]):  # Itera sobre los valores de la variable
        if es_valor_consistente(variable, valor, asignaciones, restricciones):  # Verifica si el valor es consistente
            asignaciones[variable] = valor  # Asigna el valor a la variable
            dominios_reducidos = propagar_restricciones(variable, valor, asignaciones, dominios, restricciones)  # Propaga las restricciones
            if dominios_reducidos is not None:  # Verifica si no hay conflictos
                resultado = backtracking_con_propagacion(variables, dominios_reducidos, restricciones, asignaciones)  # Realiza una llamada recursiva
                if resultado is not None:  # Verifica si se encontro una solucion
                    return resultado  # Retorna las asignaciones si se encontro una solucion
            asignaciones[variable] = None  # Retrocede y elimina la asignacion si no se encontro una solucion
    return None  # Retorna None si no se encontro ninguna asignacion valida

