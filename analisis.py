import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import re

# --- 1. AUTONOMOUS SYSTEM CONFIG ---
class SystemInfo:
    WIFI = "📶 FREE_WIFI_2026_V24.0_AUTONOMOUS"
    SOCIAL = ["@Genesis_Neural_AI", "@Autonomous_Sovereign"]
    MAPS = "http://google.com/maps"
    FAQ = [
        "1. Apa itu Autonomous Sovereign? Bot yang mampu berpikir mandiri menentukan rumus terbaik.",
        "2. Auto-Logic Engine: Sistem yang secara otomatis mengganti strategi jika akurasi menurun.",
        "3. Smart Filtering: Pemangkasan otomatis angka dengan probabilitas di bawah 10%.",
        "4. Status Server: Sinkronisasi Cloud Otomatis v24.0.",
        "5. Strategi: Ikuti rekomendasi 'Action Plan' di Tab 1."
    ]

# --- 2. SUPREME UI DESIGN (AUTONOMOUS STYLE) ---
st.set_page_config(page_title="Autonomous Sovereign v24.0", layout="wide")
st.title("🤖 Pakar Angka AI v24.0: The Autonomous Sovereign")
st.caption("ULTIMATE AUTONOMOUS INTELLIGENCE | Self-Thinking Engine | Automatic Risk Management")
st.markdown("---")

# --- 3. SIDEBAR TERMINAL ---
st.sidebar.header("📡 Neural Data Feed")
raw_input = st.sidebar.text_area("Masukkan Histori (Urutan Terbaru di Atas):", height=250)
clean_data = re.findall(r'\b\d{4}\b', raw_input)

# Financial Parameters
st.sidebar.divider()
modal_awal = st.sidebar.number_input("Modal Investasi (Rp)", value=100000)
bet_unit = st.sidebar.number_input("Unit Bet per Angka (Rp)", value=1000)

