import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import re

# --- 1. PRE-CHECK LIBRARY ---
try:
    import plotly.express as px
    import plotly.graph_objects as go
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False

# --- 2. KONFIGURASI SISTEM ---
class CosmicEngine:
    VERSION = "v37.1 Error-Proof Architect"
    WEATHER_TYPES = {
        "CERAH": "☀️ Kondisi mesin sangat stabil. Pola Fibonacci terbaca sempurna.",
        "BERAWAN": "☁️ Variabel acak mulai muncul. Gunakan BBFS lebih ketat.",
        "BADAI": "⛈️ Mesin dalam fase Chaos. Kurangi nominal taruhan, fokus pada pertahanan."
    }

# --- 3. TAMPILAN PREMIUM ---
st.set_page_config(page_title="ARCHITECT v37.1", layout="wide")

st.markdown("""
    <style>
    .stApp { background: #00050a; color: #f0f0f0; }
    .god-card { background: rgba(255, 215, 0, 0.05); border: 2px solid #ffd700; padding: 25px; border-radius: 20px; text-align: center; }
    .info-panel { background: rgba(0, 210, 255, 0.05); border-left: 5px solid #00d2ff; padding: 20px; border-radius: 0 15px 15px 0; }
    .glow-title { color: #ffd700; text-shadow: 0 0 15px #ffd700; font-family: 'Arial Black', sans-serif; font-size: 40px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='glow-title'>✨ THE CELESTIAL ARCHITECT v37.1 ✨</h1>", unsafe_allow_html=True)

# --- 4. SIDEBAR ---
st.sidebar.markdown("<h2 style='color:#ffd700;'>🛰️ DATA CENTER</h2>", unsafe_allow_html=True)
raw_input = st.sidebar.text_area("📡 Input Data Riwayat (4D):", height=250, placeholder="Contoh:\n1234\n5678...")
clean_data = re.findall(r'\d{4}', raw_input)

st.sidebar.divider()
modal_awal = st.sidebar.number_input("💵 Modal (Rp)", value=5000000)
unit_pasang = st.sidebar.number_input("🎯 Pasangan (Rp)", value=50000)

# --- 5. LOGIKA UTAMA ---
if not clean_data:
    st.markdown("<div class='info-panel'>", unsafe_allow_html=True)
    st.subheader("📖 Panduan Operasional & Failsafe")
    st.write("1. Masukkan minimal 20 baris angka di sidebar.")
    st.write("2. Cek Tab 'CUACA MESIN' untuk melihat stabilitas.")
    st.write("3. Gunakan Grafik 3D untuk melihat cluster angka.")
    if not PLOTLY_AVAILABLE:
        st.error("⚠️ Library 'plotly' belum terinstal. Jalankan: pip install plotly")
    st.markdown("</div>", unsafe_allow_html=True)
else:
    try:
        # A. KALKULASI DEWA
        freq_list = [Counter([d[i] for d in clean_data]).most_common(1)[0][0] for i in range(4)]
        res_freq = "".join(freq_list)
        latest = [int(x) for x in clean_data[0]]
        res_fib = "".join([str((latest[i] + [1,2,3,5][i]) % 10) for i in range(4)])
        res_zz = "".join([str(abs(int(clean_data[0][i]) - int(clean_data[1][i]))) for i in range(4)]) if len(clean_data) > 1 else "0000"
        
        all_numbers = "".join(clean_data)
        missing = [str(i) for i in range(10) if str(i) not in all_numbers[:30]]
        res_gap = missing[0] if missing else "5"
        
        ai_final = freq_list[0] + res_fib[1] + res_zz[2] + res_gap
        
        # B. LOGIKA CUACA (STABILITAS)
        if len(clean_data) > 5:
            vals = [int(d) for d in clean_data[:10]]
            stability = np.std(vals)
            weather = "CERAH" if stability < 1500 else "BERAWAN" if stability < 3000 else "BADAI"
        else:
            weather = "BERAWAN"
            stability = 0

        # --- TABS INTERFACE ---
        t1, t2, t3, t4, t5 = st.tabs(["🎯 HASIL MUTLAK", "🌪️ CUACA MESIN", "📊 GRAFIK 3D", "🛡️ BBFS", "💰 KEUANGAN"])

        with t1:
            st.subheader("🏆 Prediksi Singularity")
            c1, c2, c3 = st.columns(3)
            with c1: st.markdown(f"<div class='god-card'><h4>2D</h4><h1>{ai_final[2:]}</h1></div>", unsafe_allow_html=True)
            with c2: st.markdown(f"<div class='god-card'><h4>3D</h4><h1>{ai_final[1:]}</h1></div>", unsafe_allow_html=True)
            with c3: st.markdown(f"<div class='god-card'><h4>4D</h4><h1>{ai_final}</h1></div>", unsafe_allow_html=True)
            
            st.markdown("### 🧬 Penjelasan Detail:")
            st.write(f"- **As ({ai_final[0]}):** Berbasis Quantum Modus.\n- **Kop ({ai_final[1]}):** Berbasis Fibonacci Spiral.\n- **Kepala ({ai_final[2]}):** Berbasis Kinetic Momentum.\n- **Ekor ({ai_final[3]}):** Berbasis Entropy Gap.")

        with t2:
            st.subheader("🌪️ Analisis Cuaca Mesin")
            st.info(f"**Status: {weather}**\n\n{CosmicEngine.WEATHER_TYPES[weather]}")
            st.metric("Indeks Chaos", f"{stability:.2f}")

        with t3:
            st.subheader("📊 Cluster Angka 3D")
            if PLOTLY_AVAILABLE and len(clean_data) > 3:
                df = pd.DataFrame({
                    'As': [int(d[0]) for d in clean_data],
                    'Kop': [int(d[1]) for d in clean_data],
                    'Kepala': [int(d[2]) for d in clean_data],
                    'Ekor': [int(d[3]) for d in clean_data]
                })
                fig = px.scatter_3d(df, x='As', y='Kop', z='Kepala', color='Ekor', template="plotly_dark")
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("Data tidak cukup atau Plotly tidak terinstall.")

        with t4:
            st.subheader("🛡️ Quantum BBFS")
            bbfs_set = sorted(list(set(ai_final + res_freq[:2] + res_fib[2:])))
            st.code(f"ANGKA BBFS: {', '.join(bbfs_set)}")

        with t5:
            st.subheader("💰 Manajemen Profit")
            st.metric("Estimasi Profit", f"Rp {unit_pasang * 70:,.0f}")
            st.line_chart([modal_awal, modal_awal + (unit_pasang * 70)])

    except Exception as e:
        st.error(f"❌ Terjadi kesalahan pada data. Pastikan format 4-digit benar. Error: {e}")

st.caption(f"© 2026 {CosmicEngine.VERSION} | Stable & Informative")
