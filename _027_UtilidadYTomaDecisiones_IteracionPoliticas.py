import random

class IteracionPoliticas:
    def __init__(self, estados, acciones, utilidad, recompensa, descuento):
        """
        Inicializa la Iteracion de Politicas.

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

    def iteracion_politicas(self, epsilon=0.01):
        """
        Realiza la iteracion de politicas para calcular la politica optima.

        Args:
            epsilon (float): Criterio de convergencia para detener la iteracion.

        Returns:
            dict: Diccionario que contiene la accion optima para cada estado.
        """
        politica_optima = {estado: random.choice(self.acciones) for estado in self.estados}
        while True:
            delta = 0
            for estado in self.estados:
                mejor_accion = None
                mejor_utilidad = float('-inf')
                for accion in self.acciones:
                    accion_utilidad = self.recompensa.get((estado, accion), 0) + \
                                      self.descuento * self.utilidad.get((estado, accion), 0)
                    if accion_utilidad > mejor_utilidad:
                        mejor_accion = accion
                        mejor_utilidad = accion_utilidad
                delta = max(delta, abs(self.utilidad.get((estado, politica_optima[estado]), 0) - mejor_utilidad))
                politica_optima[estado] = mejor_accion
            if delta < epsilon:
                break
        return politica_optima


# Definir estados, acciones, utilidades, recompensas y factor de descuento
estados = ['A', 'B', 'C']
acciones = ['Subir', 'Bajar']
utilidad = {('A', 'Subir'): 0, ('A', 'Bajar'): 0, ('B', 'Subir'): 0, ('B', 'Bajar'): 0,
            ('C', 'Subir'): 0, ('C', 'Bajar'): 0}
recompensa = {('A', 'Subir'): 4, ('A', 'Bajar'): 2, ('B', 'Subir'): 3, ('B', 'Bajar'): 2,
              ('C', 'Subir'): 3, ('C', 'Bajar'): 1}
descuento = 0.9

# Crear una instancia de Iteracion de Politicas y realizar la iteracion
iteracion_politicas = IteracionPoliticas(estados, acciones, utilidad, recompensa, descuento)
politica_optima = iteracion_politicas.iteracion_politicas()

# Imprimir la politica optima para cada estado
print("Politica optima para cada estado:")
for estado, accion in politica_optima.items():
    print(f"{estado}: {accion}")