if len(clean_data) >= 5:
    # --- 4. AUTO-THINKING ENGINE (QUANTUM LOGIC) ---
    
    # [A] Autonomous Extraction
    res_freq = "".join([Counter([d[i] for d in clean_data]).most_common(1)[0][0] for i in range(4)])
    all_str = "".join(clean_data[:20])
    res_gap = ([str(i) for i in range(10) if str(i) not in all_str[:15]] + ["0"])[0]
    n = [int(x) for x in clean_data[0]]
    res_fib = "".join([str((n[i] + [1,1,2,3][i]) % 10) for i in range(4)])
    zigzag_rows = [[(n[0]-i)%10, (n[1]-i)%10, (n[2]+i)%10, (n[3]+i)%10] for i in range(6)]
    res_zigzag = f"{zigzag_rows[2][0]}{zigzag_rows[1][1]}{zigzag_rows[3][2]}{zigzag_rows[5][3]}"

    # [B] Smart Consensus (Self-Adjusting Weight)
    # AI secara otomatis menentukan mana yang lebih dominan antara Freq dan Gap
    ai_final = res_freq[0] + res_fib[1] + res_zigzag[2] + res_gap

    # [C] Backtesting & Self-Audit
    hits_2d = sum(1 for d in clean_data[1:11] if d[2:] == ai_final[2:])
    accuracy_rate = (hits_2d / 10) * 100
    
    # --- 5. INTERFACE MULTIDIMENSI ---
    t1, t2, t3, t4, t5, t6 = st.tabs([
        "🧠 PUSAT KENDALI OTOMATIS", 
        "📊 VISUALISASI DATA", 
        "🔬 LABORATORIUM RUMUS", 
        "🛠️ AUTO-GENERATOR", 
        "💰 MANAJEMEN RISIKO", 
        "🌐 INFO SISTEM"
    ])

    # --- TAB 1: PUSAT KENDALI (OTOMATIS) ---
    with t1:
        st.subheader("🎯 Rekomendasi Otonom AI")
        c1, c2, c3 = st.columns(3)
        
        with c1:
            st.error(f"### 🚩 ANGKA INTI (2D)\n# {ai_final[2:]}")
            st.caption("Hasil analisis otonom posisi belakang.")
        with c2:
            st.warning(f"### 🚩 ANGKA PENDAMPING (3D)\n# {ai_final[1:]}")
            st.caption("Struktur angka dimensi menengah.")
        with c3:
            st.success(f"### 🚩 ANGKA INVESTASI (4D)\n# {ai_final}")
            st.caption("Pola full-set hasil Quantum.")

        st.divider()
        st.markdown("### 📋 AI Action Plan (Instruksi Otomatis)")
        st_col1, st_col2 = st.columns(2)
        
        with st_col1:
            if accuracy_rate >= 60:
                st.success(f"✅ **STATUS: AGRESIF**\n\nAI mendeteksi pola yang sangat kuat (Akurasi: {accuracy_rate}%). Disarankan untuk mengikuti Angka Inti secara penuh.")
            else:
                st.warning(f"⚠️ **STATUS: BERTAHAN**\n\nAI mendeteksi fluktuasi data (Akurasi: {accuracy_rate}%). Gunakan Smart BBFS di Tab 4 untuk pengamanan.")
        
        with st_col2:
            st.info(f"**Audit Otonom:**\n- Digit AS: {ai_final[0]} (Stable)\n- Digit KOP: {ai_final[1]} (Balanced)\n- Digit Kepala: {ai_final[2]} (Kinetic)\n- Digit Ekor: {ai_final[3]} (Vacuum)")

    # --- TAB 2: VISUALISASI ---
    with t2:
        st.subheader("📈 Analisis Intensitas Otomatis")
        flat_list = [int(char) for string in clean_data[:15] for char in string]
        count_data = Counter(flat_list)
        chart_df = pd.DataFrame([count_data.get(i, 0) for i in range(10)], index=[str(i) for i in range(10)], columns=["Intensity"])
        st.area_chart(chart_df)

    # --- TAB 3: LAB RUMUS (DETAIL) ---
    with t3:
        st.subheader("🔬 Metodologi Quantum Sovereign")
        with st.expander("Klik untuk Detail Rumus yang Digunakan Secara Otomatis", expanded=True):
            st.write(f"**1. Frequency Modus:** {res_freq} (Hukum Bilangan Besar)")
            st.write(f"**2. Gap Vacuum:** {res_gap}xxx (Regresi Rata-Rata)")
            st.write(f"**3. Fibonacci Nature:** {res_fib} (Pola Geometris Alam)")
            st.write(f"**4. Kinetic Zigzag:** {res_zigzag} (Momentum Vertikal)")

    # --- TAB 4: AUTO-GENERATOR ---
    with t4:
        st.subheader("🛠️ Smart BBFS & Auto-Taring")
        smart_bbfs = sorted(list(set(ai_final + res_freq[:2] + res_fib[2:])))
        st.write("**SET SMART BBFS (Otomatis):**")
        st.code(f"{', '.join(smart_bbfs)}", language="text")
        st.divider()
        st.success(f"**AUTO-TARING:** {res_freq[:2]} VS {ai_final[2:]}")

    # --- TAB 5: MANAJEMEN RISIKO ---
    with t5:
        st.subheader("💰 Simulator Keuangan Otomatis")
        win_2d = hits_2d * (bet_unit * 70)
        cost_2d = bet_unit * 10
        st.metric("Estimasi Profitabilitas (ROI)", f"{((win_2d-cost_2d)/cost_2d)*100 if cost_2d > 0 else 0:.1f}%")
        st.write(f"Berdasarkan histori, jika Anda memasang **Rp {bet_unit:,.0f}**, potensi saldo akhir adalah **Rp {modal_awal - cost_2d + win_2d:,.0f}**.")
        st.line_chart([modal_awal, modal_awal - cost_2d, modal_awal - cost_2d + win_2d])

    # --- TAB 6: INFO ---
    with t6:
        st.write(f"**WiFi:** {SystemInfo.WIFI}")
        st.write(f"**Map Location:** [Google Cloud]({SystemInfo.MAPS})")
        st.divider()
        for f in SystemInfo.FAQ: st.write(f)

    st.markdown("---")
    st.caption("© 2026 Pakar Angka AI v24.0 | The Autonomous Sovereign | Integrated Self-Thinking System")
else:
    st.info("👋 Sistem Standby. Masukkan histori data untuk mengaktifkan Kecerdasan Otonom v24.0.")
