def comprobacion_hacia_adelante(CSP, asignacion_actual={}):
   
    CSP_modificado = CSP.copy()  # Copia el CSP original para no modificarlo directamente

    for variable, valor in asignacion_actual.items():  # Itera sobre las asignaciones actuales
        for var_restringida, restricciones in CSP.get(variable, []):  # Itera sobre las restricciones de la variable
            dominio_restringido = CSP_modificado.get(var_restringida, [])  # Obtiene el dominio restringido de la variable restringida
            dominio_restringido = [v for v in dominio_restringido if all(r(asignacion_actual.get(var_restringida), v) for r in restricciones)]  # Aplica las restricciones al dominio
            CSP_modificado[var_restringida] = dominio_restringido  # Actualiza el dominio restringido en el CSP modificado

    return CSP_modificado  # Retorna el CSP modificado despues de la comprobacion hacia adelante

# Ejemplo de CSP: Mapa de colores de paises adyacentes
CSP = {
    'Francia': [('Portugal', [lambda x, y: x != y])],  # Restriccion: Francia no puede tener el mismo color que Portugal
    'Portugal': [('Francia', [lambda x, y: x != y])],  # Restriccion: Portugal no puede tener el mismo color que Francia
    'Italia': [('Francia', [lambda x, y: x != y])],    # Restriccion: Italia no puede tener el mismo color que Francia
    'Andorra': [],  # Sin restricciones
    'Suiza': [('Alemania', [lambda x, y: x != y])],    # Restriccion: Suiza no puede tener el mismo color que Alemania
    'Alemania': [('Suiza', [lambda x, y: x != y])]     # Restriccion: Alemania no puede tener el mismo color que Suiza
}

# Asignacion actual
asignacion_actual = {'Francia': 'Rojo'}

# Aplicar la comprobacion hacia adelante
CSP_modificado = comprobacion_hacia_adelante(CSP, asignacion_actual)

# Imprimir el CSP modificado despues de la comprobacion hacia adelante
print("CSP modificado despues de la comprobacion hacia adelante:")
print(CSP_modificado)
