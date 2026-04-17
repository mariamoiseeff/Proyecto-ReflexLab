def parsear_linea(linea):
    '''
    

    Parameters
    ----------
    linea : str
        linea que va a ser recorrida

    Returns
    -------
    list
        lista de datos separados y convertidos 
    '''
    
    if len(linea) == 0:
        raise ValueError("Error en funcion parseo: La linea esta vacia")
    
    partes = linea.strip().split(",")
    if len(partes) != 8:
        raise ValueError("Error en funcion parseo: Faltan columnas en la linea")
    try: 
        id_part = int(partes[0])
    except:
        raise TypeError("Error en funcion parseo: El id tiene que ser un numero entero")
    
    try: 
        trial = int(partes[1])
    except: 
        raise TypeError("Error en funcion parseo: El trial tiene que ser un numero entero")
        
    try:
        estimulo = str(partes[2])
    except:
        raise TypeError("Error en funcion parseo: El estimulo tiene que ser un string")
    
    try: 
        t_inicio = float(partes[3])
    except:
        raise TypeError("Error en funcion parseo: El timepo de inicuio tiene que ser un float")

    respuesta = partes[4] 
    if respuesta == "True":
        respuesta = True 
    elif respuesta == "False":
        respuesta = False
    else:
        raise TypeError("Error en funcion parseo: La respuesta tiene que ser True o False")
    
    try:
        t_reaccion = float(partes[5])
    except: TypeError("Error en funcion parseo: El tiempo de reaccion tiene que ser un float")
    
    try: 
        resultado_respuesta = str(partes[6])
    except: TypeError("Error en funcion parseo: El resultado de respuesta tiene que ser un string")
    
    try:
        condicion = str(partes[7])
    except: TypeError("Error en funcion parseo: La condicion tiene que ser un string") 
    
    return[id_part, 
           trial, 
           estimulo, 
           t_inicio, 
           respuesta, 
           t_reaccion, 
           resultado_respuesta, 
           condicion]
   
    
def cargar_datos(ruta_archivo):
    '''
    abrir el archivo, recorrer las líneas, aplicar parseo, generar diccionario por participante, 
    devolver lista de registros de participantes
    
    Parameters
    ----------
    ruta : str
        ruta que lleva y abre un archivo con datos. 

    Returns
    -------
    list
        registro de diccionrios de participantes

    '''
    
    registros_participantes = {}
  
    with open (ruta_archivo, "r") as archivo:
        for linea in archivo:
            
            try: 
                parseo = parsear_linea(linea)
            except TypeError as e:
                print(f"Esta linea se descarta: {e}")
                continue
                       
            from src.validacion_datos import validar_registro
            try: 
                parseo_validado = validar_registro(parseo)
            except ValueError as e: 
                print(e)
                print("error en la carga de datos porque hay datos invalidos en esta linea, entonces se descarta.")
                continue
            
            id_part = int(parseo_validado[0])
            
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
