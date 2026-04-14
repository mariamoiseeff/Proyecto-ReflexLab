def parsear_linea(linea):
    '''
    

    Parameters
    ----------
    linea : str
        linea que va a ser recorrida

    Returns
    -------
    list
        lista de str con datos separados
    '''
    
    partes = linea.strip().split(",")
    
    
    return[partes[0], 
           partes[1], 
           partes[2], 
           partes[3], 
           partes[4], 
           partes[5], 
           partes[6], 
           partes[7]]
   
    
def cargar_datos(ruta_archivo):
    '''
    abrir el archivo, recorrer las líneas, aplicar parseo, generar diccionario por participante, devolver lista de registros de participantes
    
    Parameters
    ----------
    ruta : str
        ruta que recorre

    Returns
    -------
    list
        registro de diccionrios de participantes

    '''
    
    registros_participantes = {}
  
    with open (ruta_archivo, "r") as archivo:
        for linea in archivo:
            parseo = parsear_linea(linea)
            print(parseo)
           
            #si encontro dato invalido, no tomarlo en cuenta, volver al ciclo for a ver la siguiente linea: 
            
            from src.validacion_datos import validar_registro
            try: 
                parseo_validado = validar_registro(parseo)
            except ValueError: 
                print("error en la carga de datos porque hay datos invalidos en esta linea, entonces se descarta.")
                continue
            
            id_part = parseo[0]
            
            if id_part not in registros_participantes:
                registros_participantes[id_part] = {"id_participante": id_part,
                                                     "trial":[parseo_validado[1]], 
                                                     "estimulo": [parseo_validado[2]], 
                                                     "t_inicio": [parseo_validado[3]], 
                                                     "respuesta": [parseo_validado[4]], 
                                                     "tiempo_reaccion": [parseo_validado[5]], 
                                                     "resultado_respuesta": [parseo_validado[6]], 
                                                     "condicion": [parseo_validado[7]]}
            else:
                registros_participantes[id_part]["trial"].append(parseo_validado[1]) 
                registros_participantes[id_part]["estimulo"].append(parseo_validado[2])
                registros_participantes[id_part]["t_inicio"].append(parseo_validado[3])
                registros_participantes[id_part]["respuesta"].append(parseo_validado[4])
                registros_participantes[id_part]["tiempo_reaccion"].append(parseo_validado[5])
                registros_participantes[id_part]["resultado_respuesta"].append(parseo_validado[6])
                registros_participantes[id_part]["condicion"].append(parseo_validado[7])
    
    registros = list(registros_participantes.values())
    return registros

#comentario: cambiaria el codigo para que vaya haciendo lista segun los trials y de todos los campos por participante