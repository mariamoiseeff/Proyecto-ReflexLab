from src.carga_datos import cargar_datos
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import calcular_tiempo_reaccion_promedio
from src.metricas import calcular_tasa_error

ruta = "datos/ReflexLab_mock_data.csv"
datos_validos = cargar_datos(ruta) #nose si tenemos que usar try-except aca porque tenemos un try-expect dentro de carga datos que corresponde a la validacion

try:
    id_participante = int(input("ID de participante: ")) #tenemos que validar que el id sea valido?
    if id_participante <= 0:
        raise ValueError("El id del participante no puede ser negativo ")
except:
    raise ValueError("El id es invalido")
else:
    participante_pedido = filtrar_por_participante(datos_validos, id_participante)
    print(participante_pedido)        

#haria bloque try-except porque vamos a manejar errores dentro del promedio

promedio_id_participante = calcular_tiempo_reaccion_promedio(datos_validos, id_participante)
 #cambiaria para que el argumento de estas funciones sea participante_pedido
print(f"El promedio del participante es: {promedio_id_participante}") 

#otro bloque try-except poruqe vamos a manejar errorer dentro de calcular tasa error
tasa_error_id_participante = calcular_tasa_error(datos_validos, id_participante)
#cambiaria para que el argumento de estas funciones sea participante_pedido
print(f"La tasa de error del participante es: {tasa_error_id_participante}")

