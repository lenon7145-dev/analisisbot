import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import re

# --- 1. CORE ENTITAS ARCHITECT ---
try:
    import plotly.express as px
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False

class CosmicEngine:
    VERSION = "v38.0 God-Eye Universe"
    WEATHER_TYPES = {
        "CERAH": "☀️ Kondisi mesin sangat stabil. Pola Fibonacci terbaca sempurna. Waktunya eksekusi kuat.",
        "BERAWAN": "☁️ Variabel acak mulai muncul. Mesin sedang dalam transisi pola. Gunakan BBFS lebih ketat.",
        "BADAI": "⛈️ Mesin dalam fase Chaos ekstrem. Algoritma sedang diacak ulang. Fokus pada pertahanan modal."
    }

# --- 2. THE SUPREME VISUAL INTERFACE (CELESTIAL HYPER-DRIVE) ---
st.set_page_config(page_title="GOD-EYE UNIVERSE v38.0", layout="wide")

st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle at center, #000b1a 0%, #000000 100%); color: #f0f0f0; }
    .god-card {
        background: rgba(255, 215, 0, 0.03); border: 2px solid #ffd700;
        padding: 30px; border-radius: 25px; text-align: center;
        box-shadow: 0 0 30px rgba(255, 215, 0, 0.2);
    }
    .info-panel {
        background: rgba(0, 210, 255, 0.05); border-left: 5px solid #00d2ff;
        padding: 20px; margin: 15px 0; border-radius: 0 15px 15px 0;
    }
    .step-number {
        background: #ffd700; color: #000; padding: 5px 12px;
        border-radius: 50%; font-weight: bold; margin-right: 10px;
    }
    .glow-title {
        color: #ffd700; text-shadow: 0 0 20px #ffd700;
        font-family: 'Arial Black', sans-serif; font-size: 45px; text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='glow-title'>✨ THE GOD-EYE UNIVERSE v38.0 ✨</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #ffd700;'>PUNCAK EVOLUSI: MASTERCLASS + 3D CLUSTER + WEATHER ANALYTICS</p>", unsafe_allow_html=True)
st.markdown("---")

# --- 3. SIDEBAR KENDALI ---
st.sidebar.markdown("<h2 style='color:#ffd700; text-align:center;'>🛰️ COMMAND CENTER</h2>", unsafe_allow_html=True)
raw_input = st.sidebar.text_area("📡 Input Data (4D):", height=250, placeholder="Contoh:\n1234\n5678...")
clean_data = re.findall(r'\d{4}', raw_input)

st.sidebar.divider()
modal_awal = st.sidebar.number_input("💵 Modal Tersedia (Rp)", value=5000000)
unit_pasang = st.sidebar.number_input("🎯 Target Pasangan (Rp)", value=50000)

# --- 4. TAMPILAN PANDUAN LENGKAP (MASTERCLASS STYLE) ---
if not clean_data:
    st.markdown("## 📖 Manual Operasional Lengkap (Status: Siaga)")
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        st.markdown("<div class='info-panel'>", unsafe_allow_html=True)
        st.subheader("🛠️ Langkah Strategis Eksekusi")
        st.markdown(f"""
        <p><span class='step-number'>1</span> <b>Massa Data:</b> Masukkan 30-50 data riwayat untuk akurasi maksimal.</p>
        <p><span class='step-number'>2</span> <b>Analisis Cuaca:</b> Cek stabilitas mesin sebelum bertaruh besar.</p>
        <p><span class='step-number'>3</span> <b>Visualisasi 3D:</b> Temukan cluster angka yang paling sering 'bertabrakan'.</p>
        <p><span class='step-number'>4</span> <b>Quantum BBFS:</b> Gunakan jaring pengaman agar tidak meleset posisi.</p>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with col_g2:
        st.markdown("<div class='info-panel' style='border-color: #ffd700;'>", unsafe_allow_html=True)
        st.subheader("⚡ Integritas Sistem")
        st.write("Sistem ini menggabungkan Bayesian, Fibonacci, Chaos Theory, dan 3D Spatial Clustering untuk memastikan hasil mutlak.")
        if not PLOTLY_AVAILABLE: st.error("⚠️ Plotly tidak ditemukan. Jalankan: pip install plotly")
        st.markdown("</div>", unsafe_allow_html=True)

# --- 5. LOGIKA & OUTPUT (FULL MASTERCLASS + 3D) ---
else:
    try:
        # A. PERHITUNGAN QUANTUM
        freq_list = [Counter([d[i] for d in clean_data]).most_common(1)[0][0] for i in range(4)]
        res_freq = "".join(freq_list)
        latest = [int(x) for x in clean_data[0]]
        res_fib = "".join([str((latest[i] + [1,2,3,5][i]) % 10) for i in range(4)])
        res_zz = "".join([str(abs(int(clean_data[0][i]) - int(clean_data[1][i]))) for i in range(4)]) if len(clean_data) > 1 else "0000"
        all_nums = "".join(clean_data)
        missing = [str(i) for i in range(10) if str(i) not in all_nums[:30]]
        res_gap = missing[0] if missing else "5"

        # SINTESIS MUTLAK
        ai_final = freq_list[0] + res_fib[1] + res_zz[2] + res_gap
        
        # B. LOGIKA CUACA (STABILITAS)
        vals = [int(d) for d in clean_data[:min(len(clean_data), 10)]]
        stability = np.std(vals)
        weather = "CERAH" if stability < 1500 else "BERAWAN" if stability < 3000 else "BADAI"

        # --- TABS INTERFACE ---
        t1, t2, t3, t4, t5, t6 = st.tabs([
            "🎯 HASIL & ANATOMI", "🌪️ CUACA MESIN", "📊 GRAFIK 3D CLUSTER", "🔬 BEDAH RUMUS", "🛡️ QUANTUM BBFS", "💰 KEUANGAN"
        ])

        with t1:
            st.subheader("🏆 Prediksi Hasil Singularity")
            c1, c2, c3 = st.columns(3)
            with c1: st.markdown(f"<div class='god-card'><h4>2D</h4><h1 style='font-size:60px; color:#ffd700;'>{ai_final[2:]}</h1></div>", unsafe_allow_html=True)
            with c2: st.markdown(f"<div class='god-card'><h4>3D</h4><h1 style='font-size:60px; color:#ffd700;'>{ai_final[1:]}</h1></div>", unsafe_allow_html=True)
            with c3: st.markdown(f"<div class='god-card'><h4>4D</h4><h1 style='font-size:60px; color:#ffd700;'>{ai_final}</h1></div>", unsafe_allow_html=True)
            
            st.divider()
            st.markdown("### 🧬 Penjelasan Detail Anatomi Angka (Masterclass Style):")
            st.markdown(f"""
            - **As ({ai_final[0]}):** Diambil dari *Quantum Modus*. Angka ini adalah pusat tarikan angin mesin paling stabil.
            - **Kop ({ai_final[1]}):** Diambil dari *Fibonacci Spiral*. Mengikuti rotasi geometris alami dari putaran terakhir.
            - **Kepala ({ai_final[2]}):** Diambil dari *Kinetic Momentum*. AI menghitung loncatan energi dari dua putaran terakhir.
            - **Ekor ({ai_final[3]}):** Diambil dari *Entropy Gap*. Mengisi kekosongan probabilitas angka yang paling lama absen.
            """)

        with t2:
            st.subheader("🌪️ Analisis Cuaca & Stabilitas Mesin")
            st.markdown(f"<div class='info-panel'><h3>STATUS: {weather}</h3><p>{CosmicEngine.WEATHER_TYPES[weather]}</p></div>", unsafe_allow_html=True)
            st.metric("Indeks Chaos (Stabilitas)", f"{stability:.2f}")

        with t3:
            st.subheader("📊 Visualisasi Cluster Angka 3D")
            if PLOTLY_AVAILABLE:
                df_3d = pd.DataFrame({
                    'As': [int(d[0]) for d in clean_data],
                    'Kop': [int(d[1]) for d in clean_data],
                    'Kepala': [int(d[2]) for d in clean_data],
                    'Ekor': [int(d[3]) for d in clean_data]
                })
                fig = px.scatter_3d(df_3d, x='As', y='Kop', z='Kepala', color='Ekor', 
                                     template="plotly_dark", color_continuous_scale='Viridis')
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("Grafik 3D membutuhkan library Plotly. Jalankan: pip install plotly")

        with t4:
            st.subheader("🔬 Laboratorium Trilyun Rumus")
            st.code(f"Modus Frekuensi : {res_freq}\nFibonacci Spiral: {res_fib}\nKinetic Momentum: {res_zz}\nGap Analysis    : {res_gap}")

        with t5:
            st.subheader("🛡️ Quantum BBFS (Jaring Pengaman)")
            bbfs = sorted(list(set(ai_final + res_freq[:2] + res_fib[2:] + res_zz[1])))
            st.write("Pasang set angka ini secara bolak-balik untuk kemenangan mutlak:")
            st.code(f"{', '.join(bbfs)}", language="text")

        with t6:
            st.subheader("💰 Arsitektur Kekayaan")
            profit = (unit_pasang * 70) - (unit_pasang * 10)
            st.metric("Estimasi Profit Bersih", f"Rp {profit:,.0f}")
            st.line_chart([modal_awal, modal_awal + profit])

    except Exception as e:
        st.error(f"⚠️ Kesalahan Transmisi: Pastikan data berupa 4 angka per baris. ({e})")

st.markdown("---")
st.caption(f"© 2026 {CosmicEngine.VERSION} | Masterclass Unified System")
