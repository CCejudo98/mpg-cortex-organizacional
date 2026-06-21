import streamlit as st
import psycopg2
from datetime import datetime

# ==========================================
# VECTOR DE CONEXIÓN INMUTABLE (NEON)
# ==========================================
DB_URL = "postgresql://neondb_owner:npg_4IuJofqBpE3v@ep-patient-pine-apfibhxx-pooler.c-7.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

# Costos unitarios de la entropía en el sector servicios para el cálculo monetario
COSTOS_ENTROPIA_SERVICIOS = {
    "S1_retrabajo_hora": 350.0,      
    "S1_espera_minuto": 15.0,        
    "S2_cuello_botella": 2500.0,     
    "S2_friccion_com": 1200.0,       
}

st.set_page_config(page_title="MPG - Córtex Organizacional", page_icon="🧠", layout="wide")

# ==========================================
# ESTILO VISUAL: BUSINESS NAVY (TEXTOS FORZADOS A BLANCO PURO)
# ==========================================
st.markdown("""
<style>
    /* Fondo Azul Marino Profesional */
    .stApp {
        background-color: #001f3f;
        color: #ffffff !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Barra Lateral Oxford */
    [data-testid="stSidebar"], [data-testid="stSidebar"] > div:first-child {
        background-color: #1a1a1a !important;
        border-right: 2px solid #003366 !important;
    }
    
    section[data-testid="stSidebar"] .stMarkdown, section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h4, section[data-testid="stSidebar"] p, section[data-testid="stSidebar"] span {
        color: #ffffff !important;
    }

    h1, h2, h3, h4, h5, h6, label, p, span {
        color: #ffffff !important;
        font-weight: 600 !important;
    }
    
    .stNumberInput input, .stTextInput input, .stSelectbox div {
        background-color: #f0f2f6 !important;
        color: #001f3f !important;
        border-radius: 5px !important;
    }
    
    .stSlider {
        padding-bottom: 20px !important;
    }

    hr {
        border-top: 1px solid #003366 !important;
    }

    /* CORRECCIÓN DE COLORES: Forzar Blanco en etiquetas de componentes nativos de Streamlit */
    [data-testid="stMetricLabel"] p {
        color: #ffffff !important;
    }
    [data-testid="stMetricValue"] div {
        color: #4ade80 !important; /* El valor numérico de la pérdida se mantiene visible */
    }
    [data-testid="stMetricDelta"] div {
        color: #ff6b6b !important; /* El delta de intervención en rojo */
    }
    
    /* Forzar que los párrafos dentro de las cajas personalizadas de las células también sean blancos */
    .stMarkdown div p {
        color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🧠 CÓRTEX ORGANIZACIONAL: MOTOR DE VIABILIDAD")
st.caption("Metric & Power Group // Automatización de Estándares de Calidad e Inteligencia de Sistemas.")

# ==========================================
# CONEXIÓN A LA BASE DE DATOS
# ==========================================
db_disponible = False
conn = None
cursor = None
try:
    conn = psycopg2.connect(DB_URL)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS metric_history (
            id SERIAL PRIMARY KEY, 
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
            e_in DOUBLE PRECISION, 
            e_out DOUBLE PRECISION, 
            efficiency DOUBLE PRECISION
        );
    """)
    conn.commit()
    st.sidebar.success("✅ Conexión con Servidor Central Activa")
    db_disponible = True
except Exception:
    st.sidebar.warning("⚠️ Operando en modo local (sin internet)")
    db_disponible = False

# ==========================================
# DIRECCIÓN ESTRATÉGICA
# ==========================================
st.sidebar.header("⚖️ Dirección Estratégica y Gobernanza")
nodo_id = st.sidebar.text_input("Nombre de la Empresa / Sucursal:", value="Mi PYME Eficiente 01")
politica_calidad = st.sidebar.selectbox(
    "Política de Calidad Activa:",
    ["Consistencia Absoluta en Tiempos de Entrega", "Cero Retrabajo en Entregables", "Saturación Óptima de Capacidad"]
)

st.sidebar.markdown("---")
st.sidebar.header("💼 Inversión de Estructura")
costo_licencia = st.sidebar.number_input("Inversión Anual en Software (MXN):", min_value=0.0, value=15000.0, step=1000.0)

# ==========================================
# GESTIÓN DE RIESGOS
# ==========================================
st.sidebar.markdown("---")
st.sidebar.header("📡 Radar de Riesgos Externos (ISO 9001:2015)")

risk_1 = st.sidebar.slider("Volatilidad del Mercado / Competencia (%):", 0, 100, 25)
risk_2 = st.sidebar.slider("Incertidumbre Regulatoria / Fiscal (%):", 0, 100, 15)
lambda_entorno = 1.0 + ((risk_1 + risk_2) / 200.0)

# ==========================================
# ARQUITECTURA DE NAVEGACIÓN (TÉRMINOS LEAN & ISO)
# ==========================================
st.markdown("---")
subsistema_activo = st.radio(
    "Seleccione la Dimensión Organizacional a Auditar u Operar:",
    [
        "Módulo 1: Flujo Operativo (Lean & Gemba)", 
        "Módulo 2: Control de Variabilidad (SPC & Alertas)", 
        "Módulo 3: Auditoría de Calidad (ISO 9001 Dashboard)"
    ],
    horizontal=True
)

# ==========================================
# DESPLIEGUE DE MÓDULOS DE SOFTWARE
# ==========================================

if subsistema_activo == "Módulo 1: Flujo Operativo (Lean & Gemba)":
    st.header("⚡ Módulo de Flujo Operativo Primario")
    st.subheader("Optimización de Procesos y Eliminación de Desperdicio (*Muda*)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 📥 Capacidad Operativa Invertida")
        horas_hombre = st.number_input("Horas-Hombre ejecutadas en el servicio hoy:", min_value=0.0, value=40.0)
        casos_atendidos = st.number_input("Casos, Proyectos o Clientes atendidos exitosamente:", min_value=0.0, value=12.0)
        
        e_in_real = (horas_hombre * 100) + (casos_atendidos * 500)
        
    with col2:
        st.markdown("#### 📉 Desperdicios Detectados en el Servicio")
        horas_retrabajo = st.number_input("Horas perdidas en corregir errores o rehacer entregables:", min_value=0.0, value=4.0)
        minutos_espera = st.number_input("Minutos acumulados que el cliente esperó por retrasos:", min_value=0.0, value=60.0)
        
        i_destroyed = ((horas_retrabajo * COSTOS_ENTROPIA_SERVICIOS["S1_retrabajo_hora"]) + 
                       (minutos_espera * COSTOS_ENTROPIA_SERVICIOS["S1_espera_minuto"])) * lambda_entorno

    eficiencia_real = max(0.0, ((e_in_real - i_destroyed) / e_in_real) * 100.0) if e_in_real > 0 else 0.0
    perdida_anual = i_destroyed * 365.0
    ahorro_potencial = perdida_anual * 0.70

    st.markdown("---")
    st.subheader("📊 Indicadores de Homeostasis Estabilizada")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""<div style="background-color: #1a1a1a; padding: 25px; border-radius: 8px; border: 1px solid #003366;">
            <span style="font-size: 12px; text
