# Importar la libreria para trabajar con restricciones
from constraint import *

# Crear un problema de restricciones
problem = Problem()

# Definir las variables y dominios
problem.addVariable('A', [1, 2, 3])
problem.addVariable('B', [4, 5, 6])

# Definir la restriccion
def restriccion(a, b):
    return a < b

problem.addConstraint(restriccion, ('A', 'B'))

# Encontrar la solucion
soluciones = problem.getSolutions()
print(soluciones)


