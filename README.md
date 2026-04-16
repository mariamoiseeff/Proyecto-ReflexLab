# Proyecto-ReflexLab
Nombres: Sofia Davidov, Maria Moiseeff, Clara Antelo Cernadas

Funcion del proyecto: Analizar datos de ReflexLab para estudiar los tiempo de reaccion y las respuestas de los participantes, generando metricas que nos permiten evaluar el resultado. 

Que se encuentra dentro: el proyecto incluye, modulos para cargar, validar, procesar y validar datos. Un archivo pricipal y una carpeta con los datos y diagramas del sistema. 

Como se ejecuta: el programa carga los datos, los valida y los procesa para calcular metricas como tiempo de reaccion y porcentaje de aciertos, depues muestra los resultados por pantalla. 

Errores y Validaciones: 
- Funcion validar_registro: 
    - Para cada dato parseado se valida que sea el tipo de dato correcto y este dentro de las opciones permitidas. 
    - Si no se verifican estas condiciones, se levanta un ValueError y se detiene la validacion de todos los datos. Si uno esta mal, ya ese registro no sirve. 
- Funcion cargar_datos: 
    - Para cada linea de datos se trata de validar. Si hay datos invalidos, se lanza un ValueError y se deja de leer esa linea, porque los datos invalidos no pueden ser tomados en cuenta. 
    - Se descarta esa linea invalida y se siguen recorriendo y validando las siguientes lineas de datos.
- Funcion calcular_tiempo_reaccion_promedio: 
    - un posible error es que la lista de tiempos de reaccion este vacia, lo manejamos lanzando un error para que se detenga la ejecucion de la funcion. 
- Funcion calcular_tasa_error: 
    - un posible error es que la lista de respuestas este vacia, lo manejamos lanzando un error para que se detenga la ejecucion de la funcion. 
- Funcion filtrar_por_participante: 
    - posible error es que ingresen un numero negativo, lo manejamos dentro de la funcion y en el codigo principal lanzando ValueError, deteniendo la ejecucion del programa en ambos lados. 
    - posible error es que no se pueda convertir en un entero, lo manejamos en el codigo principal con bloque try-except
    - posible error es que ingresen ID de un participante que no exista en nuestro registro de datos. Lo manejamos dentro de la funcion lanznado un error si no esta dentro de una lista de posibles valores que armamos al recorrer los datos. 


