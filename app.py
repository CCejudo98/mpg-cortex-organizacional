import streamlit as st
import psycopg2
from datetime import datetime
import numpy as np
import pandas as pd

# ==========================================
# VECTOR DE CONEXIÓN UNIFICADO Y SÍNCRONO
# ==========================================
DB_URL = "postgresql://neondb_owner:npg_4IuJofqBpE3v@ep-patient-pine-apfibhxx-pooler.c-7.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

COSTOS_ENTROPIA_SERVICIOS = {
    "S1_retrabajo_hora": 350.0,      
    "S1_espera_minuto": 15.0,        
    "S2_cuello_botella": 2500.0,     
    "S2_friccion_com": 1200.0,       
}

st.set_page_config(page_title="GAC - Córtex Organizacional", page_icon="🧠", layout="wide")

# ==========================================
# CÁPSULA ESTÉTICA: GRIS MATE Y GRAFITO (CERO TONOS AZULES)
# ==========================================
st.markdown("""
<style>
    /* Fondo General Gris Oscuro Neutro, limpio de residuos azules */
    .stApp {
        background-color: #12131a !important;
        color: #e2e8f0 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* Barra Lateral en Gris Carbón */
    [data-testid="stSidebar"], [data-testid="stSidebar"] > div:first-child {
        background-color: #181920 !important;
        border-right: 2px solid #262730 !important;
    }
    section[data-testid="stSidebar"] .stMarkdown, section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h4, section[data-testid="stSidebar"] p, section[data-testid="stSidebar"] span {
        color: #ffffff !important;
    }
    h1, h2, h3, h4, h5, h6, label, p, span {
        color: #ffffff !important;
        font-weight: 600 !important;
    }
    /* Inputs con contraste neutral */
    .stNumberInput input, .stTextInput input, .stSelectbox div {
        background-color: #f8fafc !important;
        color: #0f172a !important;
        border-radius: 6px !important;
    }
    hr { border-top: 1px solid #262730 !important; }
    [data-testid="stMetricLabel"] p { color: #94a3b8 !important; }
    [data-testid="stMetricValue"] div { color: #34d399 !important; }
    [data-testid="stMetricDelta"] div { color: #f87171 !important; }
</style>
""", unsafe_allow_html=True)

st.title("🧠 CÓRTEX ORGANIZACIONAL: MOTOR DE EFICIENCIA OPERATIVA")
st.caption("GAC Consultoría // Automatización de Estándares de Calidad e Inteligencia de Sistemas.")

# ==========================================
# CONEXIÓN A LA BASE DE DATOS Y MIGRACIÓN SÍNCRONA
# ==========================================
db_disponible = False
historico_eficiencia = []

try:
    conn = psycopg2.connect(DB_URL)
    cursor = conn.cursor()
    
    # 1. Asegurar tabla base
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
    
    # 2. Asegurar columna foco
    try:
        cursor.execute("ALTER TABLE metric_history ADD COLUMN IF NOT EXISTS foco VARCHAR(100);")
        conn.commit()
    except Exception:
        cursor.execute("ROLLBACK;")
    
    db_disponible = True
    st.sidebar.success("✅ Conexión con Servidor Central Activa")
except Exception as e:
    st.sidebar.warning(f"⚠️ Modo Local: {e}")

# ==========================================
# DIRECCIÓN ESTRATÉGICA Y RIESGOS
# ==========================================
st.sidebar.header("⚖️ Dirección Estratégica")
nodo_id = st.sidebar.text_input("Nombre de la Empresa / Sucursal:", value="Mi PYME Eficiente 01")
politica_calidad = st.sidebar.selectbox("Política de Calidad Activa:", ["Consistencia Absoluta en Tiempos de Entrega", "Cero Retrabajo en Entregables", "Saturación Óptima de Capacidad"])

