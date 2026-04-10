def validar_registro(registro):
    '''
    valida que las distintas partes sean el tipo de dato necesario para poder hacer el analisis y las convierte, 
    descartando los datos que no corresponden. 
    
    Parameters
    ----------
    registro : lista
    lista de str de valores ya parseados(separados)
    

    Returns
    -------
    lista
    lista de valores verificados separados en sus categorias

    '''
    datos_validados = []
    #validar id_participante
    
    if registro[0].isdigit(): 
        datos_validados.append(int(registro[0]))
    else: 
        return None
    
    #validar que trial sea un entero
    
    if registro[1].isdigit():
        datos_validados.append(int(registro[1]))
    else: 
        return None
    
    #validar estimulo solo go o no go
    estimulo = registro[2].lower()
    if estimulo in ["go" , "nogo"]: 
        datos_validados.append(estimulo)
    else: 
        return None
    
    #validar tiempo de inicio
    try: 
        datos_validados.append(float(registro[3]))
    except: 
        return None
    
    #validar respuesta tiene que ser un entero
    if registro[4].isdigit(): 
        datos_validados.append(int(registro[4]))
    else:
        return None
    
    #tiempo de reaccion
    try:
        datos_validados.append(float(registro[5]))
    except:
        return None

    # resultado
    resultado = registro[6].lower()
    if resultado in ["correcto", "incorrecto"]:
        datos_validados.append(resultado)
    else:
        return None

    # condicion
    condicion = registro[7].lower()
    if condicion in ["alta_go" , "balanceada"]: 
        datos_validados.append(condicion)
    else: 
        datos_validados.append(condicion)
        return None

    return datos_validados
