
def calcular_datos_transmitidos(velocidad, tiempo):
    return velocidad * tiempo

velocidad = 100


for tiempo in range(0, 1001, 100):  
    datos_transmitidos = calcular_datos_transmitidos(velocidad, tiempo)
    print(f"Datos transmitidos en {tiempo} segundos: {datos_transmitidos} megabits")