st.sidebar.markdown("---")
st.sidebar.header("📡 Radar de Riesgos Externos (ISO 9001:2015)")
risk_1 = st.sidebar.slider("Volatilidad del Mercado / Competencia (%):", 0, 100, 25)
risk_2 = st.sidebar.slider("Incertidumbre Regulatoria / Fiscal (%):", 0, 100, 15)
lambda_entorno = 1.0 + ((risk_1 + risk_2) / 200.0)

# ==========================================
# ARQUITECTURA DE NAVEGACIÓN
# ==========================================
st.markdown("---")
subsistema_activo = st.radio(
    "Seleccione la Dimensión Organizacional a Auditar u Operar:",
    ["Módulo 1: Flujo Operativo (Lean & Gemba)", "Módulo 2: Control de Variabilidad (SPC & Alertas)", "Módulo 3: Auditoría de Calidad (ISO 9001 Dashboard)"],
    horizontal=True
)

foco_metabolico = "Producción y Fábrica"

if db_disponible:
    try:
        cursor.execute("SELECT efficiency FROM metric_history WHERE foco = %s ORDER BY id DESC LIMIT 30;", (foco_metabolico,))
        historico_eficiencia = [row[0] for row in cursor.fetchall()]
    except Exception:
        pass

# ==========================================
# DESPLIEGUE DE MÓDULOS DE SOFTWARE
# ==========================================

if subsistema_activo == "Módulo 1: Flujo Operativo (Lean & Gemba)":
    st.markdown("## ⚡ Módulo de Flujo Operativo Primario")
    st.subheader("Optimización de Procesos y Eliminación de Desperdicio (*Muda*)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 📥 Capacidad Operativa Invertida")
        horas_hombre = st.number_input("Horas-Hombre ejecutadas en el servicio hoy:", min_value=1.0, value=40.0)
        casos_atendidos = st.number_input("Casos o Clientes atendidos exitosamente:", min_value=0.0, value=12.0)
        e_in_real = (horas_hombre * 100) + (casos_atendidos * 500)
        
    with col2:
        st.markdown("#### 📉 Desperdicios Detectados en el Servicio")
        horas_retrabajo = st.number_input("Horas perdidas en corregir errores o rehacer entregables:", min_value=0.0, value=4.0)
        minutos_espera = st.number_input("Minutos acumulados que el cliente esperó por retrasos:", min_value=0.0, value=60.0)
        i_destroyed = ((horas_retrabajo * COSTOS_ENTROPIA_SERVICIOS["S1_retrabajo_hora"]) + (minutos_espera * COSTOS_ENTROPIA_SERVICIOS["S1_espera_minuto"])) * lambda_entorno

    eficiencia_real = max(0.0, ((e_in_real - i_destroyed) / e_in_real) * 100.0) if e_in_real > 0 else 0.0
    perdida_anual = i_destroyed * 365.0
    ahorro_potencial = perdida_anual * 0.70

    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f'<div style="background-color: #1c1d26; padding: 25px; border-radius: 8px; border: 1px solid #2d2e3a;"><span style="font-size: 12px; text-transform: uppercase; color: #94a3b8;">Eficiencia de Flujo Continuo</span><p style="font-size: 32px; font-weight: bold; color: #34d399 !important; margin: 0;">{eficiencia_real:.1f}%</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div style="background-color: #1c1d26; padding: 25px; border-radius: 8px; border: 1px solid #451a1a;"><span style="font-size: 12px; text-transform: uppercase; color: #fca5a5;">Fuga Financiera Anual</span><p style="font-size: 32px; font-weight: bold; color: #f87171 !important; margin: 0;">${perdida_anual:,.2f} MXN</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div style="background-color: #142e1b; padding: 25px; border-radius: 8px; border: 1px solid #1e5a2c;"><span style="color: #34d399 !important; font-size: 12px; text-transform: uppercase;">Ahorro Retenido por GAC (70%)</span><p style="font-size: 32px; font-weight: bold; color: #34d399 !important; margin: 0;">${ahorro_potencial:,.2f} MXN</p></div>', unsafe_allow_html=True)

    st.markdown("---")
    if st.button("💾 Registrar Datos en Histórico Central"):
        if db_disponible:
            try:
                cursor
