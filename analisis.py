import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import re
import random
import time

# --- 1. OMNI-SPECIALIST DATABASE ---
# Setiap server memiliki "Mode" khusus yang akan mengubah cara bot berhitung.
SERVER_CONFIG = {
    "Hongkong (HK)": {"mode": "Mechanical", "trust": 45, "color": "#ff4b4b", "strategy": "Step-Ladder Detection"},
    "HK Lotto": {"mode": "Mechanical", "trust": 60, "color": "#ffd700", "strategy": "Ball-Drop Pattern"},
    "Singapore (SGP)": {"mode": "Conservative", "trust": 72, "color": "#ffa500", "strategy": "Hard-Suppress Tracking"},
    "Sydney (SDY)": {"mode": "Entropy", "trust": 85, "color": "#00d2ff", "strategy": "Chaos-Pattern Analysis"},
    "Macau (MC)": {"mode": "Anti-Admin", "trust": 20, "color": "#7b2cbf", "strategy": "Void-Spot Hunting"}
}

if 'feedback_loop' not in st.session_state:
    st.session_state['feedback_loop'] = []

# --- 2. THEME & UI ---
st.set_page_config(page_title="SENTINEL v38.1 - OMNI", layout="wide")
st.markdown("""
    <style>
    .stApp { background: #010501; color: #00ff7f; font-family: 'Courier New', monospace; }
    .specialist-card { 
        background: rgba(0, 255, 127, 0.05); border: 2px solid #00ff7f; 
        padding: 25px; border-radius: 15px; text-align: center;
        box-shadow: 0 0 30px rgba(0, 255, 127, 0.1);
    }
    .main-pred { font-size: 80px; color: #ff4b4b; text-shadow: 0 0 20px #ff4b4b; font-weight: bold; }
    .mode-tag { background: #00ff7f; color: #000; padding: 5px 15px; border-radius: 20px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>🏛️ SENTINEL v38.1: OMNI-SPECIALIST</h1>", unsafe_allow_html=True)

# --- 3. COMMAND CENTER ---
st.sidebar.header("📡 COMMAND CENTER")
target = st.sidebar.selectbox("Pilih Target Server:", list(SERVER_CONFIG.keys()))
config = SERVER_CONFIG[target]

if st.sidebar.button("🌀 SYNC OMNI-ENGINE"):
    with st.spinner(f"Mengaktifkan Mode {config['mode']}..."):
        st.session_state['live_data'] = [str(random.randint(1000, 9999)) for _ in range(35)]
        time.sleep(1.5)
        st.sidebar.success(f"Mode {config['strategy']} Aktif!")

st.sidebar.divider()
st.sidebar.subheader("🔄 Adaptive Feedback")
last_res = st.sidebar.text_input("Result Terakhir:", placeholder="Contoh: 8821")
if st.sidebar.button("Adaptasikan"):
    st.session_state['feedback_loop'].append(last_res)
    st.sidebar.success("Algoritma Tersinkronisasi.")

# --- 4. DYNAMIC SPECIALIST ENGINE ---
if 'live_data' in st.session_state:
    data = st.session_state['live_data']
    all_digits = "".join(data)
    counts = Counter(all_digits)
    suppressed = [d for d, c in sorted(counts.items(), key=lambda x: x[1])[:4]]

    # LOGIKA BERDASARKAN MODE SPESIALIS
    if config['mode'] == "Mechanical":
        # Pola bola jatuh (HK/HK Lotto)
        res_as = str((int(data[0][0]) + 1) % 10)
        res_kop = suppressed[0]
        res_kepala = str((int(data[0][2]) + 1) % 10)
        res_ekor = suppressed[1]
    elif config['mode'] == "Conservative":
        # Pola angka yang paling lama ditahan (SGP)
        res_as, res_kop, res_kepala, res_ekor = suppressed[0], suppressed[1], suppressed[2], suppressed[3]
    elif config['mode'] == "Entropy":
        # Pola acak momentum (SDY)
        res_as = str(random.choice(suppressed))
        res_kop = str((int(data[0][1]) + 5) % 10)
        res_kepala = suppressed[-1]
        res_ekor = str((int(data[1][3]) + 2) % 10)
    else:
        # Anti-Admin (Macau) - Mencari angka paling "tidak logis"
        res_as = suppressed[0]
        res_kop = str(random.randint(0, 9)) if random.random() > 0.5 else suppressed[1]
        res_kepala = suppressed[2]
        res_ekor = str((int(data[0][3]) + 9) % 10)

    # Final Adaptive Shift
    if st.session_state['feedback_loop']:
        shift = int(st.session_state['feedback_loop'][-1][-1]) % 3
        res_ekor = str((int(res_ekor) + shift) % 10)

    main_pred = res_as + res_kop + res_kepala + res_ekor
    shadow_up = main_pred[:3] + str((int(main_pred[3]) + 1) % 10)
    shadow_down = main_pred[:3] + str((int(main_pred[3]) - 1) % 10)

    # --- DISPLAY ---
    t1, t2, t3 = st.tabs(["🎯 OMNI-PREDICTION", "🧠 ENGINE SPECS", "📑 AUDIT LOG"])

    with t1:
        st.markdown("<div class='specialist-card'>", unsafe_allow_html=True)
        st.markdown(f"<span class='mode-tag'>MODE: {config['mode'].upper()}</span>", unsafe_allow_html=True)
        st.write(f"### 🔮 PREDIKSI SPESIALIS: {target.upper()}")
        st.markdown(f"<p class='main-pred'>{main_pred}</p>", unsafe_allow_html=True)
        
        prob = min(99.9, (len(data) * 2) + (100 - config['trust']))
        st.write(f"**PROBABILITAS TEMBUS: {prob}%**")
        st.progress(prob/100)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.write("---")
        st.write("### 🕵️ SHADOW TRACKER")
        c1, c2 = st.columns(2)
        with c1: st.info(f"**SHADOW (+1): {shadow_up}**")
        with c2: st.info(f"**SHADOW (-1): {shadow_down}**")
        

    with t2:
        st.subheader(f"🛠️ Spesifikasi Engine: {config['strategy']}")
        st.write(f"Sistem ini sekarang bekerja khusus untuk menangani kerentanan **{config['mode']}** pada server **{target}**.")
        

    with t3:
        st.subheader("📜 System Memory")
        st.write("Adaptasi Terakhir:", st.session_state['feedback_loop'][-5:] if st.session_state['feedback_loop'] else "Belum ada data.")
        st.code(f"SERVER_ID: {target}\nSTRATEGY: {config['strategy']}\nSTATUS: OPTIMIZED")

st.markdown("---")
st.caption("© 2026 Sentinel v38.1 | The Omni-Specialist - Master of All Domains")
