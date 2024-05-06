def calcular_utilidad(valor, pendiente, intercepto):
    """
    Calcula la utilidad utilizando una funcion de utilidad lineal.

    Args:
        valor (float): El valor a evaluar.
        pendiente (float): La pendiente de la funcion de utilidad.
        intercepto (float): El intercepto de la funcion de utilidad.

    Returns:
        float: La utilidad calculada.
    """
    return pendiente * valor + intercepto

# Definir los parametros de la funcion de utilidad
pendiente = 0.5
intercepto = 2.0

# Ejemplo de uso
valor_producto = 10.0
utilidad = calcular_utilidad(valor_producto, pendiente, intercepto)

# Imprimir la utilidad
print("La utilidad para un producto con valor", valor_producto, "es:", utilidad)

