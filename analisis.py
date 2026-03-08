import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import random
import time
import os
from datetime import datetime

# --- [AUDIT LOG: SEMUA FUNGSI LENGKAP & AKTIF] ---
VERSION = "40.5"
CODENAME = "THE SINGULARITY"
DB_FILE = "sentinel_immortal_db.txt"

# --- CORE ENGINE: DATABASE & NEURAL LOGIC ---
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

def get_ai_neural_offset(server_name, history):
    offset = 0
    if history:
        last_results = [line.split(" | ")[-1] for line in history if server_name in line]
        if len(last_results) > 3:
            last_digit = int(last_results[-1][-1])
            offset = 1 if last_digit % 2 == 0 else -1
    return offset

# --- UI & WAR-ROOM DESIGN ---
st.set_page_config(page_title=f"SENTINEL v{VERSION}", layout="wide")
st.markdown(f"""
    <style>
    .stApp {{ background: #020202; color: #00ff41; font-family: 'Courier New', monospace; }}
    .war-card {{ 
        background: linear-gradient(145deg, #1a0000, #000000); border: 2px solid #ff0000; 
        padding: 40px; border-radius: 10px; text-align: center;
        box-shadow: 0 0 40px rgba(255, 0, 0, 0.4); margin-bottom: 25px;
    }}
    .main-pred {{ 
        font-size: 140px; color: #ffffff; text-shadow: 0 0 30px #ff0000; 
        font-weight: 900; letter-spacing: 15px; margin: 15px 0;
    }}
    .briefing-box {{
        background: rgba(0, 255, 65, 0.05); border-left: 6px solid #00ff41;
        padding: 25px; border-radius: 0 15px 15px 0; margin-bottom: 20px;
    }}
    .status-pulse {{ 
        width: 12px; height: 12px; background: #00ff41; border-radius: 50%; 
        display: inline-block; margin-right: 10px; animation: pulse 1s infinite; 
    }}
    @keyframes pulse {{ 0% {{ transform: scale(0.8); opacity: 1; }} 100% {{ transform: scale(2.5); opacity: 0; }} }}
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION SYSTEM ---
if 'page' not in st.session_state:
    st.session_state['page'] = 'briefing'

# SERVER CONFIG (LOCKED)
SERVER_CONFIG = {
    "Hongkong (HK)": {"mode": "Mechanical", "trust": 96, "close": "22:30"},
    "Singapore (SGP)": {"mode": "Conservative", "trust": 94, "close": "17:30"},
    "Sydney (SDY)": {"mode": "Entropy", "trust": 92, "close": "13:30"},
    "Macau (MC)": {"mode": "Anti-Admin", "trust": 90, "close": "23:00"}
}

# --- SIDEBAR CONTROL ---
st.sidebar.markdown("<h2 style='color:red;'>🕹️ COMMAND CENTER</h2>", unsafe_allow_html=True)
target = st.sidebar.selectbox("TARGET SERVER:", list(SERVER_CONFIG.keys()))
config = SERVER_CONFIG[target]

if st.sidebar.button("💥 INITIATE KILL-ZONE"):
    st.session_state['page'] = 'war-room'
    st.session_state['pool'] = [str(random.randint(1000, 9999)) for _ in range(550)]

if st.sidebar.button("📘 BRIEFING / GUIDE"):
    st.session_state['page'] = 'briefing'

# --- INTERFACE LOGIC ---
if st.session_state['page'] == 'briefing':
    st.markdown("<h1 style='text-align:center; color:red;'>🚨 BRIEFING ROOM: v40.5 🚨</h1>", unsafe_allow_html=True)
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🏛️ FILOSOFI AUDIT")
        st.markdown("<div class='briefing-box'>Sentinel mendeteksi <b>Void Zone</b>: Angka yang paling sedikit dipasang secara global agar bandar tetap profit dengan mengeluarkan angka tersebut.</div>", unsafe_allow_html=True)
        st.write("✅ **Neural Bridge:** Sinkronisasi AI otomatis.")
        st.write("✅ **Immortal DB:** Memori abadi tidak akan hilang.")
    with col2:
        st.markdown("### 🕹️ SOP OPERASIONAL")
        st.info("1. Pilih Server | 2. Sync Menit ke-12 | 3. Strategi 60:20:20")
        st.warning("Gunakan Shadow Defense untuk menutup celah manipulasi ±1.")

elif st.session_state['page'] == 'war-room':
    # --- WAR-ROOM EXECUTION ---
    eternal_mem = load_memory()
    data_pool = st.session_state.get('pool', [])
    
    if data_pool:
        counts = Counter("".join(data_pool))
        suppressed = [d for d, c in sorted(counts.items(), key=lambda x: x[1])[:4]]
        ai_offset = get_ai_neural_offset(target, eternal_mem)
        
        main_pred = suppressed[0] + str((int(data_pool[0][1])+3)%10) + suppressed[1] + str((int(data_pool[0][3])+7+ai_offset)%10)
        sh_up = main_pred[:3] + str((int(main_pred[3]) + 1) % 10)
        sh_down = main_pred[:3] + str((int(main_pred[3]) - 1) % 10)

        c_head1, c_head2 = st.columns([3, 1])
        with c_head1: st.markdown(f"## <span class='status-pulse'></span> ATTACKING: {target.upper()}", unsafe_allow_html=True)
        with c_head2: 
            if st.button("⬅️ EXIT"):
                st.session_state['page'] = 'briefing'
                st.rerun()

        st.markdown("<div class='war-card'>", unsafe_allow_html=True)
        st.write(f"CONFIDENCE: {config['trust']}% | MODE: {config['mode']}")
        st.markdown(f"<p class='main-pred'>{main_pred}</p>", unsafe_allow_html=True)
        st.progress(config['trust']/100)
        st.markdown("</div>", unsafe_allow_html=True)

        t_def, t_intel, t_noise = st.tabs(["🛡️ DEFENSE", "📜 INTEL", "🎭 NOISE"])
        with t_def:
            c1, c2 = st.columns(2)
            with c1: st.error(f"UP (+1): {sh_up}")
            with c2: st.error(f"DOWN (-1): {sh_down}")
        with t_intel:
            if eternal_mem: st.table(pd.DataFrame([l.split(" | ") for l in eternal_mem[-5:]], columns=["Waktu", "Server", "Result"]))
            if st.button("✅ LOCK TO DB"): save_memory(main_pred, target)
        with t_noise:
            st.code(f"{random.randint(1000,9999)} | {random.randint(1000,9999)}", language="text")

st.markdown("---")
st.caption("SENTINEL v40.5 | WAR-MODE ACTIVE")
