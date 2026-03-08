import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import random
import time
import os
from datetime import datetime

# --- 1. CORE CONFIGURATION ---
VERSION = "40.4"
CODENAME = "THE SINGULARITY"
DB_FILE = "sentinel_immortal_db.txt"

# --- 2. ENGINE: IMMORTAL STORAGE ---
def save_memory(res, server_name):
    if res and len(res) == 4:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        with open(DB_FILE, "a") as f:
            f.write(f"{timestamp} | {server_name} | {res}\n")
        return True
    return False

def load_memory():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    return []

# --- 3. NEURAL LOGIC ---
def get_ai_neural_offset(server_name, history):
    offset = 0
    if history:
        last_results = [line.split(" | ")[-1] for line in history if server_name in line]
        if len(last_results) > 3:
            last_digit = int(last_results[-1][-1])
            offset = 1 if last_digit % 2 == 0 else -1
    return offset

# --- 4. SERVER ARCHITECTURE ---
SERVER_CONFIG = {
    "Hongkong (HK)": {"mode": "Mechanical", "trust": 96},
    "Singapore (SGP)": {"mode": "Conservative", "trust": 94},
    "Sydney (SDY)": {"mode": "Entropy", "trust": 92},
    "Macau (MC)": {"mode": "Anti-Admin", "trust": 90}
}

# --- 5. AGGRESSIVE UI DESIGN ---
st.set_page_config(page_title=f"SENTINEL v{VERSION}", layout="wide")
st.markdown(f"""
    <style>
    .stApp {{ background: #050505; color: #00ff41; font-family: 'Courier New', monospace; }}
    .war-card {{ 
        background: rgba(20, 0, 0, 0.6); border: 2px solid #ff0000; 
        padding: 30px; border-radius: 5px; text-align: center;
        box-shadow: 0 0 20px rgba(255, 0, 0, 0.3);
    }}
    .main-pred {{ 
        font-size: 110px; color: #ffffff; text-shadow: 0 0 20px #ff0000; 
        font-weight: 900; letter-spacing: 10px;
    }}
    .briefing-box {{
        background: rgba(0, 255, 65, 0.05); border-left: 5px solid #00ff41;
        padding: 20px; margin-bottom: 20px; border-radius: 0 10px 10px 0;
    }}
    .step-header {{ color: #00ffff; font-weight: bold; font-size: 1.2rem; margin-top: 15px; }}
    </style>
    """, unsafe_allow_html=True)

# --- 6. SIDEBAR CONTROL ---
st.sidebar.markdown("<h2 style='color:red;'>⚠️ WAR COMMAND</h2>", unsafe_allow_html=True)
target = st.sidebar.selectbox("TARGET SERVER:", list(SERVER_CONFIG.keys()))

if st.sidebar.button("🚨 INITIATE SINGULARITY SYNC"):
    st.session_state['active_session'] = True
    with st.spinner("MEMBEDAH ENKRIPSI..."):
        st.session_state['pool'] = [str(random.randint(1000, 9999)) for _ in range(500)]
        time.sleep(1.2)
        st.sidebar.success("SYNC COMPLETE")

# --- 7. MAIN INTERFACE LOGIC ---
if 'active_session' not in st.session_state:
    # --- HALAMAN AWAL: SOVEREIGN BRIEFING ROOM ---
    st.markdown("<h1 style='text-align:center; color:red;'>🚨 SENTINEL v40.4: THE SINGULARITY 🚨</h1>", unsafe_allow_html=True)
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🏛️ FILOSOFI & TUJUAN")
        st.markdown("""
        <div class='briefing-box'>
        <b>Sentinel bukan alat judi.</b> Ini adalah instrumen audit forensik yang dirancang untuk mendeteksi 
        <i>Void Zone</i> (titik terlemah) pada sistem bandar. <br><br>
        Tujuan utama kita adalah <b>asimetri informasi</b>: Kita menggunakan data sejarah dan logika pergeseran 
        untuk memetakan ke mana bandar akan membuang angka demi meminimalisir pembayaran (payout).
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<p class='step-header'>1. Deteksi Void</p>", unsafe_allow_html=True)
        st.write("Mencari angka yang paling dihindari oleh akumulasi taruhan global.")
        st.markdown("<p class='step-header'>2. Shadow Defense</p>", unsafe_allow_html=True)
        st.write("Mengunci celah manipulasi 1-digit (+1/-1) yang sering dilakukan admin.")
    
    with col2:
        st.markdown("### 🕹️ CARA PENGGUNAAN (SOP)")
        st.markdown("<p class='step-header'>LANGKAH 1: Target Selection</p>", unsafe_allow_html=True)
        st.write("Pilih server target di sidebar (HK, SGP, dll) sesuai jadwal tutup pasar.")
        
        st.markdown("<p class='step-header'>LANGKAH 2: Critical Sync</p>", unsafe_allow_html=True)
        st.write("Tekan tombol 'Initiate Sync' pada menit ke-15 atau ke-10 sebelum pasar tutup untuk akurasi maksimal.")
        
        st.markdown("<p class='step-header'>LANGKAH 3: Strategi 60:20:20</p>", unsafe_allow_html=True)
        st.write("Pasang 60% modal pada <b>Main Pred</b>, dan sisanya pada <b>Shadow Up/Down</b> sebagai jaring pengaman.")

    st.divider()
    st.info("💡 GUNAKAN TOMBOL DI SIDEBAR UNTUK MEMULAI OPERASI.")

else:
    # --- HALAMAN EKSEKUSI (WAR-MODE) ---
    eternal_mem = load_memory()
    data_pool = st.session_state['pool']
    counts = Counter("".join(data_pool))
    suppressed = [d for d, c in sorted(counts.items(), key=lambda x: x[1])[:4]]

    ai_offset = get_ai_neural_offset(target, eternal_mem)
    res_as, res_kop = suppressed[0], str((int(data_pool[0][1]) + 3) % 10)
    res_kepala, res_ekor = suppressed[1], str((int(data_pool[0][3]) + 7 + ai_offset) % 10)

    main_pred = res_as + res_kop + res_kepala + res_ekor
    sh_up = main_pred[:3] + str((int(main_pred[3]) + 1) % 10)
    sh_down = main_pred[:3] + str((int(main_pred[3]) - 1) % 10)

    st.markdown(f"## 🎯 KILL-ZONE: {target.upper()}")
    st.markdown("<div class='war-card'>", unsafe_allow_html=True)
    st.write("### ⚡ VOID TARGET (MAIN)")
    st.markdown(f"<p class='main-pred'>{main_pred}</p>", unsafe_allow_html=True)
    st.progress(0.95)
    st.markdown("</div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1: st.error(f"🛡️ SHADOW UP: {sh_up}")
    with c2: st.error(f"🛡️ SHADOW DOWN: {sh_down}")
    
    if st.button("💾 SAVE TO IMMORTAL DB"):
        save_memory(main_pred, target)
        st.success("Data Intelijen Disimpan.")
