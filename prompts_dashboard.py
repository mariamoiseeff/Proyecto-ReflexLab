prompt semmila:
    Sos un experto en diseño de interfaces web y en Streamlit. Necesito que me hagas el archivo app.py, que es la interfaz web del sistema ReflexLab, 
    conectada con los módulos que ya tenemos hechos en src/. El proyecto analiza datos de una tarea cognitiva Go/No-Go. Ya tenemos carga_datos.py con
    la función cargar_datos(ruta) que lee el CSV, lo convierte en un DataFrame de pandas y lo valida, si algo está mal lanza un ValueError. También
    tenemos metricas.py con calcular_tiempo_reaccion_promedio(df) y calcular_tasa_error(df) que reciben el DataFrame y devuelven un número, 
    y graficos.py con grafico_barras(df) y grafico_lineas(df) que generan gráficos con matplotlib. El CSV tiene estas columnas: id_participante, 
    trial, estimulo (go/nogo), t_inicio, respuesta (True/False), tiempo_reaccion, resultado_respuesta (correcto/incorrecto), condicion (alta_go/balanceada). 
    El documento de diseño está en src/diseño.md (adjunto). La interfaz tiene que seguir este orden: primero un st.file_uploader para que el 
    usuario suba el CSV, después llamar a cargar_datos() y si lanza ValueError mostrarlo con st.error() y cortar con st.stop(), después mostrar 
    4 métricas con st.metric (tiempo de reacción promedio, tasa de error, cantidad de participantes y total de trials), y por último mostrar los 
    dos gráficos con st.pyplot en dos columnas. Usá un diseño oscuro y prolijo, acorde a un proyecto de investigación en neurociencia.

interaccion: 
    Cuando corrimos el archivo app.py desde Spyder, nos apareció un error que decía No module named 'streamlit'. Esto pasó porque Streamlit no 
    estaba instalado en el entorno que estaba usando Spyder. Investigamos que para solucionarlo había que instalar Streamlit desde la terminal 
    con el comando pip install streamlit y que además no se puede correr desde Spyder sino que hay que ejecutarlo con streamlit run app.py 
    directamente en la terminal. Sin embargo, no llegamos a probarlo porque no pudimos completar la instalación.
    
reflexion tecnica:
    Lo que más nos ayudó fue armar el prompt con la estructura ROCA desde el principio. Ponerle un rol experto a la IA hizo que el código generado 
    tuviera sentido para el proyecto. Decirle exactamente cómo se llamaban las funciones, qué recibían y qué errores lanzaban evitó que inventara 
    cosas. Escribir el flujo del usuario como pasos numerados fue clave para que respetara la lógica del programa: si el archivo es inválido, se 
    detiene y no sigue mostrando nada.
