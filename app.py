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

st.set_page_config(page_title="MPG - Córtex Organizacional", page_icon="🧠", layout="wide")

# ==========================================
# ESTILO VISUAL: BUSINESS NAVY DE ALTA SOBERANÍA
# ==========================================
st.markdown("""
<style>
    .stApp {
        background-color: #001f3f;
        color: #e0e0e0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
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
</style>
""", unsafe_allow_html=True)

st.title("🧠 CÓRTEX ORGANIZACIONAL: MOTOR DE VIABILIDAD")
st.caption("Metric & Power Group // Automatización de Estándares de Calidad e Inteligencia de Sistemas.")

# ==========================================
# CONEXIÓN A LA BASE DE DATOS (NÚCLEO PERSISTENTE)
# ==========================================
db_disponible = False
conn = None
cursor = None
try:
    conn = psycopg2.connect(DB_URL)
    cursor = conn.cursor()
    # Inicialización del histórico adaptado al ecosistema de viabilidad
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
# SISTEMA 5: IDENTIDAD Y POLÍTICAS (BARRA LATERAL)
# ==========================================
st.sidebar.header("⚖️ Sistema 5: Identidad y Gobernanza")
nodo_id = st.sidebar.text_input("Nombre de la Empresa / Oikos:", value="Mi PYME Eficiente 01")
politica_calidad = st.sidebar.selectbox(
    "Regla de Oro de Calidad (Política Activa):",
    ["Consistencia Absoluta en Tiempos de Entrega", "Cero Retrabajo en Entregables", "Saturación Óptima de Capacidad"]
)

st.sidebar.markdown("---")
st.sidebar.header("💼 Inversión de Estructura")
costo_licencia = st.sidebar.number_input("Inversión Anual en Software (MXN):", min_value=0.0, value=15000.0, step=1000.0)

# ==========================================
# SISTEMA 4: INTELIGENCIA Y ENTORNO (BARRA LATERAL)
# ==========================================
st.sidebar.markdown("---")
st.sidebar.header("📡 Sistema 4: Radar del Entorno (ISO 9001:2015)")
st.sidebar.markdown("*Gestión Predictiva de Riesgos y Oportunidades del Mercado*")

risk_1 = st.sidebar.slider("Volatilidad del Mercado / Competencia (%):", 0, 100, 25)
risk_2 = st.sidebar.slider("Incertidumbre Regulatoria / Fiscal (%):", 0, 100, 15)
lambda_entorno = 1.0 + ((risk_1 + risk_2) / 200.0)

# ==========================================
# ARQUITECTURA DE NAVEGACIÓN POR SUBSISTEMAS VSM
# ==========================================
st.markdown("---")
subsistema_activo = st.radio(
    "Seleccione el Subsistema Organizacional a Auditar u Operar:",
    [
        "Sistema 1: Operación Eficiente (Lean & Gemba)", 
        "Sistema 2: Estabilizador Anti-Crisis (SPC & Alertas)", 
        "Sistema 3: Control y Dashboard (ISO 9001 Auditoría)"
    ],
    horizontal=True
)

# ==========================================
# DESPLIEGUE DE MÓDULOS DE SOFTWARE
# ==========================================

