class NodoRBD:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del nodo
        self.valor = None  # Valor del nodo

    def set_valor(self, valor):
        self.valor = valor  # Metodo para establecer el valor del nodo

class RedBayesianaDinamica:
    def __init__(self):
        self.nodos = {}  # Diccionario para almacenar los nodos de la red

    def agregar_nodo(self, nombre):
        if nombre not in self.nodos:
            nuevo_nodo = NodoRBD(nombre)  # Crear un nuevo nodo
            self.nodos[nombre] = nuevo_nodo  # Agregar el nodo al diccionario
        else:
            print("El nodo ya existe en la red.")

    def conectar_nodos(self, nodo_padre, nodo_hijo):
        if nodo_padre in self.nodos and nodo_hijo in self.nodos:
            self.nodos[nodo_hijo].padre = self.nodos[nodo_padre]  # Establecer el nodo padre del nodo hijo
        else:
            print("Uno o ambos nodos no existen en la red.")

    def establecer_valor(self, nombre, valor):
        if nombre in self.nodos:
            self.nodos[nombre].set_valor(valor)  # Establecer el valor de un nodo existente
        else:
            print("El nodo no existe en la red.")

# Crear una instancia de la Red Bayesiana Dinamica
red_bayesiana = RedBayesianaDinamica()

# Agregar nodos a la red
red_bayesiana.agregar_nodo('Lluvia')
red_bayesiana.agregar_nodo('Riego')
red_bayesiana.agregar_nodo('Cesped')

# Conectar nodos en la red
red_bayesiana.conectar_nodos('Lluvia', 'Cesped')
red_bayesiana.conectar_nodos('Riego', 'Cesped')

# Establecer valores para algunos nodos
red_bayesiana.establecer_valor('Lluvia', True)
red_bayesiana.establecer_valor('Riego', False)

# Imprimir los valores de los nodos
for nombre, nodo in red_bayesiana.nodos.items():
    print(f"Valor del nodo {nombre}: {nodo.valor}")

