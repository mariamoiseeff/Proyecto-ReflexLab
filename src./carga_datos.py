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
    
    return[int(partes[0]), 
           int(partes[1]), 
           partes[2], 
           float(partes[3]), 
           int(partes[4]), 
           float(partes[5]), 
           partes[6], 
           partes[7]]

#comentario: tendria que devolver lista de str pero sin conversion,porque eso lo va a hacer la de validar
#borarria el return de la lista con las conversiones para que solo return partes
   
    
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
    with open ("datos.csv", "r") as archivo:
        for linea in archivo:
            parseo = parsear_linea(linea)
            #comentario: agregar funcion de validacion, hay que abrir archivo de validacion??: 
            #comentario: parseo_validado = validar_registro(parseo) --> cambiar todo a parseo validado, o igualar funcion de validacion a parseo y cambair nombre de variable de la de arriba
            
            #si encontro dato invalido, no tomarlo en cuenta, volver al ciclo for a ver la siguiente linea: 
            #if parseo_validado == None: 
                #continue
            
            
            id_part = parseo[0]
            
            if id_part not in registros_participantes:
                registros_participantes[id_part] = {"id_participante": id_part,
                                                     "trial":[parseo[1]], 
                                                     "estimulo": [parseo[2]], 
                                                     "t_inicio": [parseo[3]], 
                                                     "respuesta": [parseo[4]], 
                                                     "tiempo_reaccion": [parseo[5]], 
                                                     "resultado_respuesta": [parseo[6]], 
                                                     "condicion": [parseo[7]]}
            else:
                registros_participantes[id_part]["trial"].append(parseo[1]) 
                registros_participantes[id_part]["estimulo"].append(parseo[2])
                registros_participantes[id_part]["t_inicio"].append(parseo[3])
                registros_participantes[id_part]["respuesta"].append(parseo[4])
                registros_participantes[id_part]["tiempo_reaccion"].append(parseo[5])
                registros_participantes[id_part]["resultado_respuesta"].append(parseo[6])
                registros_participantes[id_part]["condicion"].append(parseo[7])
    
    return list(registros_participantes.values())

#comentario: cambiaria el codigo para que vaya haciendo lista segun los trials y de todos los campos por participante