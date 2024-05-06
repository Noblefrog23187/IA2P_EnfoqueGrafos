import numpy as np

class EstrategiaExploracionExplotacion:
    def __init__(self, num_acciones, epsilon):
        """
        Inicializa la estrategia de exploracion-explotacion.

        Args:
            num_acciones (int): El numero de acciones posibles.
            epsilon (float): La probabilidad de exploracion.
        """
        self.num_acciones = num_acciones
        self.epsilon = epsilon
        # Inicializa los valores esperados de las acciones a cero
        self.valores_esperados = np.zeros(num_acciones)

    def seleccionar_accion(self):
        """
        Selecciona una accion utilizando una politica epsilon-greedy.

        Returns:
            int: La accion seleccionada.
        """
        # Decide si se explora o se explota
        if np.random.rand() < self.epsilon:
            # Exploracion: selecciona una accion al azar
            return np.random.choice(self.num_acciones)
        else:
            # Explotacion: selecciona la accion con el mayor valor esperado
            return np.argmax(self.valores_esperados)

    def actualizar_valor_esperado(self, accion, recompensa):
        """
        Actualiza el valor esperado de la accion basado en la recompensa observada.

        Args:
            accion (int): La accion tomada.
            recompensa (float): La recompensa observada.
        """
        # Actualiza el valor esperado de la accion utilizando la regla de actualizacion de la media incremental
        self.valores_esperados[accion] += (recompensa - self.valores_esperados[accion]) / (self.valores_esperados[accion] + 1)

# Definir parametros del entorno
num_acciones = 3  # Numero de acciones posibles
epsilon = 0.1  # Probabilidad de exploracion

# Crear una instancia de la estrategia de exploracion-explotacion
estrategia = EstrategiaExploracionExplotacion(num_acciones, epsilon)

# Ejemplo de uso: seleccion de acciones durante varios pasos de tiempo
for paso_tiempo in range(10):
    # Seleccionar una accion utilizando la estrategia
    accion_seleccionada = estrategia.seleccionar_accion()
    # Simular la observacion de una recompensa (en este ejemplo, una recompensa aleatoria)
    recompensa_observada = np.random.normal(loc=0, scale=1)
    # Actualizar el valor esperado de la accion basado en la recompensa observada
    estrategia.actualizar_valor_esperado(accion_seleccionada, recompensa_observada)
    # Imprimir la accion seleccionada en el paso de tiempo actual
    print(f"Paso de tiempo {paso_tiempo}: Accion seleccionada = {accion_seleccionada}")


