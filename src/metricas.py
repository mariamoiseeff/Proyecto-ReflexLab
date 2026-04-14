#metricas
def calcular_tiempo_reaccion_promedio(datos,id_buscado): 
    
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
   for registro_participante in datos:
        if registro_participante["id"] == id_buscado:
            
            tiempos_reaccion = registro_participante["tiempo de reaccion"]
            promedio = sum(tiempos_reaccion) / len(tiempos_reaccion)
            
            return promedio
    
   return 0           
        
def calcular_tasa_error(datos,id_buscado):
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
     
    cantidad_incorrectas = 0
    cantidad_total = 0

    for registro in datos:
        if registro["id"] == id_buscado:
            
            cantidad_total += 1
            
            if registro["resultado_respuesta"] == "incorrecto":
                cantidad_incorrectas += 1

    if cantidad_total == 0:
        return 0

    tasa_error = cantidad_incorrectas / cantidad_total
    return tasa_error 
            
            
            
             

            
            
            
            
            
            
            
            
            
            