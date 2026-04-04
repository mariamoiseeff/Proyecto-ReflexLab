#metricas
def calcular_tiempo_reaccion_promedio(datos): 
    
   '''
    promedio de tiempos de reaccion de todos los participantes
    

    Parameters
    ----------
    datos : list
        lista de diccionarios de los datos de todos los participantes .

    Returns
    -------
    float
        promedio: suma de todos los tiempos de reaccion dividido la cantidad.
    '''
    promedios_tiempos_reaccion = []
    for registro_participante in datos: #me agarra diccionarios de registro de un participante
        tiempos_reaccion = registro_participante["tiempo de reaccion"]
        promedio = sum(tiempos_reaccion) / len(tiempos_reaccion)
        promedios_tiempos_reaccion.append(promedio)
    
    promedio_todos = sum(promedios_tiempos_reaccion) / len(promedios_tiempos_reaccion)
    return promedio_todos
        
    
    
def calcular_tasa_error(datos: list) -> float:
    '''
    calcula  proporción de respuestas incorrectas

    Parameters
    ----------
    datos : list
        lista de diccionarios de los datos de respuestas de los participantes.

    Returns
    -------
    float
        resultado de division de respuestas incorrectas / respuestas totales.

    '''