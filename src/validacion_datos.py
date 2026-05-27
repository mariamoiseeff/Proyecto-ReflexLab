def validar_registro(df):
    '''
    valida que los distintos datos sean validos en sus valores por columna. 
    
    Parameters
    ----------
    df : dataframe 
        dataframe de todos los datos
    
    Raises
    ------
        ValueError si hay algun dato invalido

    '''
    
    #validar id_participante
    if (df["id_participante"] < 0): 
        raise ValueError("Error en funcion de validacion: El id del participante no puede ser un numero negativo")
    
    #validar que trial sea un entero
    if (df["trial"] < 0): 
        raise ValueError("Error en funcion de validacion: Trial no puede ser un numero negativo")
    
    #validar estimulo solo go o no go y validar que sea str que pueda convertirse todo a minusculas

    if (df["estimulo"] not in ["go" , "nogo"]): 
        raise ValueError("Error en funcion de validacion: estimulo invalido. Solo puede ser 'go' o 'nogo'")
 
    #validar tiempo de inicio

    if (df["t_inicio"] < 0): 
        raise ValueError("Error en funcion de validacion: tiempo de inicio no puede ser negativo")

    
    #validar respuesta tiene que ser solo True (si respondio) y False (si no respondio) -> ya se maneja en el parseo
    if (df["respuesta"].dtype!= bool): 
        raise ValueError("Error en funcion de validacion: el dato no es booleano")
    
    #tiempo de reaccion
    if (df[" t_reaccion"] < 0): 
        raise ValueError("Error en funcion de validacion: tiempo de reaccion no puede ser negativo")

    #resultado_respuesta
    if (df["resultado_respuesta"] not in ["correcto", "incorrecto"]):
        raise ValueError("Error en funcion de validacion resultado: resultado de respuesta puede ser unicamente 'correcto' o 'incorrecto'")
   
    # condicion
    if (df["condicion"] not in ["alta_go" , "balanceada"]): 
        raise ValueError("Error en funcion de validacion: condicion experimental invalida, puede ser unicamente 'alta_go' o 'balanceada' ")


