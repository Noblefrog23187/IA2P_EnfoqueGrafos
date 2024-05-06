import random  # Importa el modulo random para generar numeros aleatorios

class MinimosConflictos:  # Define la clase MinimosConflictos
    def __init__(self, variables, dominios, restricciones):
        # Inicializa la clase con las variables, dominios y restricciones
        self.variables = variables
        self.dominios = dominios
        self.restricciones = restricciones

    def minimos_conflictos(self, max_iter):
        # Implementa el algoritmo de minimos conflictos
        estado_actual = {var: random.choice(self.dominios[var]) for var in self.variables}
        # Inicializa el estado actual asignando valores aleatorios a las variables
        
        for _ in range(max_iter):  # Realiza un numero maximo de iteraciones
            conflicto_vars = self.obtener_conflictos(estado_actual)
            # Obtiene las variables con conflictos en el estado actual
            if not conflicto_vars:  # Si no hay variables en conflicto, se ha encontrado una solucion
                return estado_actual
            
            var = random.choice(conflicto_vars)  # Selecciona una variable en conflicto aleatoriamente
            val = self.obtener_valor_min_conflictos(var, estado_actual)
            # Obtiene el valor que minimiza los conflictos para la variable seleccionada
            estado_actual[var] = val  # Asigna el valor a la variable en el estado actual
        
        return None  # Retorna None si no se encontro una solucion en el numero maximo de iteraciones

    def obtener_conflictos(self, estado):
        # Obtiene las variables en conflicto en el estado actual
        conflicto_vars = []
        for var in self.variables:
            if not self.verificar_restricciones(var, estado):
                conflicto_vars.append(var)
        return conflicto_vars

    def obtener_valor_min_conflictos(self, var, estado):
        # Obtiene el valor que minimiza los conflictos para una variable dada
        min_conflictos = float('inf')
        val_min_conflictos = None
        for val in self.dominios[var]:
            estado[var] = val
            # Prueba cada valor en el dominio de la variable
            conflictos = len([var for var in self.variables if not self.verificar_restricciones(var, estado)])
            # Cuenta el numero de variables en conflicto despues de asignar el valor
            if conflictos < min_conflictos:
                min_conflictos = conflictos
                val_min_conflictos = val
                # Actualiza el valor minimo de conflictos y el valor correspondiente
        return val_min_conflictos

    def verificar_restricciones(self, var, estado):
        # Verifica si se cumplen todas las restricciones en el estado actual
        for restriccion in self.restricciones:
            if var in restriccion:
                if not restriccion(estado):
                    return False
        return True
