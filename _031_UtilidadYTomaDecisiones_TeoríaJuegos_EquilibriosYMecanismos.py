class TeoriaJuegos:
    def __init__(self, pagos_jugador1, pagos_jugador2):
        # Inicializa la clase con los pagos para cada jugador
        self.pagos_jugador1 = pagos_jugador1  # Pagos para el jugador 1
        self.pagos_jugador2 = pagos_jugador2  # Pagos para el jugador 2

    def encontrar_equilibrio_nash(self):
        """
        Encuentra un equilibrio de Nash en el juego de dos jugadores.

        Returns:
            tuple: Una tupla que contiene las estrategias optimas para ambos jugadores.
        """
        # Inicializa las estrategias optimas y los pagos maximos
        estrategia_optima_jugador1 = None
        estrategia_optima_jugador2 = None
        max_pago_jugador1 = float('-inf')
        max_pago_jugador2 = float('-inf')

        # Busca la estrategia optima para el jugador 1
        for estrategia_jugador1, pagos in enumerate(self.pagos_jugador1):
            if max(pagos) > max_pago_jugador1:
                max_pago_jugador1 = max(pagos)
                estrategia_optima_jugador1 = estrategia_jugador1

        # Busca la estrategia optima para el jugador 2
        for estrategia_jugador2, pagos in enumerate(self.pagos_jugador2):
            if max(pagos) > max_pago_jugador2:
                max_pago_jugador2 = max(pagos)
                estrategia_optima_jugador2 = estrategia_jugador2

        # Retorna las estrategias optimas encontradas
        return (estrategia_optima_jugador1, estrategia_optima_jugador2)


# Definir los pagos para cada jugador en el juego
pagos_jugador1 = [[3, 2], [0, 2]]  # Pagos para el jugador 1 en cada estrategia
pagos_jugador2 = [[3, 0], [2, 4]]  # Pagos para el jugador 2 en cada estrategia

# Crear una instancia de TeoriaJuegos con los pagos definidos
teoria_juegos = TeoriaJuegos(pagos_jugador1, pagos_jugador2)

# Encontrar el equilibrio de Nash en el juego
equilibrio_nash = teoria_juegos.encontrar_equilibrio_nash()

# Imprimir el equilibrio de Nash encontrado
print("Equilibrio de Nash encontrado:")
print("Estrategia optima para el jugador 1:", equilibrio_nash[0])
print("Estrategia optima para el jugador 2:", equilibrio_nash[1])

