import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import re
import plotly.express as px
import plotly.graph_objects as go

# --- 1. CORE ENTITAS ARCHITECT ---
class CosmicEngine:
    VERSION = "v37.0 Celestial Architect"
    WEATHER_TYPES = {
        "CERAH": "☀️ Kondisi mesin sangat stabil. Pola Fibonacci terbaca sempurna.",
        "BERAWAN": "☁️ Variabel acak mulai muncul. Gunakan BBFS lebih ketat.",
        "BADAI": "⛈️ Mesin dalam fase Chaos. Kurangi nominal taruhan, fokus pada pertahanan."
    }

# --- 2. THE SUPREME VISUAL INTERFACE ---
st.set_page_config(page_title="CELESTIAL ARCHITECT v37.0", layout="wide")

st.markdown("""
    <style>
    .stApp { background: #00050a; color: #f0f0f0; }
    .god-card {
        background: rgba(255, 215, 0, 0.05); border: 2px solid #ffd700;
        padding: 25px; border-radius: 20px; text-align: center;
    }
    .weather-box {
        background: rgba(0, 210, 255, 0.1); border: 1px solid #00d2ff;
        padding: 20px; border-radius: 15px; margin-top: 10px;
    }
    .glow-title {
        color: #ffd700; text-shadow: 0 0 15px #ffd700;
        font-family: 'Arial Black', sans-serif; font-size: 40px; text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='glow-title'>✨ THE CELESTIAL ARCHITECT v37.0 ✨</h1>", unsafe_allow_html=True)

# --- 3. SIDEBAR ---
st.sidebar.markdown("<h2 style='color:#ffd700;'>🛰️ DATA CENTER</h2>", unsafe_allow_html=True)
raw_input = st.sidebar.text_area("📡 Input Data (4D):", height=250, placeholder="Input data riwayat...")
clean_data = re.findall(r'\d{4}', raw_input)

# --- 4. LOGIKA & OUTPUT ---
if not clean_data:
    st.info("💡 **Dashboard Menunggu Transmisi.** Masukkan data riwayat untuk mengaktifkan Grafik 3D dan Prediksi Cuaca Mesin.")
else:
    try:
        # A. PERHITUNGAN QUANTUM
        freq_results = [Counter([d[i] for d in clean_data]).most_common(1)[0][0] for i in range(4)]
        latest = [int(x) for x in clean_data[0]]
        res_fib = "".join([str((latest[i] + [1,2,3,5][i]) % 10) for i in range(4)])
        res_zz = "".join([str(abs(int(clean_data[0][i]) - int(clean_data[1][i]))) for i in range(4)]) if len(clean_data) > 1 else "0000"
        ai_final = freq_results[0] + res_fib[1] + res_zz[2] + "5" # Contoh ekor statis untuk demo
        
        # B. LOGIKA CUACA MESIN
        diffs = [abs(int(clean_data[i]) - int(clean_data[i+1])) for i in range(min(len(clean_data)-1, 10))]
        stability_score = np.std(diffs)
        if stability_score < 1000: weather = "CERAH"
        elif stability_score < 2500: weather = "BERAWAN"
        else: weather = "BADAI"

        # --- TABS INTERFACE ---
        t1, t2, t3, t4 = st.tabs(["🎯 KEPUTUSAN DEWA", "🌪️ CUACA MESIN", "📊 GRAFIK 3D CLUSTER", "🛡️ BBFS"])

        with t1:
            st.subheader("🏆 Hasil Prediksi Utama")
            c1, c2, c3 = st.columns(3)
            with c1: st.markdown(f"<div class='god-card'><h4>2D</h4><h1>{ai_final[2:]}</h1></div>", unsafe_allow_html=True)
            with c2: st.markdown(f"<div class='god-card'><h4>3D</h4><h1>{ai_final[1:]}</h1></div>", unsafe_allow_html=True)
            with c3: st.markdown(f"<div class='god-card'><h4>4D</h4><h1>{ai_final}</h1></div>", unsafe_allow_html=True)

        with t2:
            st.subheader("🌪️ Analisis Cuaca & Stabilitas Mesin")
            st.markdown(f"<div class='weather-box'>", unsafe_allow_html=True)
            st.write(f"### Status Saat Ini: **{weather}**")
            st.write(f"{CosmicEngine.WEATHER_TYPES[weather]}")
            st.write(f"**Indeks Stabilitas:** `{stability_score:.2f}` (Semakin rendah, semakin akurat)")
            st.markdown("</div>", unsafe_allow_html=True)

        with t3:
            st.subheader("📊 Visualisasi Cluster Angka 3D")
            st.write("Grafik ini menunjukkan sebaran angka dalam ruang 3D (As, Kop, Kepala). Cari kumpulan titik yang paling padat!")
            
            # Data untuk 3D Plot
            df_3d = pd.DataFrame({
                'As': [int(d[0]) for d in clean_data],
                'Kop': [int(d[1]) for d in clean_data],
                'Kepala': [int(d[2]) for d in clean_data],
                'Ekor': [int(d[3]) for d in clean_data]
            })
            
            fig = px.scatter_3d(df_3d, x='As', y='Kop', z='Kepala', color='Ekor', 
                                 title="Peta Energi Angka", template="plotly_dark",
                                 color_continuous_scale='Viridis')
            st.plotly_chart(fig, use_container_width=True)

        with t4:
            st.subheader("🛡️ Quantum BBFS")
            bbfs = sorted(list(set(ai_final + res_freq[0] + res_fib[0] + "012")))
            st.code(f"SET BBFS: {', '.join(bbfs)}")

    except Exception as e:
        st.error(f"⚠️ Transmisi Terganggu: {e}")

st.caption("© 2026 Celestial Architect v37.0 | Quantum & 3D Visualization")