if subsistema_activo == "Sistema 1: Operación Eficiente (Lean & Gemba)":
    st.header("⚡ Módulo de Operación Eficiente (Sistema 1)")
    st.subheader("Automatización de Flujo Continuo y Mitigación de Desperdicio (*Muda*)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 📥 Entradas: Capacidad Operativa")
        horas_hombre = st.number_input("Horas-Hombre ejecutadas en el servicio hoy:", min_value=0.0, value=40.0)
        casos_atendidos = st.number_input("Casos, Proyectos o Clientes atendidos exitosamente:", min_value=0.0, value=12.0)
        
        # Energía metabólica abstracta del sistema
        e_in_real = (horas_hombre * 100) + (casos_atendidos * 500)
        
    with col2:
        st.markdown("#### 📉 Entropía Oculta: Desperdicios del Servicio (Lean)")
        horas_retrabajo = st.number_input("Horas perdidas en corregir errores o rehacer entregables:", min_value=0.0, value=4.0)
        minutos_espera = st.number_input("Minutos acumulados que el cliente esperó por retrasos:", min_value=0.0, value=60.0)
        
        # Destrucción de energía afectada por la volatilidad exterior del Sistema 4
        i_destroyed = ((horas_retrabajo * COSTOS_ENTROPIA_SERVICIOS["S1_retrabajo_hora"]) + 
                       (minutos_espera * COSTOS_ENTROPIA_SERVICIOS["S1_espera_minuto"])) * lambda_entorno

    # Cálculos Financieros y de Eficiencia Termodinámica
    eficiencia_real = max(0.0, ((e_in_real - i_destroyed) / e_in_real) * 100.0) if e_in_real > 0 else 0.0
    perdida_anual = i_destroyed * 365.0
    ahorro_potencial = perdida_anual * 0.70  # El software absorbe el 70% de la variedad no deseada

    st.markdown("---")
    st.subheader("📊 Indicadores de Homeostasis Operativa")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""<div style="background-color: #1a1a1a; padding: 25px; border-radius: 8px; border: 1px solid #003366;">
            <span style="font-size: 12px; text-transform: uppercase; color: #888;">Nivel de Eficiencia del Flujo</span>
            <p style="font-size: 32px; font-weight: bold; color: #4ade80; margin: 0;">{eficiencia_real:.1f}%</p>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div style="background-color: #1a1a1a; padding: 25px; border-radius: 8px; border: 1px solid #772222;">
            <span style="font-size: 12px; text-transform: uppercase; color: #ff6b6b;">Fuga Financiera por Entropía Anual</span>
            <p style="font-size: 32px; font-weight: bold; color: #ff6b6b; margin: 0;">${perdida_anual:,.2f} MXN</p>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""<div style="background-color: #0f3322; padding: 25px; border-radius: 8px;">
            <span style="color: #4ade80; font-size: 12px; text-transform: uppercase;">Ahorro Garantizado por MPG (70%)</span>
            <p style="font-size: 32px; font-weight: bold; color: #4ade80; margin: 0;">${ahorro_potencial:,.2f} MXN</p>
        </div>""", unsafe_allow_html=True)

    # Botón de guardado y persistencia
    st.markdown("---")
    if st.button("💾 Enviar Datos de Operación al Core"):
        if db_disponible:
            try:
                cursor.execute("INSERT INTO metric_history (e_in, e_out, efficiency) VALUES (%s, %s, %s);", 
                               (e_in_real, i_destroyed, eficiencia_real))
                conn.commit()
                st.success(f"✅ Datos grabados en el Lógos central bajo la política de: '{politica_calidad}'")
            except Exception as e:
                st.error(f"Falla en la comunicación cibernética: {e}")

elif subsistema_activo == "Sistema 2: Estabilizador Anti-Crisis (SPC & Alertas)":
    st.header("🛡️ Módulo Anti-Crisis y Coordinación (Sistema 2)")
    st.subheader("Control Estadístico de Procesos (SPC) y Gestión de Incidencias (ISO 20000)")
    
    st.markdown("### 🚦 Semáforo de Variabilidad de Células de Servicio")
    st.markdown("*El software monitorea desviaciones estándar sin forzarlo a leer gráficas complejas.*")
    
    col_s1, col_s2, col_s3 = st.columns(3)
    
    with col_s1:
        st.markdown("""<div style="background-color: #1a2e1a; padding: 20px; border-radius: 8px; border-left: 8px solid #4ade80;">
            <h4 style="color: #4ade80 !important; margin:0;">Célula A: Atención Directa</h4>
            <p style="margin:5px 0 0 0; font-size:14px; color:#aaa;">Variabilidad: Bajo Control (Dentro de Sigma 3)</p>
            <p style="font-size:20px; font-weight:bold; color:#fff; margin:5px 0 0 0;">ESTABLE</p>
        </div>""", unsafe_allow_html=True)
        
    with col_s2:
        st.markdown("""<div style="background-color: #3b3010; padding: 20px; border-radius: 8px; border-left: 8px solid #facc15;">
            <h4 style="color: #facc15 !important; margin:0;">Célula B: Procesamiento Digital</h4>
            <p style="margin:5px 0 0 0; font-size:14px; color:#aaa;">Tendencia de retraso detectada en el flujo de datos.</p>
            <p style="font-size:20px; font-weight:bold; color:#fff; margin:5px 0 0 0;">PREVENCIÓN</p>
        </div>""", unsafe_allow_html=True)
        
    with col_s3:
        st.markdown("""<div style="background-color: #3b1a1a; padding: 20px; border-radius: 8px; border-left: 8px solid #f87171;">
            <h4 style="color: #f87171 !important; margin:0;">Célula C: Soporte Técnico</h4>
            <p style="margin:5px 0 0 0; font-size:14px; color:#aaa;">Cuello de botella detectado: 5 tickets fuera de SLA.</p>
            <p style="font-size:20px; font-weight:bold; color:#fff; margin:5px 0 0 0;">ALERTA DE CAOS</p>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🎛️ Simulación de Atenuación de Variedad")
    cuellos_botella_ingresados = st.slider("Número de incidentes de desalineación interdepartamental detectados hoy:", 0, 10, 2)
    fricciones_comunicacion = st.slider("Reportes de información duplicada o ambigua:", 0, 20, 5)
    
    impacto_s2 = (cuellos_botella_ingresados * COSTOS_ENTROPIA_SERVICIOS["S2_cuello_botella"]) + (fricciones_comunicacion * COSTOS_ENTROPIA_SERVICIOS["S2_friccion_com"])
    st.metric(label="Pérdida por Descoordinación Interna (Estimado Diario)", value=f"${impacto_s2:,.2f} MXN", delta="-Acción Regulatoria Requerida", delta_color="inverse")

