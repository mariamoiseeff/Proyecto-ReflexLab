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
- Codigo principal:
    - Cargar_datos puede laznar una excepcion si algun dato es invalido, por es usamos un bloque try except al llamar esta funcion. Si hay un error no se ejecuta el resto del programa.  
    - Id ingresado puede ser invalido entonces usamos un try-except. Si es invalido, no se ejecuta el resto del programa.
    - Pueden haber problemas con el filtrado del participante, por eso llamamos a la funcion dentro de un try-except
        - Si hay un error, se detiene 
        - Si no hay un error, continua el programa para calcular las metricas 
    - Como las funciones de promedio y tasa error pueden lanzar errores, cada una va con su bloque try-except

Objetos:
modelariamos el sistema usando objetos dividiéndolo en 3 clases diferentes: ensayo, participante y experimento.

Clase Ensayo:

    Atributos:			
        numero_ensayo → entero que identifica el número de ensayo
        estimulo → string que indica el tipo de estímulo presentado 
        t_inicio → número que representa el tiempo de inicio del estímulo
        respuesta → booleano que indica si el participante respondió o no
        tiempo_reaccion → número que representa el tiempo de reacción, en milisegundos
        resultado_respuesta → string que indica si la respuesta fue correcta o incorrecta
        condicion → string que indica la condición experimental 

    Métodos:
        es_correcto() → retorna True si el resultado del ensayo fue correcto
        es_error_comision() → retorna True si el participante respondió ante un estímulo No-Go, cuando no debía hacerlo
        es_error_omision() → retorna True si el participante no respondió ante un estímulo Go, cuando debía hacerlo

Clase Participante:

    Atributos:
        id_participante → entero que identifica de forma única al participante
        ensayos → lista de objetos de tipo Ensayo que contiene todos los ensayos registrados para ese participante

    Métodos:
        agregar_ensayo(ensayo) → incorpora un objeto Ensayo a la lista de ensayos del participante
        calcular_tiempo_reaccion_promedio() → calcula y retorna el promedio de los tiempos de reacción de los ensayos correctos
        calcular_tasa_error() → calcula y retorna la proporción de respuestas incorrectas sobre el total de ensayos
        errores_comision() → cuenta y retorna la cantidad de ensayos donde el participante respondió ante un estímulo No-Go
        errores_omision() → cuenta y retorna la cantidad de ensayos donde el participante no respondió ante un estímulo Go

Clase Experimento:

    Atributos:
        ruta → string con la ruta relativa al archivo CSV
        participantes → lista de objetos de tipo Participante cargados desde el archivo

    Métodos:
        validar_archivo() → verifica que la ruta exista, que el archivo pueda abrirse y que no esté vacío
        validar_linea(linea) → verifica que cada línea del archivo tenga la cantidad correcta de columnas, los tipos de datos esperados y los valores dentro de los rangos válidos
        cargar_datos() → lee el archivo CSV, aplica las validaciones y construye los objetos Participante y Ensayo correspondientes
        buscar_participante(id_participante) → busca y retorna el objeto Participante que corresponde al ID ingresado

