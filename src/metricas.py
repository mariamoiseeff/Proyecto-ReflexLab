#metricas
def calcular_tiempo_reaccion_promedio(datos):    
   '''
    promedio de tiempos de reaccion de todos los participantes
    
    Parameters
    ----------
    datos: df
        df con los datos de todos los participantes

    Returns
    -------
    dataframe
        promedios de los tiempos de reaccion de todos los partiicpantes (2 columnas)
   
    '''
   
   tiempos_promedios = datos.groupby("id_participante")["tiempo_reaccion"].mean().reset_index()
   return tiempos_promedios
             
        
def calcular_tasa_error(datos):
    '''
    calcula  proporción de respuestas incorrectas de todos los participantes

    Parameters
    ----------
    datos : df
        df con los datos de todos los participantes

    Returns
    -------
    df
        resultado de division de respuestas incorrectas / respuestas totales de todos los participantes

    '''
    
    datos['es_incorrecta'] = datos["resultado_respuesta"] == 'incorrecto'
    tasa_por_participante = datos.groupby('id_participante')['es_incorrecta'].mean().mul(100).reset_index(name = "tasa_error")

    
    return  tasa_por_participante

    
            
            
             

            
            
            
            
            
            
            
            
            
            