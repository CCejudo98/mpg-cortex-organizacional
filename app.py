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
        color: #4ade80 !important; 
    }
    [data-testid="stMetricDelta"] div {
        color: #ff6b6b !important; 
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
    conn = psycopg
            efficiency DOUBLE PRECISION
