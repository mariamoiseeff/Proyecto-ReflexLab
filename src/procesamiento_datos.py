def filtrar_por_participante(datos, id_participante):
    '''
    seleccionar los datos correspondientes a un participante y lo devuelve

    Parameters
    ----------
    datos : dataframe
        dataframe con datos validos.
    id_participante : int
        numero de participante.

    Returns
    -------
    serie: 
        sereie con todos los datos de un participante
    
    Raises: 
        ValueError si ID ingresado es negativo o si no se encuentra dentro de los posibles ID.
        ValueError si la base de datos esta vacia. 
        ValueError si el ID no esta en la base de datos. 
    
    '''
    if id_participante <= 0:
        raise ValueError("Error en funcion cargar datos: El id del participante no puede ser negativo ")
    if datos.empty: 
        raise ValueError("Error en funcion cargar datos: la base de datos esta vacia. ")
    if id_participante not in list(datos["id_participante"]):
        raise ValueError("Error en funcion cargar datos: El id del participante no se encuentra en la base de datos")
    
    filtro_participante = datos[datos["id_participante"] == id_participante]
    
    return filtro_participante 