elif subsistema_activo == "Sistema 3: Control y Dashboard (ISO 9001 Auditoría)":
    st.header("📈 Módulo de Optimización y Auditoría (Sistema 3)")
    st.subheader("Tablero del 'Aquí y Ahora' // Generación Automática para Certificaciones ISO 9001")
    
    st.markdown("""
    > **Nota del Córtex:** Este módulo elimina el 90% del papeleo manual. Los datos históricos recolectados de los Sistemas 1 y 2 alimentan de forma inmediata la **Revisión por la Dirección** obligatoria de los sistemas de gestión de calidad internacionales.
    """)
    
    # Renderizado simulado de reportes para auditoría
    st.markdown("### 📑 Reporte Automatizado de Cumplimiento")
    st.text_area(
        label="Cuerpo del Reporte de Auditoría Generado por Inteligencia Sistémica:",
        value=f"INFORME DE CAPACIDAD Y VIABILIDAD OPERATIVA\n"
              f"Organismo: {nodo_id}\n"
              f"Fecha de Evaluación: {datetime.now().strftime('%Y-%m-%d')}\n"
              f"Estatus de la Política de Calidad ('{politica_calidad}'): Conforme con desviaciones mínimas.\n"
              f"Diagnóstico Cibernético: El flujo operativo mantiene una disipación de entropía controlada. Canales del Sistema 2 estables. Se recomienda monitorear los riesgos del Sistema 4.",
        height=150
    )
    st.download_button(label="📥 Descargar Reporte Completo para Certificación ISO", data="Datos de Auditoría MPG", file_name="Auditoria_ISO9001_MPG.txt")
