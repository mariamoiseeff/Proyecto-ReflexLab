import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
 
# ── Agregar src/ al path para importar módulos del backend ──────────────────
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
 
from carga_datos import cargar_datos
from metricas import calcular_tiempo_reaccion_promedio, calcular_tasa_error
from graficos import grafico_barras, grafico_lineas
 
# ── Configuración de página ──────────────────────────────────────────────────
st.set_page_config(
    page_title="ReflexLab Dashboard",
    page_icon="🧠",
    layout="wide",
)
 
# ── Estilos ──────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background-color: #0f172a;
        color: #e2e8f0;
    }
    [data-testid="stHeader"] { background: transparent; }
 
    .titulo {
        font-family: 'Georgia', serif;
        font-size: 2.2rem;
        font-weight: 700;
        color: #93c5fd;
        letter-spacing: 0.04em;
    }
    .subtitulo {
        font-size: 0.9rem;
        color: #64748b;
        margin-bottom: 1.5rem;
    }
 
    [data-testid="stMetric"] {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 1rem 1.2rem;
    }
    [data-testid="stMetricLabel"] { color: #94a3b8 !important; font-size: 0.8rem; }
    [data-testid="stMetricValue"] { color: #93c5fd !important; font-size: 1.7rem; font-weight: 700; }
 
    .seccion { color: #cbd5e1; font-weight: 600; font-size: 1rem; margin-bottom: 0.4rem; }
</style>
""", unsafe_allow_html=True)
 
# ── Encabezado ───────────────────────────────────────────────────────────────
st.markdown('<p class="titulo">🧠 ReflexLab — Dashboard</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitulo">Análisis de Tarea Go/No-Go · Control Inhibitorio</p>', unsafe_allow_html=True)
st.markdown("---")
 
 
# ════════════════════════════════════════════════════════════════════════════
# PASO 1 — Carga dinámica de datos
# ════════════════════════════════════════════════════════════════════════════
st.subheader("📂 Cargar archivo de datos")
 
archivo = st.file_uploader(
    "Arrastrá o seleccioná el archivo CSV del experimento",
    type=["csv"],
    help="El archivo debe contener las columnas: id_participante, trial, estimulo, "
         "t_inicio, respuesta, tiempo_reaccion, resultado_respuesta, condicion"
)
 
if archivo is None:
    st.info("⬆️ Cargá un archivo CSV para comenzar el análisis.")
    st.stop()
 
 
# ════════════════════════════════════════════════════════════════════════════
# PASO 2 — Puente de validación defensiva
# ════════════════════════════════════════════════════════════════════════════
 
# Guardar el archivo subido en una ruta temporal para pasarla a cargar_datos()
ruta_temporal = f"/tmp/{archivo.name}"
with open(ruta_temporal, "wb") as f:
    f.write(archivo.getbuffer())
 
try:
    df = cargar_datos(ruta_temporal)   # devuelve un DataFrame validado
except ValueError as e:
    st.error(f"🚫 El archivo no pasó la validación:\n\n{e}")
    st.stop()
except Exception as e:
    st.error(f"🚫 Error inesperado al cargar el archivo:\n\n{e}")
    st.stop()
 
st.success(f"✅ Archivo válido: **{archivo.name}** — {len(df)} registros cargados.")
st.markdown("---")
 
 
# ════════════════════════════════════════════════════════════════════════════
# PASO 3 — Indicadores Clave (KPIs)
# ════════════════════════════════════════════════════════════════════════════
st.subheader("📊 Indicadores Clave")
 
try:
    tr_promedio = calcular_tiempo_reaccion_promedio(df)
except ValueError:
    tr_promedio = None
 
try:
    tasa_error = calcular_tasa_error(df)
except ValueError:
    tasa_error = None
 
n_participantes = df["id_participante"].nunique()
n_trials = len(df)
 
col1, col2, col3, col4 = st.columns(4)
 
with col1:
    st.metric(
        label="⏱ T. Reacción Promedio",
        value=f"{tr_promedio:.1f} ms" if tr_promedio is not None else "—"
    )
with col2:
    st.metric(
        label="❌ Tasa de Error",
        value=f"{tasa_error * 100:.1f} %" if tasa_error is not None else "—"
    )
with col3:
    st.metric(
        label="👤 Participantes",
        value=str(n_participantes)
    )
with col4:
    st.metric(
        label="🔢 Total de Trials",
        value=str(n_trials)
    )
 
st.markdown("---")
 
 
# ════════════════════════════════════════════════════════════════════════════
# PASO 4 — Visualización interactiva
# ════════════════════════════════════════════════════════════════════════════
st.subheader("📈 Visualizaciones")
 
col_izq, col_der = st.columns(2)
 
# ── Gráfico de barras: T. Reacción por condición ────────────────────────────
with col_izq:
    st.markdown('<p class="seccion">Tiempo de Reacción Promedio por Condición</p>', unsafe_allow_html=True)
    fig1, ax1 = plt.subplots(figsize=(7, 4), facecolor="#1e293b")
    ax1.set_facecolor("#1e293b")
 
    promedio_condicion = df.groupby("condicion")["tiempo_reaccion"].mean()
    colores = ["#1d4ed8", "#b45309"]
    promedio_condicion.plot(
        kind="bar",
        ax=ax1,
        color=colores[:len(promedio_condicion)],
        edgecolor="#334155",
        alpha=0.9,
    )
    ax1.set_title("T. Reacción por Condición", color="#cbd5e1", fontsize=11, fontweight="bold", pad=10)
    ax1.set_xlabel("Condición", color="#94a3b8", fontsize=9)
    ax1.set_ylabel("Tiempo de Reacción (ms)", color="#94a3b8", fontsize=9)
    ax1.tick_params(colors="#94a3b8", rotation=0)
    ax1.spines[:].set_color("#334155")
    ax1.grid(True, linestyle="--", alpha=0.3, axis="y", color="#475569")
    plt.tight_layout()
    st.pyplot(fig1)
    plt.close(fig1)
 
# ── Gráfico de líneas: evolución por trial ───────────────────────────────────
with col_der:
    st.markdown('<p class="seccion">Evolución del Tiempo de Reacción por Trial</p>', unsafe_allow_html=True)
    fig2, ax2 = plt.subplots(figsize=(7, 4), facecolor="#1e293b")
    ax2.set_facecolor("#1e293b")
 
    promedio_trial = df.groupby("trial")["tiempo_reaccion"].mean()
    promedio_trial.plot(
        kind="line",
        ax=ax2,
        color="#38bdf8",
        linewidth=1.8,
        marker="o",
        markersize=3,
    )
    ax2.set_title("Evolución por Trial", color="#cbd5e1", fontsize=11, fontweight="bold", pad=10)
    ax2.set_xlabel("Trial", color="#94a3b8", fontsize=9)
    ax2.set_ylabel("Tiempo de Reacción Promedio (ms)", color="#94a3b8", fontsize=9)
    ax2.tick_params(colors="#94a3b8")
    ax2.spines[:].set_color("#334155")
    ax2.grid(True, linestyle=":", alpha=0.4, color="#475569")
    plt.tight_layout()
    st.pyplot(fig2)
    plt.close(fig2)
 
st.markdown("---")
 
# ── Tabla de datos crudos (opcional) ─────────────────────────────────────────
with st.expander("🔍 Ver datos crudos"):
    st.dataframe(df, use_container_width=True, height=300)
 

