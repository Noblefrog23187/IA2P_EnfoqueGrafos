#Definir la funcion de restriccion
def restriccion(A, B):
    return A != B  # La restriccion se cumple si A y B son diferentes

# Definir la funcion de Salto Atras Dirigido por Conflictos (Backjumping)
def backjumping(variables, dominios):
    asignaciones = {}  # Inicializar las asignaciones como un diccionario vacio
    conflict_set = set()  # Inicializar el conjunto de conflictos como un conjunto vacio

    while len(asignaciones) < len(variables):  # Mientras haya variables sin asignar
        variable = seleccionar_variable_sin_asignar(variables, asignaciones)  # Seleccionar una variable sin asignar

        # Seleccionar un valor del dominio de la variable actual
        for valor in dominios[variable]:
            asignaciones[variable] = valor  # Asignar el valor a la variable
            if es_consistente(asignaciones, restriccion):  # Verificar si la asignacion actual es consistente
                break  # Si es consistente, romper el bucle y pasar a la siguiente variable

        # Si no se encontro un valor consistente, hay un conflicto
        if variable in asignaciones and not es_consistente(asignaciones, restriccion):
            conflict_set.add(variable)  # Agregar la variable al conjunto de conflictos
            variable_conflicto = conflict_set.pop()  # Seleccionar una variable del conjunto de conflictos
            del asignaciones[variable_conflicto]  # Eliminar la asignacion de la variable de conflicto

    return asignaciones  # Devolver las asignaciones

# Funcion auxiliar para verificar la consistencia de las asignaciones
def es_consistente(asignaciones, restriccion):
    for var1, val1 in asignaciones.items():
        for var2, val2 in asignaciones.items():
            if var1 != var2 and not restriccion(val1, val2):
                return False  # Si alguna restriccion no se cumple, las asignaciones no son consistentes
    return True  # Si todas las restricciones se cumplen, las asignaciones son consistentes

# Funcion auxiliar para seleccionar una variable sin asignar
def seleccionar_variable_sin_asignar(variables, asignaciones):
    for variable in variables:
        if variable not in asignaciones:
            return variable  # Devolver la primera variable sin asignar encontrada

# Definir las variables y sus dominios
variables = ['A', 'B', 'C']
dominios = {
    'A': [1, 2, 3],
    'B': [4, 5],
    'C': [2, 3]
}

# Obtener las asignaciones mediante Salto Atras Dirigido por Conflictos
asignaciones = backjumping(variables, dominios)

# Imprimir las asignaciones encontradas
print("Asignaciones encontradas:")
for variable, valor in asignaciones.items():
    print(f"{variable}: {valor}")

