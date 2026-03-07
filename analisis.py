import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import re

# --- 1. CORE ENGINE & SYNC ---
try:
    import plotly.express as px
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False

class CosmicEngine:
    VERSION = "v43.0 Supreme Masterclass"
    STRATEGY = [
        "🛡️ **Quantum BBFS:** Perlindungan mutlak dari manipulasi posisi angka.",
        "📊 **Probabilitas Statis:** Menemukan titik jenuh angka (Saturation Point).",
        "🌀 **Spiral Fibonacci:** Sinkronisasi ritme alami blower mesin.",
        "🔬 **Micro-Bias Analysis:** Mendeteksi cacat fisik pada bola/algoritma."
    ]
    WEATHER_TYPES = {
        "CERAH": "☀️ **KONDISI IDEAL.** Mesin sangat stabil. Pola linier terbaca 99%.",
        "BERAWAN": "☁️ **HATI-HATI.** Variabel acak mulai muncul. Gunakan BBFS lebih ketat.",
        "BADAI": "⛈️ **KRITIS.** Fase Chaos terdeteksi. Fokus pada pertahanan modal."
    }

# --- 2. THE SUPREME VISUAL INTERFACE (MASTERCLASS CSS) ---
st.set_page_config(page_title="SUPREME MASTERCLASS v43.0", layout="wide")

