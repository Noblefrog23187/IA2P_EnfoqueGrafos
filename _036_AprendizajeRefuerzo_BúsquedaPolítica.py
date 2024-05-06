import numpy as np

class PolicySearch:
    def __init__(self, num_estados, num_acciones, learning_rate):
        """
        Inicializa el agente de busqueda de politica.

        Args:
            num_estados (int): El numero de estados del entorno.
            num_acciones (int): El numero de acciones posibles.
            learning_rate (float): Tasa de aprendizaje para la actualizacion de la politica.
        """
        self.num_estados = num_estados
        self.num_acciones = num_acciones
        self.learning_rate = learning_rate
        # Inicializa la politica aleatoriamente
        self.policy = np.random.rand(num_estados, num_acciones)
        # Normaliza la politica para que la suma de las probabilidades en cada estado sea 1
        self.policy /= np.sum(self.policy, axis=1, keepdims=True)

    def seleccionar_accion(self, estado):
        """
        Selecciona una accion segun la politica actual.

        Args:
            estado (int): El estado actual del entorno.

        Returns:
            int: La accion seleccionada.
        """
        return np.random.choice(self.num_acciones, p=self.policy[estado])

    def actualizar_politica(self, estados, acciones, recompensas):
        """
        Actualiza la politica utilizando el metodo de gradiente ascendente.

        Args:
            estados (list): Lista de estados visitados durante la interaccion con el entorno.
            acciones (list): Lista de acciones tomadas durante la interaccion con el entorno.
            recompensas (list): Lista de recompensas recibidas durante la interaccion con el entorno.
        """
        # Inicializa el gradiente de la politica
        gradient = np.zeros_like(self.policy)
        for estado, accion, recompensa in zip(estados, acciones, recompensas):
            # Calcula el gradiente para la accion seleccionada en el estado actual
            gradient[estado, accion] += recompensa
        # Actualiza la politica utilizando el gradiente ascendente
        self.policy += self.learning_rate * gradient
        # Normaliza la politica despues de la actualizacion
        self.policy /= np.sum(self.policy, axis=1, keepdims=True)

# Definir parametros del entorno y del agente
num_estados = 5
num_acciones = 3
learning_rate = 0.01

# Crear una instancia del agente de busqueda de politica
policy_search_agent = PolicySearch(num_estados, num_acciones, learning_rate)

# Simular interaccion con el entorno y actualizacion de la politica
for _ in range(1000):
    # Simular un paso en el entorno
    estado_actual = np.random.randint(num_estados)  # Estado inicial aleatorio
    accion_seleccionada = policy_search_agent.seleccionar_accion(estado_actual)
    recompensa = np.random.normal(loc=0, scale=1)  # Recompensa aleatoria
    # Actualizar la politica basada en la experiencia
    policy_search_agent.actualizar_politica([estado_actual], [accion_seleccionada], [recompensa])

# Imprimir la politica aprendida
print("Politica aprendida:")
print(policy_search_agent.policy)

