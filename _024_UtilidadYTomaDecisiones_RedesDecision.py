class NodoDecision:
    def __init__(self, nombre, utilidad):
        """
        Inicializa un nodo de decision.

        Args:
            nombre (str): El nombre del nodo.
            utilidad (float): La utilidad asociada a la decision.
        """
        self.nombre = nombre
        self.utilidad = utilidad
        self.opciones = []

    def agregar_opcion(self, opcion):
        """
        Agrega una opcion a la decision.

        Args:
            opcion (Opcion): La opcion a agregar.
        """
        self.opciones.append(opcion)

    def evaluar(self):
        """
        Evalua la utilidad de cada opcion y devuelve la mejor opcion.
        
        Returns:
            Opcion: La mejor opcion.
        """
        mejor_opcion = None
        mejor_utilidad = float('-inf')
        for opcion in self.opciones:
            utilidad_opcion = opcion.evaluar()
            if utilidad_opcion > mejor_utilidad:
                mejor_utilidad = utilidad_opcion
                mejor_opcion = opcion
        return mejor_opcion


class Opcion:
    def __init__(self, nombre, utilidad):
        """
        Inicializa una opcion de decision.

        Args:
            nombre (str): El nombre de la opcion.
            utilidad (float): La utilidad asociada a la opcion.
        """
        self.nombre = nombre
        self.utilidad = utilidad

    def evaluar(self):
        """
        Devuelve la utilidad asociada a la opcion.

        Returns:
            float: La utilidad de la opcion.
        """
        return self.utilidad


# Crear los nodos de decision
comprar_nodo = NodoDecision("Comprar", 5.0)
no_comprar_nodo = NodoDecision("No comprar", 0.0)

# Crear las opciones para el nodo "Comprar"
comprar_opcion1 = Opcion("Comprar barato", 8.0)
comprar_opcion2 = Opcion("Comprar caro", 3.0)
comprar_nodo.agregar_opcion(comprar_opcion1)
comprar_nodo.agregar_opcion(comprar_opcion2)

# Crear las opciones para el nodo "No comprar"
no_comprar_opcion = Opcion("No comprar", 0.0)
no_comprar_nodo.agregar_opcion(no_comprar_opcion)

# Evaluar las opciones y tomar la mejor decision
mejor_decision = comprar_nodo.evaluar()
print("La mejor decision es:", mejor_decision.nombre)