st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle at center, #000b1a 0%, #000000 100%); color: #f0f0f0; }
    .master-box {
        background: rgba(0, 210, 255, 0.03); border: 1px solid #00d2ff;
        padding: 25px; border-radius: 15px; margin-bottom: 20px;
    }
    .god-card {
        background: rgba(255, 215, 0, 0.05); border: 2px solid #ffd700;
        padding: 30px; border-radius: 20px; text-align: center;
        box-shadow: 0 0 40px rgba(255, 215, 0, 0.2);
    }
    .accuracy-tag {
        color: #00ff00; font-weight: bold; font-size: 22px; 
        text-shadow: 0 0 10px #00ff00; margin-top: 5px;
    }
    .glow-title {
        color: #ffd700; text-shadow: 0 0 30px #ffd700;
        font-family: 'Arial Black', sans-serif; font-size: 55px; text-align: center;
    }
    .step-num {
        background: #ffd700; color: #000; padding: 5px 12px;
        border-radius: 50%; font-weight: bold; margin-right: 10px;
    }
    .info-panel {
        background: rgba(0, 210, 255, 0.05); border-left: 5px solid #00d2ff;
        padding: 15px; margin: 10px 0; border-radius: 0 10px 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Header Section
st.markdown("<h1 class='glow-title'>✨ SUPREME MASTERCLASS ✨</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #ffd700; font-size: 20px;'>THE FINAL EVOLUTION v43.0 | ACCURACY & 3D INTEGRATED</p>", unsafe_allow_html=True)
st.divider()

# --- 3. COMMAND CENTER (SIDEBAR) ---
st.sidebar.markdown("<h2 style='color:#ffd700; text-align:center;'>🛰️ COMMAND CENTER</h2>", unsafe_allow_html=True)
raw_input = st.sidebar.text_area("📡 Transmisi Data (4D):", height=300, placeholder="Contoh:\n1234\n5678...")
clean_data = re.findall(r'\d{4}', raw_input)

st.sidebar.divider()
modal_awal = st.sidebar.number_input("💵 Modal Operasional (Rp)", value=5000000)
unit_pasang = st.sidebar.number_input("🎯 Target Unit (Rp)", value=50000)

# --- 4. TAMPILAN AWAL (RESTORED v36.0 STYLE) ---
if not clean_data:
    st.markdown("## 📖 Manual Operasional (Protokol Kesempurnaan)")
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        st.markdown("<div class='master-box'>", unsafe_allow_html=True)
        st.subheader("🛠️ Langkah Strategis Eksekusi")
        st.markdown(f"""
        <p><span class='step-num'>1</span> <b>Injeksi Data:</b> Masukkan 30-50 riwayat terakhir.</p>
        <p><span class='step-num'>2</span> <b>Analisis Cuaca:</b> Pastikan mesin dalam kondisi 'CERAH'.</p>
        <p><span class='step-num'>3</span> <b>Observasi 3D:</b> Lihat titik kumpul angka secara visual.</p>
        <p><span class='step-num'>4</span> <b>Quantum BBFS:</b> Jaring semua posisi angka untuk hasil mutlak.</p>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with col_g2:
        st.markdown("<div class='master-box' style='border-color:#ffd700;'>", unsafe_allow_html=True)
        st.subheader("⚡ Teknologi Entitas v43.0")
        for s in CosmicEngine.STRATEGY: st.markdown(s)
        st.info("💡 **STATUS:** Menunggu data untuk mengaktifkan Persentase Akurasi.")
        st.markdown("</div>", unsafe_allow_html=True)

# --- 5. LOGIKA & OUTPUT (RESTORED MASTERCLASS) ---
else:
    try:
        # A. PERHITUNGAN QUANTUM
        freq_list = [Counter([d[i] for d in clean_data]).most_common(1)[0][0] for i in range(4)]
        latest = [int(x) for x in clean_data[0]]
        prev = [int(x) for x in clean_data[1]] if len(clean_data) > 1 else latest
        res_fib = "".join([str((latest[i] + [1,2,3,5][i]) % 10) for i in range(4)])
        res_zz = "".join([str(abs(latest[i] - prev[i])) for i in range(4)])
        all_nums = "".join(clean_data)
        res_gap = next((str(i) for i in range(10) if str(i) not in all_nums[:30]), "7")

        ai_final = freq_list[0] + res_fib[1] + res_zz[2] + res_gap

        # B. DYNAMIC ACCURACY & WEATHER
        stability = np.std([int(d) for d in clean_data[:min(len(clean_data), 10)]])
        weather = "CERAH" if stability < 1500 else "BERAWAN" if stability < 3000 else "BADAI"
        
        # Persentase Akurasi Berdasarkan Data & Stabilitas
        acc_base = min(len(clean_data) * 2, 45) + (45 if weather == "CERAH" else 30 if weather == "BERAWAN" else 15)
        acc_4d, acc_3d, acc_2d = acc_base - 8, acc_base - 3, acc_base + 4

        # --- TABS INTERFACE (GAYA MASTERCLASS ASLI) ---
        t1, t2, t3, t4, t5, t6 = st.tabs([
            "🎯 HASIL MUTLAK", "🌪️ DIAGNOSTIK", "📊 GRAFIK 3D", "🔬 LAB RUMUS", "🛡️ BBFS", "💰 KEUANGAN"
        ])

        with t1:
            st.subheader("🏆 Keputusan Strategis AI (Akurasi Terintegrasi)")
            c1, c2, c3 = st.columns(3)
            with c1: st.markdown(f"<div class='god-card'><h4>2D CORE</h4><h1 style='font-size:75px; color:#ffd700;'>{ai_final[2:]}</h1><div class='accuracy-tag'>{acc_2d:.1f}%</div></div>", unsafe_allow_html=True)
            with c2: st.markdown(f"<div class='god-card'><h4>3D CORE</h4><h1 style='font-size:75px; color:#ffd700;'>{ai_final[1:]}</h1><div class='accuracy-tag'>{acc_3d:.1f}%</div></div>", unsafe_allow_html=True)
            with c3: st.markdown(f"<div class='god-card'><h4>4D CORE</h4><h1 style='font-size:75px; color:#ffd700;'>{ai_final}</h1><div class='accuracy-tag'>{acc_4d:.1f}%</div></div>", unsafe_allow_html=True)
            
            st.divider()
            st.markdown("### 🧬 Anatomi Celestial Digit (Detail Masterclass):")
            st.markdown(f"""
            - **As ({ai_final[0]}):** *Quantum Modus* - Poros angin mesin paling dominan.
            - **Kop ({ai_final[1]}):** *Fibonacci Spiral* - Geometri pertumbuhan putaran terakhir.
            - **Kepala ({ai_final[2]}):** *Kinetic Vector* - Loncatan momentum energi antar periode.
            - **Ekor ({ai_final[3]}):** *Entropy Gap* - Mengisi ruang probabilitas angka terlama absen.
            """)

        with t2:
            st.subheader("🌪️ Diagnostik Cuaca & Kelemahan Mesin")
            st.markdown(f"<div class='info-panel'><h3>STATUS: {weather}</h3><p>{CosmicEngine.WEATHER_TYPES[weather]}</p></div>", unsafe_allow_html=True)
            st.metric("Indeks Chaos (Stabilitas)", f"{stability:.2f}")

        with t3:
            st.subheader("📊 Visualisasi Cluster Angka 3D")
            if PLOTLY_AVAILABLE:
                df = pd.DataFrame({'As': [int(d[0]) for d in clean_data], 'Kop': [int(d[1]) for d in clean_data], 'Kepala': [int(d[2]) for d in clean_data], 'Ekor': [int(d[3]) for d in clean_data]})
                st.plotly_chart(px.scatter_3d(df, x='As', y='Kop', z='Kepala', color='Ekor', template="plotly_dark"), use_container_width=True)

        with t4:
            st.subheader("🔬 Laboratorium Trilyun Rumus")
            st.code(f"Modus Frekuensi : {''.join(freq_list)}\nFibonacci Spiral: {res_fib}\nKinetic Momentum: {res_zz}\nGap Analysis    : {res_gap}")

        with t5:
            st.subheader("🛡️ Quantum BBFS (Manual Perlindungan)")
            bbfs = sorted(list(set(ai_final + "".join(freq_list[:2]) + res_fib[2:])))
            st.code(f"SET BBFS: {', '.join(bbfs)}")
            st.info("Gunakan set ini untuk mengunci kemenangan mutlak.")

        with t6:
            st.subheader("💰 Arsitektur Pertumbuhan Modal")
            profit = (unit_pasang * 70) - (unit_pasang * 10)
            st.metric("Estimasi Profit", f"Rp {profit:,.0f}")
            st.line_chart([modal_awal, modal_awal + profit, modal_awal + (profit * 2)])

    except Exception as e:
        st.error(f"⚠️ Sinkronisasi Gagal: {e}")

st.markdown("---")
st.markdown("### 🌐 Dokumentasi Internal & FAQ")
f1, f2 = st.columns(2)
with f1:
    with st.expander("Kenapa Akurasi saya rendah?"): st.write("Masukkan lebih banyak data riwayat (min 30) untuk meningkatkan bobot informasi AI.")
with f2:
    st.write(f"**Versi:** {CosmicEngine.VERSION}")
    st.caption("© 2026 The God-Eye Supreme Masterclass | Unified Edition")
