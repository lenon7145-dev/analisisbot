import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import re
import random
import time

# --- 1. CONFIG & DATABASE INTEL ---
INTEL_DB = {
    "Hongkong (HK)": {"vuln": "Twin-Loop", "trust": 45, "color": "#ff4b4b"},
    "Singapore (SGP)": {"vuln": "Low-Digit Suppress", "trust": 72, "color": "#ffa500"},
    "Sydney (SDY)": {"vuln": "Entropy Shift", "trust": 85, "color": "#00d2ff"},
    "Macau (MC)": {"vuln": "Manual Override", "trust": 20, "color": "#7b2cbf"}
}

# --- 2. AUTO-FETCH LOGIC (PENGAMBILAN DATA OTOMATIS) ---
def fetch_live_data(server):
    """
    Fungsi ini mensimulasikan pengambilan data otomatis dari server. 
    Nantinya bisa dihubungkan ke API atau URL database JoyPlay.
    """
    # Simulasi data riwayat otomatis (20 data terakhir)
    base_data = [str(random.randint(1000, 9999)) for _ in range(20)]
    return base_data

# --- 3. THEME & UI ---
st.set_page_config(page_title="SENTINEL v37.8 - AUTOMATOR", layout="wide")

st.markdown("""
    <style>
    .stApp { background: #020202; color: #00ff7f; font-family: 'Courier New', monospace; }
    .main-card { background: rgba(0, 255, 127, 0.05); border: 1px solid #00ff7f; padding: 25px; border-radius: 15px; text-align: center; }
    .prediction-text { font-size: 60px; color: #ff4b4b; text-shadow: 0 0 20px #ff4b4b; font-weight: bold; margin: 0; }
    .auto-status { color: #00d2ff; font-weight: bold; animation: blink 1s infinite; }
    @keyframes blink { 50% { opacity: 0; } }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>🏛️ SENTINEL v37.8: THE AUTOMATOR</h1>", unsafe_allow_html=True)

# --- 4. COMMAND CENTER ---
st.sidebar.header("📡 AUTO-FETCH COMMAND")
target = st.sidebar.selectbox("Pilih Target Server:", list(INTEL_DB.keys()))

# Tombol Refresh Otomatis
if st.sidebar.button("🔄 REFRESH DATA OTOMATIS"):
    with st.spinner(f"Menghubungkan ke Server {target}..."):
        st.session_state['live_data'] = fetch_live_data(target)
        time.sleep(1.5)
        st.sidebar.success("Koneksi Berhasil! Data Diperbarui.")

# Tampilan Status di Sidebar
info = INTEL_DB[target]
st.sidebar.markdown(f"<div style='background:{info['color']}; padding:10px; border-radius:10px; color:#000; font-weight:bold;'>"
                    f"SERVER: {target}<br>VULNERABILITY: {info['vuln']}</div>", unsafe_allow_html=True)

# --- 5. ENGINE & DASHBOARD ---
if 'live_data' not in st.session_state:
    st.session_state['live_data'] = []

current_data = st.session_state['live_data']

if not current_data:
    st.info("💡 Klik tombol **'REFRESH DATA OTOMATIS'** di sidebar untuk menarik data dari server.")
else:
    # A. Analisis Otomatis
    all_digits = "".join(current_data)
    counts = Counter(all_digits)
    suppressed = [d for d, c in sorted(counts.items(), key=lambda x: x[1])[:3]]
    bait = counts.most_common(1)[0][0]
    
    # B. Prediksi Anti-Bandar
    res_as = suppressed[0] if len(suppressed) > 0 else "0"
    res_kop = str((int(current_data[0][1]) + 3) % 10) 
    res_kepala = suppressed[1] if len(suppressed) > 1 else "1"
    res_ekor = str(random.randint(0, 9))
    final_pred = res_as + res_kop + res_kepala + res_ekor

    prob_score = min(98, (len(current_data) * 2) + (100 - info['trust']))
    
    # C. Dashboard
    t1, t2, t3 = st.tabs(["🎯 LIVE PREDICTION", "🧠 BANDAR PSYCHOLOGY", "📊 SERVER LOG"])

    with t1:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.markdown(f"<p class='auto-status'>● LIVE FEED FROM {target.upper()}</p>", unsafe_allow_html=True)
        st.write("### 🔮 ESTIMASI ANGKA KELUAR")
        st.markdown(f"<p class='prediction-text'>{final_res if 'final_res' in locals() else final_pred}</p>", unsafe_allow_html=True)
        st.write(f"**PROBABILITY: {prob_score}%**")
        st.progress(prob_score/100)
        st.markdown("</div>", unsafe_allow_html=True)

    with t2:
        st.subheader("🕵️ Analisis Musuh")
        c1, c2 = st.columns(2)
        with c1:
            st.error(f"**Digit Umpan (Bait): {bait}**")
            st.write("Bandar sedang memancing massa. Jangan gunakan digit ini.")
        with c2:
            st.success(f"**Digit Simpanan: {', '.join(suppressed)}**")
            st.write("Zona aman bandar untuk melepas payout.")

    with t3:
        st.subheader("📑 Log Riwayat Otomatis")
        st.write("Data terakhir yang ditarik dari server:")
        st.code(", ".join(current_data))
        st.markdown(f"**Total Data Sinkron:** {len(current_data)} periode")

st.markdown("---")
st.caption("© 2026 Sentinel v37.8 | The Automator - JoyPlay Intelligence")
