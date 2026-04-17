def validar_registro(registro):
    '''
    valida que los distintos datos sean validos en sus valores. 
    
    Parameters
    ----------
    registro : lista
        lista de str de valores ya parseados(separados) y convertidos al tipo de dato necesario. 

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
    id_part = registro[0]
    if id_part <= 0:
        raise ValueError("Error en funcion de validacion: El id del participante no puede ser un numero negativo")
    else: 
        datos_validados.append(id_part)
    
    #validar que trial sea un entero

    trial = registro[1]
    if trial <= 0: 
        raise ValueError("Error en funcion de validacion: Trial no puede ser un numero negativo")
    else: 
        datos_validados.append(trial)
    
    #validar estimulo solo go o no go y validar que sea str que pueda convertirse todo a minusculas
    
    estimulo = registro[2].lower()
    if estimulo not in ["go" , "nogo"]: 
        raise ValueError("Error en funcion de validacion: estimulo invalido. Solo puede ser 'go' o 'nogo'")
 
    else: 
        datos_validados.append(estimulo)
    
    #validar tiempo de inicio
   
    t_inicio = registro[3]
    if t_inicio < 0: 
        raise ValueError("Error en funcion de validacion: tiempo de inicio no puede ser negativo")
    else: 
        datos_validados.append(t_inicio)
    
    #validar respuesta tiene que ser solo True (si respondio) y False (si no respondio) -> ya se maneja en el parseo
    datos_validados.append(registro[4])
    
    #tiempo de reaccion
    t_reaccion = registro[5]
    if t_reaccion < 0: 
        raise ValueError("Error en funcion de validacion: tiempo de reaccion no puede ser negativo")
    else: 
        datos_validados.append(t_reaccion)

    #resultado_respuesta
    try: 
        resultado_respuesta = registro[6].lower()
    except: 
        raise ValueError("Error en funcion de validacion: resultado de respuesta tiene que poder convertirse en una palabra minusculas")
    if resultado_respuesta not in ["correcto", "incorrecto"]:
        raise ValueError("Error en funcion de validacion resultado: resultado de respuesta puede ser unicamente 'correcto' o 'incorrecto'")
    else:
        datos_validados.append(resultado_respuesta)

    # condicion
    try: 
        condicion = registro[7].lower()
    except: 
        raise ValueError("Error en funcion de validacion: resultado de respuesta tiene que poder convertirse en una palabra minusculas")
   
    if condicion not in ["alta_go" , "balanceada"]: 
        raise ValueError("Error en funcion de validacion: condicion experimental invalida, puede ser unicamente 'alta_go' o 'balanceada' ")
    else: 
        datos_validados.append(condicion)

    #si todo salio bien, todos los datos validos, se devuelven. sino, se corta la funcion
    return datos_validados


