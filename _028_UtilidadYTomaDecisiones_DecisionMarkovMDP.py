import numpy as np

class MDP:
    def __init__(self, estados, acciones, recompensas, transiciones, gamma=0.9):
        """
        Inicializa el Proceso de Decision de Markov (MDP).

        Args:
            estados (list): Lista de estados posibles.
            acciones (list): Lista de acciones posibles.
            recompensas (dict): Diccionario que mapea cada par (estado, accion) a su recompensa.
            transiciones (dict): Diccionario que mapea cada par (estado, accion) a la distribucion de probabilidades
                                 sobre los estados siguientes.
            gamma (float): Factor de descuento para futuras recompensas.
        """
        self.estados = estados
        self.acciones = acciones
        self.recompensas = recompensas
        self.transiciones = transiciones
        self.gamma = gamma

    def iteracion_valor(self, epsilon=0.01):
        """
        Realiza la iteracion de valor para calcular la utilidad optima de cada estado.

        Args:
            epsilon (float): Criterio de convergencia para detener la iteracion.

        Returns:
            dict: Diccionario que contiene la utilidad optima para cada estado.
        """
        # Inicializar la utilidad de cada estado a 0
        utilidad = {estado: 0 for estado in self.estados}

        # Iteracion de valor
        while True:
            delta = 0
            for estado in self.estados:
                mejor_utilidad = float('-inf')
                for accion in self.acciones:
                    accion_utilidad = sum(prob * (self.recompensas.get((estado, accion), 0) +
                                                  self.gamma * utilidad[estado_siguiente])
                                          for estado_siguiente, prob in self.transiciones.get((estado, accion), {}).items())
                    mejor_utilidad = max(mejor_utilidad, accion_utilidad)
                delta = max(delta, abs(mejor_utilidad - utilidad[estado]))
                utilidad[estado] = mejor_utilidad
            if delta < epsilon:
                break

        return utilidad

# Definir estados, acciones, recompensas y transiciones
estados = ['A', 'B', 'C']
acciones = ['Subir', 'Bajar']
recompensas = {('A', 'Subir'): 4, ('A', 'Bajar'): 2, ('B', 'Subir'): 3, ('B', 'Bajar'): 2,
               ('C', 'Subir'): 3, ('C', 'Bajar'): 1}
transiciones = {('A', 'Subir'): {'A': 0.7, 'B': 0.2, 'C': 0.1},
                ('A', 'Bajar'): {'A': 0.1, 'B': 0.6, 'C': 0.3},
                ('B', 'Subir'): {'A': 0.3, 'B': 0.5, 'C': 0.2},
                ('B', 'Bajar'): {'A': 0.2, 'B': 0.4, 'C': 0.4},
                ('C', 'Subir'): {'A': 0.5, 'B': 0.3, 'C': 0.2},
                ('C', 'Bajar'): {'A': 0.4, 'B': 0.3, 'C': 0.3}}

# Crear una instancia del Proceso de Decision de Markov (MDP) y realizar la iteracion de valor
mdp = MDP(estados, acciones, recompensas, transiciones)
utilidad_optima = mdp.iteracion_valor()

# Imprimir la utilidad optima para cada estado
print("Utilidad optima para cada estado:")
for estado, utilidad in utilidad_optima.items():
    print(f"{estado}: {utilidad}")

