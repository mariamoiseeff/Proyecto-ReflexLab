#procesamiento datos
def filtrar_por_participante(datos, id_participante):
    '''
    seleccionar los datos correspondientes a un participante y lo devuelve

    Parameters
    ----------
    datos : list
        lista de diccionarios de todos los datos parseados.
    id_participante : int
        numero de participante.

    Returns
    -------
    diccionario con todos los datos de un participante
    
    '''
    for registro_participate in datos: #me agarra un diccionario a la vez
        if id_participante == registro_participate["id_participante"]: 
            return registro_participate
    return None