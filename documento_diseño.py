'''
objetivo del programa:  
- Analizar datos de una tarea Go/NoGo para estudiar los tiempo de reaccion y las respuestas de los participantes, generando metricas que nos permiten evaluar el resultado
- el proyecto incluye, modulos para cargar, validar, procesar y validar datos. Un archivo pricipal y una carpeta con los datos y diagramas del sistema.

inputs: 
- ruta de un csv con datos de un experimento
- ID de participante para despues ver las metricas de ese participante

outputs: 
- datos filtrados del participante pedido
- promedio de los tiempos de reaccion de todos los participantes (Dataframe)
- tasa de error de todos los participantes (dataframe)
- Graficos

procesos principales: 
- cargar los datos del csv
- validar los datos 
- filtrar datos de un participante
- generar metricas de los participantes
- generar graficos

estructuras de datos: 
- guardamos los datos de todos los participantes con todas las partes de experimento en un dataframe. 
    - tiene 8 columnas (id_participante, trial, estimulo (go - nogo), tiempo de inicio, respuesta (true - false), tiempo de reaccion, resultado de la respuesta (correcto - incorrecto), condicion (alta go - balanceada))
    - las filas dependen de la cantidad de informacion que tenga el csv
    
modulos / funciones + errores: 
- Main: codifo principal -> importa los archivos, carga los datos, y llama a las funciones principales
    - ataja los errores posibles de las funciones con try/except
- Validacion: funcion validar_registro(df) --> df valido. valida que los distintos datos sean validos en sus valores por columna. 
    - Errores Posibles: ValueError si hay algun dato invalido
        - id_participante >= 0
        - trial >= 0
        - estimulo solo puede ser "go"-"nogo"
        - t_inicio >= 0
        - respuesta: dato booleano True - False
        - t_reaccion >= 0
        - resultado_respuesta solo puede ser "correcto"-"incorrecto
        - condiction solo puede ser "balanceada" - "alta go"
- Carga Datos: 
    -cargar_datos(registro) --> dataframe
        abrir el archivo, convierte en un dataframe con nombre de las columnas correctos y etiqueta como el ID, llama a validacion
        errores: si el archivo no es valido, si la ruta no existe o no lleva a un archivo  
        
- Procesamiento de Datos: 
    - filtrar_por_participante(datos, id_participante) -> df
    - --> selecciona los datos correspondientes a un participante pedido y lo devuelve
    - Posibles errores: 
        -ValueError si ID ingresado es negativo o si no se encuentra dentro de los posibles ID.
        ValueError si la base de datos esta vacia. 
        ValueError si el ID no esta en la base de datos. 
        
- Metricas: 
    - calcular_tiempo_reaccion_promedio(datos) --> df 
        promedio de tiempos de reaccion de todos los participantes
    - calcular_tasa_error(datos) --> df
        calcula  proporción de respuestas incorrectas de todos los participantes
    
- Graficos: 
    -generar_graficos(df) --> Genera y guarda dos gráficos a partir del DataFrame del experimento:
        1.Gráfico de barras: tiempo de reacción promedio por condición experimental.
        2.Gráfico de líneas: evolución del tiempo de reacción a lo largo de los trials.
        Guarda los gráficos como archivos .png en la carpeta 'graficos/'
    - grafico_barras(df):  Genera un gráfico de barras comparando el tiempo de reacción promedio entre las condiciones experimentales ('alta_go' y 'balanceada').
        Guarda el gráfico en 'graficos/comparacion_condiciones.png'.
    - grafico_lineas(df): Genera un gráfico de líneas mostrando la evolución del tiempo de reacción promedio a lo largo de los trials del experimento.
        Guarda el gráfico en 'graficos/evolucion_trials.png'
'''
