import os
os.system("cls")
def calcular_datos_transmitidos(velocidad_mbps, tiempo_segundos):
    
    datos_transmitidos = velocidad_mbps * tiempo_segundos
    return datos_transmitidos

velocidad = 100


tiempo_45_segundos = 45
tiempo_1_5_minutos = 1.5 * 60  
tiempo_1_hora = 60 * 60  


datos_45_segundos = calcular_datos_transmitidos(velocidad, tiempo_45_segundos)
datos_1_5_minutos = calcular_datos_transmitidos(velocidad, tiempo_1_5_minutos)
datos_1_hora = calcular_datos_transmitidos(velocidad, tiempo_1_hora)


print(f"Datos transmitidos en 45 segundos: {datos_45_segundos} megabits")
print(f"Datos transmitidos en 1.5 minutos: {datos_1_5_minutos} megabits")
print(f"Datos transmitidos en 1 hora: {datos_1_hora} megabits")
