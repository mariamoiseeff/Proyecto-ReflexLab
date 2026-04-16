from src.carga_datos import cargar_datos
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import calcular_tiempo_reaccion_promedio
from src.metricas import calcular_tasa_error

ruta = "datos/ReflexLab_mock_data.csv"

# Cargar datos
try:
    datos_validos = cargar_datos(ruta)
except ValueError as e:
    print(f"Error al cargar datos: {e}")  
    datos_validos = None

if datos_validos is not None:

    try:
        id_participante = int(input("ID de participante: "))
        if id_participante <= 0:
            raise ValueError("El id del participante no puede ser negativo o cero")
    except ValueError as e:
        print(f"Error: {e}")
        id_participante = None

    if id_participante is not None:
        try:
            # Filtrar participante
            participante_pedido = filtrar_por_participante(datos_validos, id_participante)
        except ValueError as e:
            print (f"Error: {e}")
            participante_pedido = None
            
        if participante_pedido is not None:

            # Calcular promedio
           try:             
               promedio = calcular_tiempo_reaccion_promedio(participante_pedido)
               print(f"El promedio del participante es: {promedio} ms") 
           except ValueError as e:
               print (f"Error: {e}")    
              
            # Calcular tasa de error 
           try:                
                tasa_error = calcular_tasa_error(participante_pedido)
                print(f"La tasa de error del participante es: {tasa_error}%")

           except ValueError as e: 
                print(f"Error: {e}") 

