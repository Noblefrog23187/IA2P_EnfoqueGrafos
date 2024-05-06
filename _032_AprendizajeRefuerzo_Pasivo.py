import numpy as np

class AprendizajePorRefuerzoPasivo:
    def __init__(self, num_estados, num_acciones, matriz_recompensas, factor_descuento, epsilon):
        """
        Inicializa el agente de aprendizaje por refuerzo pasivo.

        Args:
            num_estados (int): El numero de estados en el entorno.
            num_acciones (int): El numero de acciones posibles.
            matriz_recompensas (numpy.ndarray): La matriz de recompensas del entorno.
            factor_descuento (float): El factor de descuento para futuras recompensas.
            epsilon (float): La probabilidad de exploracion.
        """
        self.num_estados = num_estados
        self.num_acciones = num_acciones
        self.matriz_recompensas = matriz_recompensas
        self.factor_descuento = factor_descuento
        self.epsilon = epsilon

        # Inicializa el valor Q para cada par (estado, accion)
        self.Q = np.zeros((num_estados, num_acciones))

    def seleccionar_accion(self, estado):
        """
        Selecciona una accion para un estado dado utilizando una politica epsilon-greedy.

        Args:
            estado (int): El estado actual del agente.

        Returns:
            int: La accion seleccionada.
        """
        # Decide si se explora o se explota
        if np.random.rand() < self.epsilon:
            # Exploracion: selecciona una accion al azar
            return np.random.choice(self.num_acciones)
        else:
            # Explotacion: selecciona la accion con el mayor valor Q
            return np.argmax(self.Q[estado])

    def actualizar_valor_Q(self, estado, accion, recompensa, proximo_estado):
        """
        Actualiza el valor Q para el par (estado, accion) dado el resultado de una transicion.

        Args:
            estado (int): El estado actual.
            accion (int): La accion realizada en el estado actual.
            recompensa (float): La recompensa recibida por la accion realizada.
            proximo_estado (int): El estado resultante de la transicion.
        """
        # Calcula el objetivo de la actualizacion del valor Q
        objetivo = recompensa + self.factor_descuento * np.max(self.Q[proximo_estado])

        # Actualiza el valor Q utilizando la regla de actualizacion Q-learning
        self.Q[estado, accion] += objetivo - self.Q[estado, accion]


# Definir los parametros del entorno y el agente
num_estados = 3
num_acciones = 2
matriz_recompensas = np.array([[7, 1], [8, 3], [9, 5]])
factor_descuento = 0.9
epsilon = 0.1

# Crear una instancia del agente de aprendizaje por refuerzo pasivo
agente = AprendizajePorRefuerzoPasivo(num_estados, num_acciones, matriz_recompensas, factor_descuento, epsilon)

# Ejecutar un episodio de interaccion con el entorno
estado_actual = 0
accion = agente.seleccionar_accion(estado_actual)
recompensa = matriz_recompensas[estado_actual, accion]
proximo_estado = estado_actual + 1
agente.actualizar_valor_Q(estado_actual, accion, recompensa, proximo_estado)

# Imprimir los valores Q aprendidos por el agente
print("Valores Q aprendidos por el agente:")
print(agente.Q)
