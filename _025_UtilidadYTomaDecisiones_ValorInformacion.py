class ValorInformacion:
    def __init__(self, probabilidad_informacion, utilidad_informacion):
        """
        Inicializa el Valor de la Informacion.

        Args:
            probabilidad_informacion (float): La probabilidad de que la informacion sea correcta.
            utilidad_informacion (float): La utilidad asociada a la informacion.
        """
        self.probabilidad_informacion = probabilidad_informacion
        self.utilidad_informacion = utilidad_informacion

    def calcular_valor(self):
        """
        Calcula el Valor de la Informacion como el producto de la probabilidad y la utilidad.

        Returns:
            float: El Valor de la Informacion.
        """
        return self.probabilidad_informacion * self.utilidad_informacion


# Crear una instancia de Valor de la Informacion
valor_info = ValorInformacion(0.8, 10.0)

# Calcular y mostrar el Valor de la Informacion
valor = valor_info.calcular_valor()
print("El Valor de la Informacion es:", valor)

