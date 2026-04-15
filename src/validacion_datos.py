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
    
    Raises
    ------
    ValueError si hay algun dato invalido

    '''
    datos_validados = []
    
    #validar id_participante
    #tengo que validar que el id exista, nose como hacerlo todavia
    try: 
        id_part = int(registro[0])
        if id_part <= 0:
            raise ValueError("El id del participante no puede ser un numero negativo")
    except: 
        raise ValueError("El id del participante es invalido")
    else: 
        datos_validados.append(id_part)
    
    #validar que trial sea un entero
    try: 
        trial = int(registro[1])
        if trial <= 0: 
            raise ValueError("Trial no puede ser un numero negativo")
    except: 
        raise ValueError("Trial tiene que ser un entero")
    else: 
        datos_validados.append(trial)
    
    #validar estimulo solo go o no go y validar que sea str que pueda convertirse todo a minusculas
    try: 
        estimulo = registro[2].lower()
        if estimulo not in ["go" , "nogo"]: 
            raise ValueError("estimulo invalido")
    except: 
        raise ValueError("estimulo invalido")
    
    else: 
        datos_validados.append(estimulo)
    
    
    #validar tiempo de inicio
    try: 
        t_inicio = float(registro[3])
        if t_inicio < 0: 
            raise ValueError("tiempo de inicio no puede ser negativo")
    except: 
        raise ValueError("tiempo de inicio invalido")
    else: 
        datos_validados.append(t_inicio)
    
    
    #validar respuesta tiene que ser solo True (si respondio) y False (si no respondio)

    if registro[4] == "True": 
        datos_validados.append(True)
    elif registro[4] == "False":
        datos_validados.append(False)
    else:
        raise ValueError("respuesta invalida, debe ser True o False unicamente")
    
    #tiempo de reaccion
    try:
        t_reaccion = float(registro[5])
        if t_reaccion < 0: 
            raise ValueError("tiempo de reaccion no puede ser negativo")
    except:
        raise ValueError("tiempo de reaccion invalido")
    else: 
        datos_validados.append(t_reaccion)


    #resultado_respuesta
    try: 
        resultado_respuesta = registro[6].lower()
        if resultado_respuesta not in ["correcto", "incorrecto"]:
            raise ValueError("resultado invalido: puede ser unicamente 'correcto' o 'incorrecto'")
    except: 
        raise ValueError("resultado invalido")
    else:
        datos_validados.append(resultado_respuesta)

    # condicion
    try:
        condicion = registro[7].lower()
        if condicion not in ["alta_go" , "balanceada"]: 
            raise ValueError("condicion invalida, puede ser unicamente 'alta_go' o 'balanceada' ")
    except: 
        raise ValueError("condicion invalida")
    else: 
        datos_validados.append(condicion)

    #si todo salio bien, todos los datos validos, se devuelven. sino, se corta la funcion
    return datos_validados
