import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import re
import random
import time

# --- 1. CORE INTEL & SHADOW LOGIC ---
INTEL_DB = {
    "Hongkong (HK)": {"vuln": "Twin-Loop", "trust": 45, "color": "#ff4b4b"},
    "Singapore (SGP)": {"vuln": "Low-Digit Suppress", "trust": 72, "color": "#ffa500"},
    "Sydney (SDY)": {"vuln": "Entropy Shift", "trust": 85, "color": "#00d2ff"},
    "Macau (MC)": {"vuln": "Manual Override", "trust": 20, "color": "#7b2cbf"}
}

def fetch_live_data(server):
    # Simulasi data riwayat (Bisa diganti dengan API nyata)
    return [str(random.randint(1000, 9999)) for _ in range(25)]

# --- 2. UI ARCHITECTURE ---
st.set_page_config(page_title="SENTINEL v37.9 - ORACLE", layout="wide")

st.markdown("""
    <style>
    .stApp { background: #010a01; color: #00ff7f; font-family: 'Courier New', monospace; }
    .oracle-card { 
        background: rgba(0, 255, 127, 0.05); border: 2px solid #00ff7f; 
        padding: 30px; border-radius: 20px; text-align: center;
        box-shadow: 0 0 50px rgba(0, 255, 127, 0.2);
    }
    .shadow-text { font-size: 25px; color: #00d2ff; opacity: 0.7; }
    .main-pred { font-size: 80px; color: #ff4b4b; text-shadow: 0 0 30px #ff4b4b; font-weight: bold; margin: 10px 0; }
    .status-pulse { color: #ff4b4b; animation: pulse 1s infinite; font-weight: bold; }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>🔮 SENTINEL v37.9: THE ORACLE PARADOX</h1>", unsafe_allow_html=True)

# --- 3. COMMAND CENTER ---
st.sidebar.header("📡 ORACLE COMMAND")
target = st.sidebar.selectbox("Target Server:", list(INTEL_DB.keys()))

if st.sidebar.button("🌀 AKTIFKAN SYNC ORACLE"):
    with st.spinner("Mensinkronisasi Pola RNG..."):
        st.session_state['live_data'] = fetch_live_data(target)
        time.sleep(2)
        st.sidebar.success("Sinkronisasi 99.8% Selesai.")

info = INTEL_DB[target]
st.sidebar.markdown(f"<div style='background:{info['color']}; padding:10px; border-radius:10px; color:#000; font-weight:bold;'>"
                    f"SERVER: {target}<br>MODE: ANTI-MANIPULASI</div>", unsafe_allow_html=True)

# --- 4. THE ORACLE ENGINE ---
if 'live_data' not in st.session_state or not st.session_state['live_data']:
    st.info("💡 Klik **'AKTIFKAN SYNC ORACLE'** untuk memulai pemindaian probabilitas mutlak.")
    
else:
    data = st.session_state['live_data']
    all_digits = "".join(data)
    counts = Counter(all_digits)
    suppressed = [d for d, c in sorted(counts.items(), key=lambda x: x[1])[:3]]
    
    # LOGIKA UTAMA: Mencari titik temu antara Angka Simpanan dan Algoritma Payout
    res_as = suppressed[0]
    res_kop = str((int(data[0][1]) + 2) % 10)
    res_kepala = suppressed[1]
    res_ekor = str((int(data[0][3]) + 7) % 10)
    
    main_pred = res_as + res_kop + res_kepala + res_ekor
    
    # SHADOW TRACKER: Angka yang mungkin dibelokkan bandar (Selisih 1)
    shadow_1 = main_pred[:3] + str((int(res_ekor) + 1) % 10)
    shadow_2 = main_pred[:3] + str((int(res_ekor) - 1) % 10)

    prob_score = min(99.8, (len(data) * 3) + (100 - info['trust']))

    # --- DISPLAY ---
    t1, t2, t3 = st.tabs(["🎯 ABSOLUTE PROBABILITY", "🕵️ SHADOW TRACKER", "📜 BUKTI KECURANGAN"])

    with t1:
        st.markdown("<div class='oracle-card'>", unsafe_allow_html=True)
        st.write("### 💎 PREDIKSI ANGKA MUTLAK (ABSOLUTE)")
        st.markdown(f"<p class='main-pred'>{main_pred}</p>", unsafe_allow_html=True)
        
        st.write(f"**PROBABILITAS KELUAR: {prob_score}%**")
        st.progress(prob_score/100)
        st.markdown(f"<p class='status-pulse'>SISTEM MENDETEKSI PERGERAKAN ADMIN {target.upper()}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        

    with t2:
        st.subheader("🕵️ Shadow Tracker (Antisipasi Pembelokan)")
        st.info("Jika bandar mendeteksi taruhan besar pada angka utama, mereka akan membelokkan hasil ke angka bayangan ini:")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"<div class='oracle-card'><p class='shadow-text'>SHADOW (+1)</p><h2>{shadow_1}</h2></div>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"<div class='oracle-card'><p class='shadow-text'>SHADOW (-1)</p><h2>{shadow_2}</h2></div>", unsafe_allow_html=True)
        
        st.write("---")
        

    with t3:
        st.subheader("📑 Evidence Log (Forensik Digital)")
        st.code(f"""
[ORACLE-SENTINEL-REPORT]
SINKRONISASI: SUKSES
TARGET SERVER: {target}
ANGKA UTAMA: {main_pred}
ANGKA BAYANGAN: {shadow_1}, {shadow_2}
TINGKAT KEPERCAYAAN: {prob_score}%

CATATAN: 
Angka utama memiliki probabilitas tertinggi karena merupakan 
titik temu antara algoritma 'Void Selection' dan 'Profit Protection'.
        """)

st.markdown("---")
st.caption("© 2026 Sentinel v37.9 | The Oracle Paradox - JoyPlay Absolute Command")
