#procesamiento datos
def filtrar_por_participante(datos, id_participante):
    '''
    seleccionar los datos correspondientes a un participante y lo devuelve

    Parameters
    ----------
    datos : list
        lista de diccionarios de todos los datos validados y agrupados.
    id_participante : int
        numero de participante.

    Returns
    -------
    dicc: 
        diccionario con todos los datos de un participante
    
    Raises: 
        ValueError si ID ingresado es negativo o si no se encuentra dentro de los posibles ID.
        ValueError si la lista de la base de datos esta vacia. 
    
    '''
    if id_participante <= 0:
        raise ValueError("Error en funcion cargar datos: El id del participante no puede ser negativo ")
    if len(datos) == 0: 
        raise ValueError("Error en funcion cargar datos: la base de datos esta vacia. ")
    
    posibles_id = []
    
    for registro_participante in datos: #me agarra un diccionario a la vez
        posibles_id.append(registro_participante["id_participante"])
        if id_participante == registro_participante["id_participante"]: 
            return registro_participante
  
    if id_participante not in posibles_id: 
        raise ValueError("Error en funcion cargar datos: ID no se encuentra dentro de los ID registrados")