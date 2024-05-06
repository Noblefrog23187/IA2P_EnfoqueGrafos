from itertools import product  # Importa la funcion product del modulo itertools

# Definir variables y dominios
variables = {'A': [1, 2, 3], 'B': [4, 5], 'C': [2, 3]}  # Define un diccionario con variables y sus dominios

# Definir restricciones
def constraint_function(A, B, C):  # Define una funcion de restriccion que toma valores de variables A, B y C
    return A < B and B in [2, 3] and C % 2 == 0  # Devuelve True si se cumplen las restricciones

# Aplicar fuerza bruta para encontrar solucion
for values in product(*variables.values()):  # Itera sobre todas las combinaciones posibles de valores de las variables
    if constraint_function(*values):  # Verifica si la combinacion de valores cumple con las restricciones
        solution = dict(zip(variables.keys(), values))  # Crea un diccionario de solucion mapeando variables a valores
        print("Solucion encontrada:", solution)  # Imprime la solucion encontrada
        break  # Sale del bucle despues de encontrar la primera solucion que cumple con las restricciones
