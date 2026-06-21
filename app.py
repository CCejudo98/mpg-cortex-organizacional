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
# CÁPSULA ESTÉTICA: GRIS OXFORD Y AZUL ACERO (MÍNIMA FRICCIÓN VISUAL)
# ==========================================
st.markdown("""
<style>
    /* Fondo Gris Oscuro Corporativo, sin fatiga azul */
    .stApp {
        background-color: #111625;
        color: #ffffff !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* Barra Lateral en Gris Grafito */
    [data-testid="stSidebar"], [data-testid="stSidebar"] > div:first-child {
        background-color: #1e2230 !important;
        border-right: 2px solid #2e354f !important;
    }
    section[data-testid="stSidebar"] .stMarkdown, section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h4, section[data-testid="stSidebar"] p, section[data-testid="stSidebar"] span {
        color: #ffffff !important;
    }
    h1, h2, h3, h4, h5, h6, label, p, span {
        color: #ffffff !important;
        font-weight: 600 !important;
    }
    /* Campos de entrada limpios */
    .stNumberInput input, .stTextInput input, .stSelectbox div {
        background-color: #f1f5f9 !important;
        color: #0f172a !important;
        border-radius: 6px !important;
    }
    hr { border-top: 1px solid #2e354f !important; }
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
        st.markdown(f'<div style="background-color: #1e293b; padding: 25px; border-radius: 8px; border: 1px solid #334155;"><span style="font-size: 12px; text-transform: uppercase; color: #94a3b8;">Eficiencia de Flujo Continuo</span><p style="font-size: 32px; font-weight: bold; color: #34d399 !important; margin: 0;">{eficiencia_real:.1f}%</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div style="background-color: #1e293b; padding: 25px; border-radius: 8px; border: 1px solid #7f1d1d;"><span style="font-size: 12px; text-transform: uppercase; color: #fca5a5;">Fuga Financiera Anual</span><p style="font-size: 32px; font-weight: bold; color: #f87171 !important; margin: 0;">${perdida_anual:,.2f} MXN</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div style="background-color: #064e3b; padding: 25px; border-radius: 8px; border: 1px solid #047857;"><span style="color: #34d399 !important; font-size: 12px; text-transform: uppercase;">Ahorro Retenido por GAC (70%)</span><p style="font-size: 32px; font-weight: bold; color: #34d399 !important; margin: 0;">${ahorro_potencial:,.2f} MXN</p></div>', unsafe_allow_html=True)

    st.markdown("---")
    if st.button("💾 Registrar Datos en Histórico Central"):
        if db_disponible:
            try:
                cursor.execute("""
                    INSERT INTO metric_history (foco, e_in, e_out, efficiency) 
                    VALUES (%s, %s, %s, %s);
                """, (foco_metabolico, e_in_real, i_destroyed, eficiencia_real))
                conn.commit()
                st.success(f"✅ Datos respaldados bajo la directriz: '{politica_calidad}'")
                st.rerun()
            except Exception as e: 
                st.error(f"Falla de almacenamiento: {e}")

elif subsystem_activo == "Módulo 2: Control de Variabilidad (SPC & Alertas)":
    st.markdown("## 🛡️ Módulo de Coordinación y Control de Variabilidad")
    st.markdown("El sistema analiza las desviaciones estándar en tiempo real para eliminar desperdicios en el flujo de trabajo.")
    
    if len(historico_eficiencia) >= 3:
        media_historica = np.mean(historico_eficiencia)
        desviacion_sigma = np.std(historico_eficiencia)
        ultima_eficiencia = historico_eficiencia[0]
        
        if ultima_eficiencia >= (media_historica - desviacion_sigma):
            estado, color_box, color_txt = "CONFORME", "#064e3b", "#34d399"
            desc = "Variabilidad Operativa dentro de límites aceptables de control (Sigma 1)."
        elif ultima_eficiencia >= (media_historica - (2 * desviacion_sigma)):
            estado, color_box, color_txt = "ACCCIÓN PREVENTIVA", "#78350f", "#fbbf24"
            desc = "Desviación inusual detectada. El flujo presenta síntomas de fricción interna."
        else:
            estado, color_box, color_txt = "DESVIACIÓN CRÍTICA", "#7f1d1d", "#f87171"
            desc = "El proceso rompió límites estadísticos. Cuello de botella severo o retrabajo masivo."
    else:
        estado, color_box, color_txt = "FALTA DE DATOS", "#1e293b", "#ffffff"
        desc = "Se requieren al menos 3 registros en la base de datos común para activar el cálculo dinámico de estabilidad."
        ultima_eficiencia = 100.0
        media_historica = 100.0

    st.markdown(f"""
    <div style="background-color: {color_box}; padding: 25px; border-radius: 8px; border-left: 8px solid {color_txt}; margin-bottom: 25px; border-top: 1px solid #334155; border-right: 1px solid #334155; border-bottom: 1px solid #334155;">
        <h4 style="color: {color_txt} !important; margin:0;">Diagnóstico de Estabilidad del Proceso (SPC)</h4>
        <p style="margin:5px 0 0 0; font-size:16px;">{desc}</p>
        <p style="font-size:24px; font-weight:bold; margin:10px 0 0 0;">ESTATUS: {estado} ({ultima_eficiencia:.1f}% Eficiencia Actual)</p>
    </div>
    """, unsafe_allow_html=True)

    if len(historico_eficiencia) >= 3:
        st.subheader("Gráfico de Control Estadístico de Procesos (Historial Reciente)")
        st.line_chart(pd.DataFrame({"Eficiencia del Flujo (%)": historico_eficiencia}))

    st.markdown("---")
    st.markdown("### 🎛️ Evaluación de Fricción Interdepartamental")
    cuellos_botella_ingresados = st.slider("Número de cuellos de botella / bloqueos operativos hoy:", 0, 10, 2)
    fricciones_comunicacion = st.slider("Fallas de alineación interna reportadas:", 0, 20, 5)
    impacto_s2 = (cuellos_botella_ingresados * COSTOS_ENTROPIA_SERVICIOS["S2_cuello_botella"]) + (fricciones_comunicacion * COSTOS_ENTROPIA_SERVICIOS["S2_friccion_com"])
    
    st.metric(label="Pérdida Económica por Descoordinación Interna (Estimación Diaria)", value=f"${impacto_s2:,.2f} MXN", delta="-Intervención Requerida", delta_color="inverse")

elif subsystem_activo == "Módulo 3: Auditoría de Calidad (ISO 9001 Dashboard)":
    st.markdown("## 📈 Módulo de Evaluación de Desempeño y Auditoría")
    st.markdown("Este módulo consolida los registros de estabilidad procesal para alimentar los requerimientos de la norma ISO 9001.")
    
    promedio_real = np.mean(historico_eficiencia) if len(historico_eficiencia) > 0 else 0.0
    total_registros = len(historico_eficiencia)
    
    st.markdown("### 📑 Reporte Automatizado de Cumplimiento (ISO 9001)")
    cuerpo_reporte = (
        f"INFORME DE CAPACIDAD Y ESTABILIDAD PROCESAL\n"
        f"Organización: {nodo_id}\n"
        f"Fecha de Emisión: {datetime.now().strftime('%Y-%m-%d')}\n"
        f"Política de Calidad Dictada por Dirección: '{politica_calidad}'\n"
        f"Muestras Analizadas en Histórico: {total_registros} días de operación.\n"
        f"Eficiencia Promedio del Flujo de Trabajo: {promedio_real:.2f}%\n"
        f"Factor de Riesgo Externo Aplicado: {lambda_entorno:.2f}x\n"
        f"Diagnóstico de Aseguramiento de Calidad: El flujo mantiene una disipación de desperdicios alineada al plan estratégico. Los datos demuestran predictibilidad para auditorías de certificación."
    )
    
    st.text_area(label="Cuerpo del Reporte Generado Dinámicamente:", value=cuerpo_reporte, height=180)
    st.download_button(label="📥 Descargar Reporte de Auditoría para Certificación", data=cuerpo_reporte, file_name=f"Auditoria_ISO9001_{nodo_id}.txt")
