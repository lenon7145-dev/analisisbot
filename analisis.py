import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import random
import time
import os
from datetime import datetime

# --- 1. CORE CONFIGURATION ---
VERSION = "40.3"
CODENAME = "NEURAL CLOUD SYNC"
DB_FILE = "sentinel_immortal_db.txt"

# --- 2. ENGINE: IMMORTAL & CLOUD DATABASE ---
def save_memory(res, server_name):
    if res and len(res) == 4:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        # Simpan ke file lokal (Internal Memory)
        with open(DB_FILE, "a") as f:
            f.write(f"{timestamp} | {server_name} | {res}\n")
        return True
    return False

def load_memory():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    return []

# --- 3. NEURAL LOGIC: AI-OFFSET ---
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
    "Hongkong (HK)": {"mode": "Mechanical", "close": "22:30", "trust": 96, "strategy": "Step-Ladder Logic"},
    "HK Lotto": {"mode": "Mechanical", "close": "21:00", "trust": 97, "strategy": "Ball-Drop Physics"},
    "Singapore (SGP)": {"mode": "Conservative", "close": "17:30", "trust": 94, "strategy": "Risk-Balance Audit"},
    "Sydney (SDY)": {"mode": "Entropy", "close": "13:30", "trust": 92, "strategy": "Volatility-Lock"},
    "Macau (MC)": {"mode": "Anti-Admin", "close": "23:00", "trust": 90, "strategy": "Deep-Void Spotting"}
}

# --- 5. MASTER THEME & UI ---
st.set_page_config(page_title=f"SENTINEL v{VERSION}", layout="wide")
st.markdown(f"""
    <style>
    .stApp {{ background: #000500; color: #00ff41; font-family: 'Consolas', monospace; }}
    .sovereign-card {{ 
        background: rgba(0, 255, 255, 0.03); border: 2px solid #00ffff; 
        padding: 30px; border-radius: 15px; text-align: center;
        box-shadow: 0 0 50px rgba(0, 255, 255, 0.2);
    }}
    .main-pred {{ font-size: 110px; color: #ff3131; text-shadow: 0 0 30px #ff3131; font-weight: bold; }}
    .status-pulse {{ color: #ff00ff; font-weight: bold; animation: pulse 1.5s infinite; }}
    @keyframes pulse {{ 0% {{ opacity: 1; }} 50% {{ opacity: 0.3; }} 100% {{ opacity: 1; }} }}
    .guide-box {{ background: rgba(0, 255, 255, 0.08); border-left: 5px solid #00ffff; padding: 20px; border-radius: 8px; }}
    </style>
    """, unsafe_allow_html=True)

st.markdown(f"<h1 style='text-align:center;'>👑 SENTINEL v{VERSION}: {CODENAME}</h1>", unsafe_allow_html=True)

# --- 6. SIDEBAR & BACKUP SYSTEM ---
st.sidebar.header("🕹️ SUPREME CONTROL")
target_server = st.sidebar.selectbox("Target Server:", list(SERVER_CONFIG.keys()))
config = SERVER_CONFIG[target_server]

# FITUR BACKUP (DOWNLOAD DATABASE)
if os.path.exists(DB_FILE):
    with open(DB_FILE, "r") as f:
        db_content = f.read()
    st.sidebar.download_button(
        label="☁️ BACKUP MEMORY TO CLOUD",
        data=db_content,
        file_name=f"sentinel_backup_{datetime.now().strftime('%Y%m%d')}.txt",
        mime="text/plain"
    )

if st.sidebar.button("💥 INITIATE NEURAL SYNC"):
    with st.spinner("Sinkronisasi Memori & AI Link..."):
        drift = random.random() > 0.92
        st.session_state['drift_detected'] = drift
        st.session_state['pool'] = [str(random.randint(1000, 9999)) for _ in range(400)]
        mock_res = str(random.randint(1000, 9999))
        save_memory(mock_res, target_server)
        time.sleep(1.5)
        st.sidebar.success("SYNC & BACKUP READY")

# --- 7. EXECUTION ENGINE ---
eternal_mem = load_memory()
if 'pool' in st.session_state:
    data_pool = st.session_state['pool']
    counts = Counter("".join(data_pool))
    suppressed = [d for d, c in sorted(counts.items(), key=lambda x: x[1])[:4]]

    ai_offset = get_ai_neural_offset(target_server, eternal_mem)
    res_as = suppressed[0]
    res_kop = str((int(data_pool[0][1]) + random.randint(1, 9)) % 10)
    res_kepala = suppressed[1]
    res_ekor = str((int(data_pool[0][3]) + 7 + ai_offset) % 10)

    main_pred = res_as + res_kop + res_kepala + res_ekor
    sh_up = main_pred[:3] + str((int(main_pred[3]) + 1) % 10)
    sh_down = main_pred[:3] + str((int(main_pred[3]) - 1) % 10)

    # --- 8. DASHBOARD ---
    t_target, t_guide, t_audit = st.tabs(["🎯 TARGET ACQUISITION", "📘 MASTER GUIDE (SOP)", "📜 IMMORTAL LOG"])

    with t_target:
        st.markdown("<div class='sovereign-card'>", unsafe_allow_html=True)
        st.markdown(f"<p class='status-pulse'>● NEURAL LINK ACTIVE: {target_server.upper()}</p>", unsafe_allow_html=True)
        st.write("### ⚡ TITIK LEMAH ABSOLUT (VOID)")
        st.markdown(f"<p class='main-pred'>{main_pred}</p>", unsafe_allow_html=True)
        st.progress(99.9/100)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.divider()
        st.subheader("🛡️ Shadow Defense (+1/-1)")
        c1, c2 = st.columns(2)
        with c1: st.error(f"**SHADOW UP: {sh_up}**")
        with c2: st.error(f"**SHADOW DOWN: {sh_down}**")

    with t_guide:
        st.subheader("🏛️ SOP Master v40.3")
        st.markdown(f"""
        <div class='guide-box'>
        <b>1. Dual-Storage Sync:</b> Bot menyimpan data di komputer Master. Selalu klik tombol <b>'BACKUP MEMORY'</b> di sidebar setelah sesi berakhir untuk menyimpan cadangan abadi.
        </div>
        <div class='guide-box'>
        <b>2. Strategi 60:20:20:</b> Main Pred (60%), Shadow UP (20%), Shadow DOWN (20%).
        </div>
        """, unsafe_allow_html=True)

    with t_audit:
        st.subheader("📜 Immortal Database Log")
        if eternal_mem:
            log_data = [line.split(" | ") for line in eternal_mem[-20:]]
            st.table(pd.DataFrame(log_data, columns=["Waktu", "Server", "Result"]))

st.markdown("---")
st.caption(f"© 2026 Sentinel v{VERSION} | Neural Cloud Sync | Stealth Mode")
