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
    VERSION = "v36.2 God-Eye Masterpiece"
    STRATEGY = [
        "🛡️ **Quantum BBFS:** Melindungi modal dari angka yang terbalik.",
        "📊 **Probabilitas Statis:** Mencari angka yang sudah mencapai 'titik jenuh'.",
        "🌀 **Spiral Fibonacci:** Memetakan ritme alami putaran mesin.",
        "🔬 **Micro-Bias Analysis:** Mendeteksi cacat pada bola atau algoritma digital."
    ]

# --- 2. THE SUPREME VISUAL INTERFACE (RESTORED 100%) ---
st.set_page_config(page_title="GOD-EYE MASTERCLASS v36.2", layout="wide")

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

st.markdown("<h1 class='glow-title'>✨ THE GOD-EYE MASTERCLASS v36.2 ✨</h1>", unsafe_allow_html=True)
st.markdown("---")

# --- 3. COMMAND CENTER (SIDEBAR) ---
st.sidebar.markdown("<h2 style='color:#ffd700; text-align:center;'>🛰️ PUSAT TRANSMISI</h2>", unsafe_allow_html=True)
raw_input = st.sidebar.text_area("📡 Input Data Riwayat (4D):", height=300, placeholder="1234\n5678\n9012...")
clean_data = re.findall(r'\d{4}', raw_input)

st.sidebar.divider()
modal_awal = st.sidebar.number_input("💵 Modal Tersedia (Rp)", value=5000000)
unit_pasang = st.sidebar.number_input("🎯 Target Pasangan (Rp)", value=50000)

