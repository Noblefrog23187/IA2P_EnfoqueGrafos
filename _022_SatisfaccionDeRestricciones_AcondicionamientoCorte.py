def cutting_stock_brute_force(demands, stock_length):
    """
    Implementa el algoritmo de fuerza bruta para el Acondicionamiento del Corte (Cutting Stock).

    Args:
        demands (list): Una lista de las demandas de cada pieza.
        stock_length (int): La longitud del stock disponible.

    Returns:
        list: Una lista que contiene la cantidad de stock necesario para satisfacer cada demanda.
    """
    # Ordena las demandas de mayor a menor
    demands_sorted = sorted(demands, reverse=True)
    stock_count = []  # Lista para almacenar la cantidad de stock necesario para cada demanda

    while demands_sorted:
        stock_used = 0  # Inicializa el stock utilizado para cortar las piezas
        remaining_length = stock_length  # Inicializa la longitud restante del stock
        
        for demand in demands_sorted:
            if demand <= remaining_length:
                # Si la demanda cabe en el stock restante, se corta una pieza y se actualizan las variables
                stock_used += 1
                remaining_length -= demand
            else:
                break  # Si no cabe, se pasa a la siguiente demanda

        # Se agrega la cantidad de stock utilizada a la lista
        stock_count.append(stock_used)
        # Se eliminan las demandas ya satisfechas
        demands_sorted = demands_sorted[stock_used:]

    return stock_count


# Ejemplo de uso
demands = [20, 15, 12, 10, 8]  # Demandas de cada pieza
stock_length = 100  # Longitud del stock disponible

# Ejecutar el algoritmo de fuerza bruta
stock_count = cutting_stock_brute_force(demands, stock_length)

# Imprimir los resultados
print("Cantidad de stock necesaria para cada demanda:", stock_count)
