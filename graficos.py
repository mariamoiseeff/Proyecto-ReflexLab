import matplotlib.pyplot as plt
import os
 
 
def generar_graficos(df):
    """
    Genera y guarda dos gráficos a partir del DataFrame del experimento:
    1. Gráfico de barras: tiempo de reacción promedio por condición experimental.
    2. Gráfico de líneas: evolución del tiempo de reacción a lo largo de los trials.
 
    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame con los datos del experimento ya cargados y validados.
        Debe contener las columnas: 'tiempo_reaccion','condicion', 'trial'.
 
    Returns
    -------
    None
        Guarda los gráficos como archivos .png en la carpeta 'graficos/'.
    """
    columnas_necesarias = ["condicion", "tiempo_reaccion", "trial"]

    for columna in columnas_necesarias:
        if columna not in df.columns:
            print(f"Falta la columna: {columna}")
            return
    
    os.makedirs("graficos", exist_ok=True)
 
    grafico_barras(df)
    grafico_lineas(df)
 
 
def grafico_barras(df):
    """
    Genera un gráfico de barras comparando el tiempo de reacción promedio
    entre las condiciones experimentales ('alta_go' y 'balanceada').
 
    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame con columnas 'condicion' y 'tiempo_reaccion'.
 
    Returns
    -------
    None
        Guarda el gráfico en 'graficos/comparacion_condiciones.png'.
    """
    promedio_por_condicion = df.groupby("condicion")["tiempo_reaccion"].mean()
 
    plt.figure(figsize=(9, 5))
    promedio_por_condicion.plot(
        kind="bar",
        color=["#1e3a8a", "#b45309"],
        edgecolor="black",
        alpha=0.8
    )
 
    plt.title(
        "Tiempo de Reacción Promedio por Condición Experimental",
        fontsize=13,
        fontweight="bold",
        pad=15
    )
    plt.xlabel("Condición Experimental", fontsize=11)
    plt.ylabel("Tiempo de Reacción Promedio (ms)", fontsize=11)
    plt.xticks(rotation=0)
    plt.grid(True, linestyle="--", alpha=0.5, axis="y")
    plt.tight_layout()
 
    plt.savefig("graficos/comparacion_condiciones.png", dpi=300)
    plt.close()
    print("Gráfico guardado: graficos/comparacion_condiciones.png")
 
 
def grafico_lineas(df):
    """
    Genera un gráfico de líneas mostrando la evolución del tiempo de reacción
    promedio a lo largo de los trials del experimento.
 
    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame con columnas 'trial' y 'tiempo_reaccion'.
 
    Returns
    -------
    None
        Guarda el gráfico en 'graficos/evolucion_trials.png'.
    """
    promedio_por_trial = df.groupby("trial")["tiempo_reaccion"].mean()
 
    plt.figure(figsize=(11, 5))
    promedio_por_trial.plot(
        kind="line",
        color="#1e3a8a",
        linewidth=1.5,
        marker="o",
        markersize=3
    )
 
    plt.title(
        "Evolución del Tiempo de Reacción a lo Largo de los Trials",
        fontsize=13,
        fontweight="bold",
        pad=15
    )
    plt.xlabel("Trial", fontsize=11)
    plt.ylabel("Tiempo de Reacción Promedio (ms)", fontsize=11)
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.tight_layout()
 
    plt.savefig("graficos/evolucion_trials.png", dpi=300)
    plt.close()
    print("Gráfico guardado: graficos/evolucion_trials.png") 

