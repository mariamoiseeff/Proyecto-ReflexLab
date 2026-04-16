#metricas
def calcular_tiempo_reaccion_promedio(registro_participante):    
   '''
    promedio de tiempos de reaccion de todos los participantes
    
    Parameters
    ----------
    registro_participante : dicc
        diccionario con los datos de un participante previamente elegido.

    Returns
    -------
    float
        promedio: suma de todos los tiempos de reaccion dividido la cantidad.
        
    Raises: 
        ValueError si la lista de tiempos de reaccion dentro del registro_participante esta vacia
    '''
   
   tiempos_reaccion = registro_participante["tiempo_reaccion"]
   if len(tiempos_reaccion) == 0: 
        raise ValueError ("Error, lista vacia. No se puede calcular el promedio")
        
   promedio = sum(tiempos_reaccion) / len(tiempos_reaccion)
   return promedio
             
        
def calcular_tasa_error(registro_participante):
    '''
    calcula  proporción de respuestas incorrectas

    Parameters
    ----------
    registro_participante : dicc
        diccionario con los datos de un participante previamente elegido.

    Returns
    -------
    float
        resultado de division de respuestas incorrectas / respuestas totales.
    
    Raises: 
        ValueError si la lista de respuestas esta vacia.

    '''
     
    cantidad_total = len(registro_participante["resultado_respuesta"])
    if cantidad_total == 0:
        raise ValueError("Error, lista de respuestas vacias. No se puede calcular tasa de error")
    
    cantidad_incorrectas = 0
    
    for respuesta in registro_participante["resultado_respuesta"]:
        if respuesta == "incorrecto":
            cantidad_incorrectas += 1
        
    tasa_error = cantidad_incorrectas / cantidad_total 
    return tasa_error 
            
            
            
             

            
            
            
            
            
            
            
            
            
            