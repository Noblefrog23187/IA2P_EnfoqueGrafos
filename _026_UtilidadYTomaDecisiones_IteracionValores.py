class IteracionValores:
    def __init__(self, estados, acciones, utilidad, recompensa, descuento):
        """
        Inicializa la Iteracion de Valores.

        Args:
            estados (list): Lista de estados del sistema.
            acciones (list): Lista de acciones disponibles en cada estado.
            utilidad (dict): Diccionario que mapea cada par (estado, accion) a su utilidad inicial.
            recompensa (dict): Diccionario que mapea cada par (estado, accion) a su recompensa inmediata.
            descuento (float): Factor de descuento para futuras recompensas.
        """
        self.estados = estados
        self.acciones = acciones
        self.utilidad = utilidad
        self.recompensa = recompensa
        self.descuento = descuento

    def iteracion_valores(self, epsilon=0.01):
        """
        Realiza la iteracion de valores para calcular la utilidad de cada estado.

        Args:
            epsilon (float): Criterio de convergencia para detener la iteracion.

        Returns:
            dict: Diccionario que contiene la utilidad final de cada estado.
        """
        nueva_utilidad = {estado: 0 for estado in self.estados}
        while True:
            delta = 0
            for estado in self.estados:
                mejor_utilidad = float('-inf')
                for accion in self.acciones:
                    accion_utilidad = self.recompensa.get((estado, accion), 0) + \
                                      self.descuento * self.utilidad.get(estado, 0)
                    if accion_utilidad > mejor_utilidad:
                        mejor_utilidad = accion_utilidad
                delta = max(delta, abs(mejor_utilidad - nueva_utilidad[estado]))
                nueva_utilidad[estado] = mejor_utilidad
            if delta < epsilon:
                break
            self.utilidad = nueva_utilidad.copy()
        return self.utilidad


# Definir estados, acciones, utilidades, recompensas y factor de descuento
estados = ['A', 'B', 'C']
acciones = ['Subir', 'Bajar']
utilidad = {'A': 0, 'B': 0, 'C': 0}
recompensa = {('A', 'Subir'): 4, ('A', 'Bajar'): 2, ('B', 'Subir'): 3, ('B', 'Bajar'): 2,
              ('C', 'Subir'): 3, ('C', 'Bajar'): 1}
descuento = 0.9

# Crear una instancia de Iteracion de Valores y realizar la iteracion
iteracion_valores = IteracionValores(estados, acciones, utilidad, recompensa, descuento)
utilidad_final = iteracion_valores.iteracion_valores()

# Imprimir la utilidad final de cada estado
print("Utilidad final de cada estado:")
for estado, u in utilidad_final.items():
    print(f"{estado}: {u}")

