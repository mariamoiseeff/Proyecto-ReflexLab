from src.carga_datos import cargar_datos
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import calcular_tiempo_reaccion_promedio
from src.metricas import calcular_tasa_error


datos_validos = cargar_datos("datos.csv")

id_participante = input("ID de participante: ")
participante_pedido = filtrar_por_participante(datos_validos, id_participante)
print(participante_pedido)        

promedio_general = calcular_tiempo_reaccion_promedio(datos_validos)
print(f"El promedio general es: {promedio_general}")

tasa_error_general = calcular_tasa_error(datos_validos)
print(f"La tasa de error general es: {tasa_error_general}")