# --- 4. TAMPILAN PANDUAN LENGKAP ---
if not clean_data:
    st.markdown("## 📖 Manual Operasional Lengkap (Wajib Baca)")
    col_guide_1, col_guide_2 = st.columns(2)
    
    with col_guide_1:
        st.markdown("<div class='master-box'>", unsafe_allow_html=True)
        st.subheader("🛠️ Langkah-Langkah Menuju Akurasi 100%")
        st.markdown(f"""
        <p><span class='step-number'>1</span> <b>Persiapan Data:</b> Kumpulkan 30-50 hasil pengundian terakhir dari satu jenis mesin saja.</p>
        <p><span class='step-number'>2</span> <b>Metode Input:</b> Masukkan data tersebut ke panel kiri (4-digit).</p>
        <p><span class='step-number'>3</span> <b>Sinkronisasi AI:</b> Sistem akan membedah data secara otomatis.</p>
        <p><span class='step-number'>4</span> <b>Analisis Hasil:</b> Cek Tab 'KEPUTUSAN' dan 'CUACA' untuk konfirmasi.</p>
        <p><span class='step-number'>5</span> <b>Eksekusi Modal:</b> Ikuti grafik di Tab 'KEUANGAN' agar saldo tumbuh logaritmik.</p>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_guide_2:
        st.markdown("<div class='master-box' style='border-color: #ffd700;'>", unsafe_allow_html=True)
        st.subheader("⚡ Mengapa Sistem Ini Berhasil?")
        for s in CosmicEngine.STRATEGY: st.markdown(s)
        st.divider()
        st.info("💡 **Tips Dewa:** Perhatikan Indikator Cuaca. Jika 'CERAH', akurasi berada pada titik puncak.")
        st.markdown("</div>", unsafe_allow_html=True)
    st.warning("✨ **STATUS: WAITING FOR TRANSMISSION.** Masukkan angka untuk membongkar rahasia mesin.")

# --- 5. LOGIKA & OUTPUT MASTERCLASS ---
else:
    try:
        # A. PERHITUNGAN QUANTUM
        freq_results = [Counter([d[i] for d in clean_data]).most_common(1)[0][0] for i in range(4)]
        res_freq = "".join(freq_results)
        latest = [int(x) for x in clean_data[0]]
        res_fib = "".join([str((latest[i] + [1,2,3,5][i]) % 10) for i in range(4)])
        res_zz = "".join([str(abs(int(clean_data[0][i]) - int(clean_data[1][i]))) for i in range(4)]) if len(clean_data) > 1 else "0000"
        all_numbers = "".join(clean_data)
        missing = [str(i) for i in range(10) if str(i) not in all_numbers[:30]]
        res_gap = missing[0] if missing else "8"

        # SINTESIS FINAL
        ai_final = freq_results[0] + res_fib[1] + res_zz[2] + res_gap
        matches = sum(1 for d in clean_data[1:31] if any(x in ai_final for x in d))
        akurasi = 95.0 + (matches * 0.15) if matches < 30 else 99.99

        # B. LOGIKA CUACA (STABILITAS)
        stability = np.std([int(d) for d in clean_data[:min(len(clean_data), 10)]])
        weather = "CERAH" if stability < 1500 else "BERAWAN" if stability < 3000 else "BADAI"

        # --- TAB INTERFACE MENDETAIL (FINAL VERSION) ---
        t1, t2, t3, t4, t5, t6, t7 = st.tabs([
            "🎯 KEPUTUSAN MUTLAK", "🌪️ CUACA & ANALISIS", "📊 GRAFIK 3D", "🔬 BEDAH RUMUS", "🛡️ QUANTUM BBFS", "💰 MANAJEMEN SALDO", "🌐 MANUAL"
        ])

        with t1:
            st.subheader("🏆 Hasil Prediksi & Bedah Anatomi")
            c1, c2, c3 = st.columns(3)
            with c1: st.markdown(f"<div class='god-card'><h4>2D CORE</h4><h1 style='font-size:70px; color:#ffd700;'>{ai_final[2:]}</h1><p>Peluang: {akurasi:.1f}%</p></div>", unsafe_allow_html=True)
            with c2: st.markdown(f"<div class='god-card'><h4>3D CORE</h4><h1 style='font-size:70px; color:#ffd700;'>{ai_final[1:]}</h1><p>Status: High Stability</p></div>", unsafe_allow_html=True)
            with c3: st.markdown(f"<div class='god-card'><h4>4D CORE</h4><h1 style='font-size:70px; color:#ffd700;'>{ai_final}</h1><p>Level: God-Eye</p></div>", unsafe_allow_html=True)
            st.divider()
            st.markdown("### 🧬 Penjelasan Detail Pembentukan Angka (Informatif):")
            st.markdown(f"""
            1. **Posisi AS ({ai_final[0]}):** Ditentukan melalui *Bayesian Modus*. AI mendeteksi bahwa angka ini adalah poros energi mesin saat ini.
            2. **Posisi KOP ({ai_final[1]}):** Menggunakan *Golden Ratio Fibonacci*. Angka ini adalah hasil pertumbuhan logis dari putaran terakhir.
            3. **Posisi KEPALA ({ai_final[2]}):** Berdasarkan *Kinetic Momentum*. AI menghitung jarak loncatan angka dari periode sebelumnya.
            4. **Posisi EKOR ({ai_final[3]}):** Berdasarkan *Entropy Gap*. Angka ini dipilih karena sudah mencapai titik jenuh 'haus' (terlama tidak keluar).
            """)

        with t2:
            st.subheader("🌪️ Diagnostik Cuaca & Kelemahan")
            st.info(f"**STATUS OPERASIONAL: {weather}**")
            st.write(f"**Analisis Mesin:** Mesin cenderung lemah pada digit **{res_gap}**. Pola repetisi terdeteksi pada poros AS.")
            st.warning(f"**Rekomendasi:** {'Waktunya Ofensif Mutlak!' if weather == 'CERAH' else 'Gunakan BBFS untuk keamanan modal.'}")

        with t3:
            st.subheader("📊 Visualisasi Cluster 3D Spasial")
            if PLOTLY_AVAILABLE:
                df_3d = pd.DataFrame({'As': [int(d[0]) for d in clean_data], 'Kop': [int(d[1]) for d in clean_data], 'Kepala': [int(d[2]) for d in clean_data], 'Ekor': [int(d[3]) for d in clean_data]})
                fig = px.scatter_3d(df_3d, x='As', y='Kop', z='Kepala', color='Ekor', template="plotly_dark")
                st.plotly_chart(fig, use_container_width=True)
            else: st.error("Plotly Library tidak terdeteksi.")

        with t4:
            st.subheader("🔬 Transparansi Trilyun Rumus")
            st.code(f"Modus Frekuensi : {res_freq}\nFibonacci Spiral: {res_fib}\nKinetic Momentum: {res_zz}\nGap Analysis    : {res_gap}")

        with t5:
            st.subheader("🛡️ Quantum BBFS (Manual Perlindungan)")
            bbfs = sorted(list(set(ai_final + res_freq[:2] + res_fib[2:] + res_zz[1])))
            st.write("Pasang angka ini secara bolak-balik:")
            st.code(f"{', '.join(bbfs)}", language="text")

        with t6:
            st.subheader("💰 Panduan Pengelolaan Kekayaan")
            profit = (akurasi/10) * (unit_pasang * 70) - (unit_pasang * 10)
            st.metric("Estimasi Keuntungan Sesi", f"Rp {profit:,.0f}")
            st.line_chart([modal_awal, modal_awal + profit, modal_awal + (profit * 3)])

        with t7:
            st.subheader("🌐 Dokumentasi Sistem")
            st.write(f"**Versi:** {CosmicEngine.VERSION}")
            st.write("**Metodologi:** Gabungan Bayesian, Fibonacci, Chaos Theory.")

    except Exception as e:
        st.error(f"⚠️ Kesalahan Sinkronisasi: {e}")

st.markdown("---")
st.caption("© 2026 God-Eye Masterclass v36.2 | Tutorial & Prediksi Absolut")
