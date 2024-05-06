import time  # Importa el modulo time para medir el tiempo de espera

def busqueda_en_linea(dato_a_buscar, fuente_de_datos):  
    """
    Realiza una busqueda en linea para encontrar un dato en una fuente de datos en tiempo real.

    Args:
        dato_a_buscar: El dato que se desea encontrar.
        fuente_de_datos: Generador o fuente de datos en tiempo real.

    Returns:
        bool: True si el dato se encuentra, False de lo contrario.
    """
    for dato in fuente_de_datos:  # Itera sobre los datos en tiempo real
        if dato == dato_a_buscar:  # Comprueba si el dato actual coincide con el dato buscado
            return True  # Retorna True si se encuentra el dato
        time.sleep(0.1)  # Espera un breve periodo de tiempo antes de revisar el siguiente dato
    return False  # Retorna False si el dato no se encuentra despues de recorrer todos los datos

# Generador de datos en tiempo real (simulado)
def fuente_de_datos():
    for dato in range(10):  # Simula la generacion de datos del 0 al 9
        yield dato  # Retorna cada dato generado uno por uno

# Dato que se desea buscar
dato_a_buscar = 5

# Realiza la busqueda en linea en la fuente de datos simulada
print("Iniciando busqueda en linea...")
resultado = busqueda_en_linea(dato_a_buscar, fuente_de_datos())

# Imprime el resultado de la busqueda
if resultado:
    print(f"El dato {dato_a_buscar} se encontro en la fuente de datos.")
else:
    print(f"El dato {dato_a_buscar} no se encontro en la fuente de datos.")

