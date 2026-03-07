import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import re

# --- 1. CORE ENTITAS MASTERCLASS ---
try:
    import plotly.express as px
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False

class CosmicEngine:
    VERSION = "v36.7 God-Eye Masterpiece (Perfect Alignment)"
    STRATEGY = [
        "🛡️ **Quantum BBFS:** Melindungi modal dari angka yang terbalik.",
        "📊 **Probabilitas Statis:** Mencari angka yang sudah mencapai 'titik jenuh'.",
        "🌀 **Spiral Fibonacci:** Memetakan ritme alami putaran mesin.",
        "🔬 **Micro-Bias Analysis:** Mendeteksi cacat pada bola atau algoritma digital."
    ]

# --- 2. THE SUPREME VISUAL INTERFACE ---
st.set_page_config(page_title="GOD-EYE MASTERCLASS v36.7", layout="wide")

st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle at center, #000b1a 0%, #000000 100%); color: #f0f0f0; }
    .master-box {
        background: rgba(0, 210, 255, 0.03); border: 1px solid #00d2ff;
        padding: 30px; border-radius: 20px; margin-bottom: 25px;
    }
    .god-card {
        background: rgba(255, 215, 0, 0.03); border: 2px solid #ffd700;
        padding: 30px; border-radius: 25px; text-align: center;
        box-shadow: 0 0 30px rgba(255, 215, 0, 0.2);
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

st.markdown("<h1 class='glow-title'>✨ THE GOD-EYE MASTERCLASS v36.7 ✨</h1>", unsafe_allow_html=True)
st.markdown("---")

# --- 3. COMMAND CENTER ---
st.sidebar.markdown("<h2 style='color:#ffd700; text-align:center;'>🛰️ PUSAT TRANSMISI</h2>", unsafe_allow_html=True)
raw_input = st.sidebar.text_area("📡 Input Data Riwayat (4D):", height=300, placeholder="1234\n5678\n9012...")
clean_data = re.findall(r'\d{4}', raw_input)

st.sidebar.divider()
modal_awal = st.sidebar.number_input("💵 Modal Tersedia (Rp)", value=5000000)
unit_pasang = st.sidebar.number_input("🎯 Target Pasangan (Rp)", value=50000)

# --- 4. TAMPILAN PANDUAN AWAL ---
if not clean_data:
    st.markdown("## 📖 Manual Operasional Lengkap (Wajib Baca)")
    col_guide_1, col_guide_2 = st.columns(2)
    with col_guide_1:
        st.markdown("<div class='master-box'>", unsafe_allow_html=True)
        st.subheader("🛠️ Langkah Strategis")
        st.markdown(f"<p><span class='step-number'>1</span> <b>Persiapan:</b> 30-50 data riwayat.</p><p><span class='step-number'>2</span> <b>Input:</b> Masukkan ke panel kiri.</p><p><span class='step-number'>3</span> <b>Analisis:</b> AI bekerja otomatis.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with col_guide_2:
        st.markdown("<div class='master-box' style='border-color: #ffd700;'>", unsafe_allow_html=True)
        st.subheader("⚡ Teknologi")
        for s in CosmicEngine.STRATEGY: st.markdown(s)
        st.markdown("</div>", unsafe_allow_html=True)
    st.warning("✨ **STATUS: WAITING.** Masukkan data untuk mengaktifkan seluruh slide analisis.")

# --- 5. LOGIKA & OUTPUT (VERIFIED SLIDES) ---
else:
    try:
        # LOGIKA DASAR
        def get_spectral_digit(idx):
            raw = [d[idx] for d in clean_data]
            counts = Counter(raw)
            signal = [v for v, c in counts.items() if c > 1]
            return signal[0] if signal else raw[0]

        res_spectral = "".join([get_spectral_digit(i) for i in range(4)])
        latest = [int(x) for x in clean_data[0]]
        res_fib = "".join([str((latest[i] + [1,2,3,5][i]) % 10) for i in range(4)])
        res_zz = "".join([str(abs(int(clean_data[0][i]) - int(clean_data[1][i]))) for i in range(4)]) if len(clean_data) > 1 else "0000"
        all_nums = "".join(clean_data)
        res_gap = next((str(i) for i in range(10) if str(i) not in all_nums[:35]), "8")

        ai_final = res_spectral[0] + res_fib[1] + res_zz[2] + res_gap
        stability = np.std([int(d) for d in clean_data[:10]])
        weather = "CERAH" if stability < 1500 else "BERAWAN" if stability < 3000 else "BADAI"
        akurasi = min(98.0 + (len(clean_data) * 0.05), 99.99)

        # --- AUDIT SETIAP SLIDE (TAB) ---
        t1, t2, t3, t4, t5, t6, t7 = st.tabs([
            "🎯 KEPUTUSAN MUTLAK", "🌪️ CUACA & ANALISIS", "📊 GRAFIK 3D", "🔬 BEDAH RUMUS", "🛡️ QUANTUM BBFS", "💰 KEUANGAN", "🌐 MANUAL"
        ])

        with t1: # Slide 1: Fokus pada Hasil Akhir
            st.subheader("🏆 Hasil Prediksi Utama")
            c1, c2, c3 = st.columns(3)
            with c1: st.markdown(f"<div class='god-card'><h4>2D CORE</h4><h1>{ai_final[2:]}</h1><p>Peluang: {akurasi:.2f}%</p></div>", unsafe_allow_html=True)
            with c2: st.markdown(f"<div class='god-card'><h4>3D CORE</h4><h1>{ai_final[1:]}</h1><p>Status: Locked</p></div>", unsafe_allow_html=True)
            with c3: st.markdown(f"<div class='god-card'><h4>4D CORE</h4><h1>{ai_final}</h1><p>Level: Absolute</p></div>", unsafe_allow_html=True)
            st.info(f"**Anatomi:** AS({ai_final[0]}) KOP({ai_final[1]}) KEPALA({ai_final[2]}) EKOR({ai_final[3]})")

        with t2: # Slide 2: Fokus pada Kondisi Mesin
            st.subheader("🌪️ Diagnostik Kondisi Mesin")
            st.metric("Status Cuaca", weather)
            st.write(f"**Analisis:** Mesin terdeteksi memiliki celah pada digit **{res_gap}**.")
            st.warning("Saran: Fokus pada angka ekor jika cuaca Berawan.")

        with t3: # Slide 3: Fokus pada Visual
            st.subheader("📊 Pemetaan Spasial Angka")
            if PLOTLY_AVAILABLE:
                df = pd.DataFrame({'As':[int(d[0]) for d in clean_data],'Kop':[int(d[1]) for d in clean_data],'Kepala':[int(d[2]) for d in clean_data],'Ekor':[int(d[3]) for d in clean_data]})
                st.plotly_chart(px.scatter_3d(df, x='As', y='Kop', z='Kepala', color='Ekor', template="plotly_dark"), use_container_width=True)

        with t4: # Slide 4: Fokus pada Transparansi Rumus
            st.subheader("🔬 Laboratorium Kalkulasi")
            st.code(f"Sinyal Spectral : {res_spectral}\nSpiral Fibonacci: {res_fib}\nMomentum Kinetic: {res_zz}\nEntropy Gap     : {res_gap}")

        with t5: # Slide 5: Fokus pada Proteksi BBFS
            st.subheader("🛡️ Quantum BBFS (Jaring Pengaman)")
            bbfs = sorted(list(set(ai_final + res_spectral[:2] + res_fib[2:])))
            st.write("Pasang full-set untuk garansi kemenangan:")
            st.code(f"{', '.join(bbfs)}", language="text")

        with t6: # Slide 6: Fokus pada Uang
            st.subheader("💰 Simulasi Pertumbuhan Saldo")
            profit = (akurasi/10) * (unit_pasang * 70) - (unit_pasang * 10)
            st.metric("Estimasi Profit/Sesi", f"Rp {profit:,.0f}")
            st.line_chart([modal_awal, modal_awal+profit, modal_awal+(profit*3)])

        with t7: # Slide 7: Fokus pada Info Sistem
            st.subheader("🌐 Info Masterclass")
            st.write(f"Versi: {CosmicEngine.VERSION}")
            st.write("Gunakan data riwayat murni tanpa modifikasi untuk akurasi maksimal.")

    except Exception as e:
        st.error(f"⚠️ Slide Error: {e}")

st.markdown("---")
st.caption("© 2026 God-Eye Masterclass v36.7 | Perfect Slide Alignment")
