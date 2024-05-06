import random

class POMDP_AdivinarNumero:
    def __init__(self, min_num, max_num):
        self.min_num = min_num
        self.max_num = max_num
        self.estado = None

    def iniciar_juego(self):
        self.estado = random.randint(self.min_num, self.max_num)
        print(f"El numero a adivinar esta entre {self.min_num} y {self.max_num}.")

    def realizar_accion(self, suposicion):
        observacion = abs(suposicion - self.estado)  # Observamos la distancia entre la suposicion y el numero real
        return observacion

# Crear una instancia del juego
juego_adivinar_numero = POMDP_AdivinarNumero(1, 768)

# Iniciar el juego
juego_adivinar_numero.iniciar_juego()

# Suposicion del jugador
suposicion_jugador = int(input("Haz una suposicion: "))

# Realizar la accion y obtener la observacion
observacion = juego_adivinar_numero.realizar_accion(suposicion_jugador)

# Mostrar la observacion al jugador
print(f"Tu observacion es: {observacion}")

