def cargar_datos(registro):
    '''
    abrir el archivo, convierte archico en un dataframe
    
    Parameters
    ----------
    ruta : str
        ruta que lleva y abre un archivo con datos. 

    Returns
    -------
    dataframe
        dataframe de informacion validada y agrupada por participantes

    '''
    
    columnas = list(registro.columns)
    columnas[0] = "id_participante"
    columnas[1] = "trial"
    columnas[2] = "estimulo"
    columnas[3] = "t_inicio"
    columnas[4] = "respuesta"
    columnas[5] = "tiempo_reaccion"
    columnas[6] = "resultado_respuesta"
    columnas[7] = "condicion"
    registro.columns = columnas 
  
                       
    from src.validacion_datos import validar_registro
    
    registro_validado = validar_registro(registro)
    
    registro_validado_etiquetado = registro_validado.set_index('id_participante')
            
    return registro_validado_etiquetado
