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
    "S2_friccion_com": 1200.0        
}

st.set_page_config(page_title="GAC - Córtex Organizacional", page_icon="🧠", layout="wide")

# ==========================================
# CÁPSULA ESTÉTICA: CARBONO Y GRAFITO PURO (CERO COMPLETAMENTE AZUL)
# ==========================================
st.markdown("""
<style>
    /* Inyección de fondo gris oscuro mate neutro absoluto */
    .stApp {
        background-color: #12131a !important;
        color: #e2e8f0 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* Estructuración de barra lateral carbono */
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
    /* Entradas de datos con contraste limpio */
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
    
    # 1. Asegurar tabla base heredada
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
    
    # 2. Inyección reparadora de la columna foco
    try:
        cursor.execute("ALTER TABLE metric_history ADD COLUMN IF NOT EXISTS foco VARCHAR(100);")
        conn.commit()
    except Exception:
        cursor.execute("ROLLBACK;")
    
    db_disponible = True
    st.sidebar.success("✅ Conexión con Servidor Central Activa")
except Exception as e:
    st.sidebar.warning(f"⚠️ Modo Local Activo: {e}")

# ==========================================
# DIRECCIÓN ESTRATÉGICA Y RIESGOS (CORREGIDO)
# ==========================================
