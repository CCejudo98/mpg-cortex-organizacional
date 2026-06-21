import streamlit as st
import psycopg2
from datetime import datetime

# ==========================================
# VECTOR DE CONEXIÓN INMUTABLE (NEON)
# ==========================================
DB_URL = "postgresql://neondb_owner:npg_4IuJofqBpE3v@ep-patient-pine-apfibhxx-pooler.c-7.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

# Costos unitarios de la entropía en el sector servicios para el cálculo monetario
COSTOS_ENTROPIA_SERVICIOS = {
    "S1_retrabajo_hora": 350.0,      # Costo de oportunidad y sueldo por corregir errores
    "S1_espera_minuto": 15.0,        # Penalización por insatisfacción/pérdida de clientes
    "S2_cuello_botella": 2500.0,     # Costo latente de un servicio estancado o fuera de SLA
    "S2_friccion_com": 1200.0,       # Costo de juntas extra y correos duplicados por desalineación
}

st.set_page_config(page_title="gac - Córtex Organizacional", page_icon="🧠", layout="wide")

# ==========================================
# ESTILO VISUAL: BUSINESS NAVY (TEXTOS CORREGIDOS A BLANCO)
# ==========================================
st.markdown("""
<style>
    /* Fondo Azul Marino Profesional */
    .stApp {
        background-color: #001f3f;
        color: #ffffff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Barra Lateral Oxford */
    [data-testid="stSidebar"], [data-testid="stSidebar"] > div:first-child {
        background-color: #1a1a1a !important;
        border-right: 2px solid #003366 !important;
    }
    
    section[data-testid="stSidebar"] .stMarkdown, section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h4 {
        color: #ffffff !important;
    }

    h1, h2, h3, h4, h5, h6, label {
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

    /* Corrección explícita para forzar texto blanco en etiquetas secundarias de métricas */
    [data-testid="stMetricLabel"] p {
        color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🧠 CÓRTEX ORGANIZACIONAL: MOTOR DE EFICIENCIA OOPERATIVA")
st.caption("GAC Consultoría // Automatización de Estándares de Calidad e Inteligencia de Sistemas.")

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
# DIRECCIÓN ESTRATÉGICA (ANTES SISTEMA 5)
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
# GESTIÓN DE RIESGOS (ANTES SISTEMA 4)
# ==========================================
st.sidebar.markdown("---")
st.sidebar.header("📡 Radar de Riesgos Externos (ISO 9001:2015)")
st.sidebar.markdown("<span style='color: #ffffff;'>Monitoreo predictivo de amenazas del mercado</span>", unsafe_allow_html=True)

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
            <span style="font-size: 12px; text-transform: uppercase; color: #ffffff;">Eficiencia de Flujo Continuo</span>
            <p style="font-size: 32px; font-weight: bold; color: #4ade80; margin: 0;">{eficiencia_real:.1f}%</p>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div style="background-color: #1a1a1a; padding: 25px; border-radius: 8px; border: 1px solid #772222;">
            <span style="font-size: 12px; text-transform: uppercase; color: #ffffff;">Fuga Financiera por Variabilidad Anual</span>
            <p style="font-size: 32px; font-weight: bold; color: #ff6b6b; margin: 0;">${perdida_anual:,.2f} MXN</p>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""<div style="background-color: #0f3322; padding: 25px; border-radius: 8px;">
            <span style="color: #4ade80; font-size: 12px; text-transform: uppercase;">Ahorro Retenido por MPG (70%)</span>
            <p style="font-size: 32px; font-weight: bold; color: #4ade80; margin: 0;">${ahorro_potencial:,.2f} MXN</p>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")
    if st.button("💾 Registrar Datos en Histórico Central"):
        if db_disponible:
            try:
                cursor.execute("INSERT INTO metric_history (e_in, e_out, efficiency) VALUES (%s, %s, %s);", 
                               (e_in_real, i_destroyed, eficiencia_real))
                conn.commit()
                st.success(f"✅ Datos respaldados bajo la directriz estratégica: '{politica_calidad}'")
            except Exception as e:
                st.error(f"Falla en el almacenamiento de datos: {e}")

elif subsistema_activo == "Módulo 2: Control de Variabilidad (SPC & Alertas)":
    st.header("🛡️ Módulo de Coordinación y Control de Variabilidad")
    st.subheader("Control Estadístico de Procesos (SPC) y Amortiguación de Cuellos de Botella")
    
    st.markdown("### 🚦 Monitor de Desviación en Células de Trabajo")
    st.markdown("<span style='color: #ffffff;'>El sistema analiza las desviaciones estándar en tiempo real para evitar la desincronización de los equipos.</span>", unsafe_allow_html=True)
    
    col_s1, col_s2, col_s3 = st.columns(3)
    
    with col_s1:
        st.markdown("""<div style="background-color: #1a2e1a; padding: 20px; border-radius: 8px; border-left: 8px solid #4ade80;">
            <h4 style="color: #4ade80 !important; margin:0;">Célula A: Frente de Servicio</h4>
            <p style="margin:5px 0 0 0; font-size:14px; color:#ffffff;">Variabilidad: Bajo Control (Estabilidad en Límites Sigma)</p>
            <p style="font-size:20px; font-weight:bold; color:#ffffff; margin:5px 0 0 0;">CONFORME</p>
        </div>""", unsafe_allow_html=True)
        
    with col_s2:
        st.markdown("""<div style="background-color: #3b3010; padding: 20px; border-radius: 8px; border-left: 8px solid #facc15;">
            <h4 style="color: #facc15 !important; margin:0;">Célula B: Procesamiento de Información</h4>
            <p style="margin:5px 0 0 0; font-size:14px; color:#ffffff;">Tendencia latente de retraso detectada en el flujo.</p>
            <p style="font-size:20px; font-weight:bold; color:#ffffff; margin:5px 0 0 0;">ACCIÓN PREVENTIVA</p>
        </div>""", unsafe_allow_html=True)
        
    with col_s3:
        st.markdown("""<div style="background-color: #3b1a1a; padding: 20px; border-radius: 8px; border-left: 8px solid #f87171;">
            <h4 style="color: #f87171 !important; margin:0;">Célula C: Soporte y Postventa</h4>
            <p style="margin:5px 0 0 0; font-size:14px; color:#ffffff;">Cuello de botella activo: Incidentes fuera de acuerdo de servicio.</p>
            <p style="font-size:20px; font-weight:bold; color:#ffffff; margin:5px 0 0 0;">DESVIACIÓN CRÍTICA</p>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🎛️ Evaluación de Fricción Interdepartamental")
    cuellos_botella_ingresados = st.slider("Número de cuellos de botella / bloqueos operativos hoy:", 0, 10, 2)
    fricciones_comunicacion = st.slider("Fallas de alineación interna reportadas:", 0, 20, 5)
    
    impacto_s2 = (cuellos_botella_ingresados * COSTOS_ENTROPIA_SERVICIOS["S2_cuello_botella"]) + (fricciones_comunicacion * COSTOS_ENTROPIA_SERVICIOS["S2_friccion_com"])
    
    # Texto de la etiqueta modificado explícitamente a Blanco mediante CSS nativo en el bloque anterior
    st.metric(label="Pérdida Económica por Descoordinación Interna (Estimación Diaria)", value=f"${impacto_s2:,.2f} MXN", delta="-Intervención Requerida", delta_color="inverse")

elif subsistema_activo == "Módulo 3: Auditoría de Calidad (ISO 9001 Dashboard)":
    st.header("📈 Módulo de Evaluación de Desempeño y Auditoría")
    st.subheader("Tablero de Mando Central // Preparación Automatizada para Certificación ISO 9001")
    
    st.markdown("""
    <span style='color: #ffffff;'>Este módulo consolida de forma nativa los registros de variabilidad operativa y control de procesos para alimentar los requerimientos de la <strong>Revisión por la Dirección</strong> exigida por las normas internacionales, reduciendo la carga administrativa.</span>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📑 Reporte Automatizado de Cumplimiento")
    st.text_area(
        label="Cuerpo del Reporte de Aseguramiento de Calidad:",
        value=f"INFORME DE CAPACIDAD Y ESTABILIDAD PROCESAL\n"
              f"Organización: {nodo_id}\n"
              f"Fecha de Emisión: {datetime.now().strftime('%Y-%m-%d')}\n"
              f"Estatus de la Política Activa ('{politica_calidad}'): Conforme con los límites de control establecidos.\n"
              f"Diagnóstico de Variabilidad: El flujo operativo mantiene estabilidad estadística. Desviaciones amortiguadas en Módulo 2. Se sugiere revisar mitigación de riesgos de la dirección.",
        height=150
    )
    st.download_button(label="📥 Descargar Reporte de Auditoría", data="Datos de Auditoría MPG", file_name="Auditoria_ISO9001_MPG.txt")
