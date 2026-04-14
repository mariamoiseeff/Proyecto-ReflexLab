from src.carga_datos import cargar_datos
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import calcular_tiempo_reaccion_promedio
from src.metricas import calcular_tasa_error

ruta = "datos/ReflexLab_mock_data.csv"
datos_validos = cargar_datos(ruta)

id_participante = input("ID de participante: ")
participante_pedido = filtrar_por_participante(datos_validos, id_participante)
print(participante_pedido)        

promedio_id_participante = calcular_tiempo_reaccion_promedio(datos_validos, id_participante)
print(f"El promedio del participante es: {promedio_id_participante}")

tasa_error_id_participante = calcular_tasa_error(datos_validos, id_participante)
print(f"La tasa de error del participante es: {tasa_error_id_participante}")

