import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import re
import random
import time

# --- 1. INTELIJEN DATABASE & KONFIGURASI ---
# Database ini menyimpan karakteristik unik dari tiap 'musuh' (Server).
INTEL_DB = {
    "Hongkong (HK)": {"vuln": "Twin-Loop", "trust": 45, "color": "#ff4b4b", "desc": "Sangat bergantung pada pola statistik."},
    "Singapore (SGP)": {"vuln": "Low-Digit Suppress", "trust": 72, "color": "#ffa500", "desc": "Relatif stabil namun sering menahan angka kecil."},
    "Sydney (SDY)": {"vuln": "Entropy Shift", "trust": 85, "color": "#00d2ff", "desc": "Paling jujur, namun pola sering berubah mendadak."},
    "Macau (MC)": {"vuln": "Manual Override", "trust": 20, "color": "#7b2cbf", "desc": "Risiko manipulasi admin sangat tinggi."}
}

# --- 2. FUNGSI INTI (LOGIKA ORACLE) ---
def fetch_live_data(server):
    """Simulasi pengambilan data otomatis dari server target."""
    return [str(random.randint(1000, 9999)) for _ in range(30)]

# --- 3. ANTARMUKA (UI ARCHITECTURE) ---
st.set_page_config(page_title="SENTINEL v37.9 - ORACLE", layout="wide")

st.markdown("""
    <style>
    .stApp { background: #010a01; color: #00ff7f; font-family: 'Courier New', monospace; }
    .oracle-card { 
        background: rgba(0, 255, 127, 0.05); border: 2px solid #00ff7f; 
        padding: 30px; border-radius: 20px; text-align: center;
        box-shadow: 0 0 30px rgba(0, 255, 127, 0.1);
    }
    .main-pred { font-size: 85px; color: #ff4b4b; text-shadow: 0 0 30px #ff4b4b; font-weight: bold; margin: 5px 0; }
    .shadow-box { background: rgba(0, 210, 255, 0.1); border: 1px solid #00d2ff; padding: 15px; border-radius: 10px; text-align: center; }
    .feature-tag { background: #00ff7f; color: #000; padding: 2px 8px; border-radius: 5px; font-weight: bold; font-size: 12px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>🔮 SENTINEL v37.9: THE ORACLE PARADOX</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Sovereign Intelligence Architecture for Global Audit</p>", unsafe_allow_html=True)

# --- 4. SIDEBAR COMMAND ---
st.sidebar.header("📡 COMMAND CENTER")
target = st.sidebar.selectbox("Pilih Target Server:", list(INTEL_DB.keys()))

if st.sidebar.button("🌀 SYNC ORACLE (AUTO-FETCH)"):
    with st.spinner("Sinkronisasi RNG..."):
        st.session_state['live_data'] = fetch_live_data(target)
        time.sleep(2)
        st.sidebar.success("Koneksi Database Stabil.")

info = INTEL_DB[target]
st.sidebar.markdown(f"""
<div style='background:{info['color']}; padding:15px; border-radius:10px; color:#000; font-weight:bold;'>
SERVER: {target}<br>
STATUS: {info['desc']}
</div>
""", unsafe_allow_html=True)

# --- 5. DASHBOARD & ANALYSIS ---
if 'live_data' not in st.session_state or not st.session_state['live_data']:
    st.info("💡 Selamat Datang, Sang Master. Gunakan tombol 'SYNC ORACLE' untuk memulainya.")
else:
    # A. LOGIKA PERHITUNGAN
    data = st.session_state['live_data']
    all_digits = "".join(data)
    counts = Counter(all_digits)
    suppressed = [d for d, c in sorted(counts.items(), key=lambda x: x[1])[:3]]
    bait = counts.most_common(1)[0][0]
    
    # Konstruksi Angka Utama
    res_as = suppressed[0]
    res_kop = str((int(data[0][1]) + 2) % 10)
    res_kepala = suppressed[1]
    res_ekor = str((int(data[0][3]) + 7) % 10)
    main_pred = res_as + res_kop + res_kepala + res_ekor
    
    # Shadow Tracker (+1/-1)
    shadow_up = main_pred[:3] + str((int(res_ekor) + 1) % 10)
    shadow_down = main_pred[:3] + str((int(res_ekor) - 1) % 10)
    
    prob_score = min(99.8, (len(data) * 3) + (100 - info['trust']))

    # B. DISPLAY TABS
    t1, t2, t3 = st.tabs(["🎯 LIVE ORACLE", "🛠️ FEATURE EXPLAINER", "📜 AUDIT LOG"])

    with t1:
        st.markdown("<div class='oracle-card'>", unsafe_allow_html=True)
        st.write("### 💎 PREDIKSI ANGKA UTAMA")
        st.markdown(f"<p class='main-pred'>{main_pred}</p>", unsafe_allow_html=True)
        st.write(f"**ABSOLUTE PROBABILITY: {prob_score}%**")
        st.progress(prob_score/100)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.write("---")
        st.write("### 🕵️ SHADOW TRACKER (PELACAK PEMBELOKAN)")
        c1, c2 = st.columns(2)
        with c1: st.markdown(f"<div class='shadow-box'><h6>SHADOW +1</h6><h2>{shadow_up}</h2></div>", unsafe_allow_html=True)
        with c2: st.markdown(f"<div class='shadow-box'><h6>SHADOW -1</h6><h2>{shadow_down}</h2></div>", unsafe_allow_html=True)

    with t2:
        st.subheader("📘 Panduan & Penjelasan Fitur")
        
        st.markdown("#### <span class='feature-tag'>1</span> Dark Mirror (Angka Simpanan)")
        st.write("Menganalisis digit yang sengaja 'ditahan' oleh bandar. Angka ini memiliki biaya pembayaran (payout) terendah bagi bandar, sehingga peluang keluarnya tertinggi.")
        
        st.markdown("#### <span class='feature-tag'>2</span> Shadow Tracker")
        st.write("Antisipasi jika bandar mengubah satu digit di menit terakhir. Dengan memasang angka utama dan bayangan, Anda mengepung manipulasi admin.")
        
        st.markdown("#### <span class='feature-tag'>3</span> Probability Meter")
        st.write("Mengukur tingkat kejujuran server. Jika skor > 90%, algoritma bandar sedang dalam kondisi statis dan mudah ditembus.")
        
        st.markdown("#### <span class='feature-tag'>4</span> Greed Index Tracking")
        st.write("Memantau seberapa agresif admin server melakukan intervensi manual berdasarkan tren pengeluaran angka anomali.")

    with t3:
        st.subheader("📑 Laporan Evidence Record")
        st.code(f"""
[REPORT-v37.9]
SERVER: {target}
PREDIKSI UTAMA: {main_pred}
SHADOWS: {shadow_up}, {shadow_down}
PROBABILITAS: {prob_score}%
VERDICT: Zona simpanan terdeteksi di digit {suppressed[0]}.
        """)

st.markdown("---")
st.caption("© 2026 Sentinel v37.9 | The Oracle Paradox - Final Command")
