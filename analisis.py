import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import random
import time
import os
from datetime import datetime

# --- 1. CORE CONFIGURATION (LOCKED) ---
VERSION = "40.5"
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

# --- 3. NEURAL LOGIC & DRIFT DETECTOR ---
def get_ai_neural_offset(server_name, history):
    offset = 0
    if history:
        last_results = [line.split(" | ")[-1] for line in history if server_name in line]
        if len(last_results) > 3:
            last_digit = int(last_results[-1][-1])
            offset = 1 if last_digit % 2 == 0 else -1
    return offset

def detect_extreme_drift(history, current_pred):
    if not history: return False
    last_res = history[-1].split(" | ")[-1]
    diff = sum(1 for a, b in zip(last_res, current_pred) if a != b)
    return diff >= 3

# --- 4. SERVER ARCHITECTURE (COMPLETE) ---
SERVER_CONFIG = {
    "Hongkong (HK)": {"mode": "Mechanical", "trust": 96, "close": "22:30", "signal": "⚡ HIGH"},
    "Singapore (SGP)": {"mode": "Conservative", "trust": 94, "close": "17:30", "signal": "📡 STABLE"},
    "Sydney (SDY)": {"mode": "Entropy", "trust": 92, "close": "13:30", "signal": "🌀 VOLATILE"},
    "Macau (MC)": {"mode": "Anti-Admin", "trust": 90, "close": "23:00", "signal": "🔥 AGGRESSIVE"}
}

# --- 5. ULTRA-AGRESIVE UI DESIGN (ALL VERSION MERGED) ---
st.set_page_config(page_title=f"SENTINEL v{VERSION}", layout="wide")
st.markdown(f"""
    <style>
    .stApp {{ background: #020202; color: #00ff41; font-family: 'Courier New', monospace; }}
    
    /* Global Glow Card */
    .war-card {{ 
        background: linear-gradient(145deg, #1a0000, #000000); border: 2px solid #ff0000; 
        padding: 40px; border-radius: 10px; text-align: center;
        box-shadow: 0 0 50px rgba(255, 0, 0, 0.5); margin-bottom: 25px;
    }}
    
    .main-pred {{ 
        font-size: 140px; color: #ffffff; text-shadow: 0 0 30px #ff0000, 0 0 70px #ff0000; 
        font-weight: 900; letter-spacing: 15px; margin: 10px 0;
    }}
    
    .critical-alert {{ 
        background: #ff0000; color: white; padding: 15px; font-weight: bold; 
        text-align: center; animation: blinker 0.8s linear infinite; border: 3px solid white; margin-bottom: 15px;
    }}
    @keyframes blinker {{ 50% {{ opacity: 0; }} }}
    
    .briefing-box {{
        background: rgba(0, 255, 65, 0.08); border-left: 6px solid #00ff41;
        padding: 25px; border-radius: 0 15px 15px 0; margin-bottom: 20px;
        box-shadow: 10px 0 30px rgba(0,255,65,0.1);
    }}
    
    .status-pulse {{ 
        width: 15px; height: 15px; background: #00ff41; border-radius: 50%; 
        display: inline-block; margin-right: 10px; animation: pulse 1.2s infinite; 
    }}
    @keyframes pulse {{ 0% {{ transform: scale(0.8); opacity: 1; }} 100% {{ transform: scale(2.8); opacity: 0; }} }}
    
    .step-header {{ color: #00ffff; font-weight: bold; font-size: 1.3rem; margin-top: 15px; }}
    </style>
    """, unsafe_allow_html=True)

# --- 6. NAVIGATION LOGIC ---
if 'page' not in st.session_state:
    st.session_state['page'] = 'briefing'

st.sidebar.markdown("<h2 style='color:red; text-align:center;'>⚠️ COMMAND CENTER</h2>", unsafe_allow_html=True)
target = st.sidebar.selectbox("TARGET SERVER:", list(SERVER_CONFIG.keys()))
config = SERVER_CONFIG[target]

if st.sidebar.button("🚨 INITIATE KILL-ZONE"):
    st.session_state['page'] = 'war-room'
    with st.spinner("MEMBEDAH SISTEM..."):
        st.session_state['pool'] = [str(random.randint(1000, 9999)) for _ in range(550)]
        time.sleep(1.5)

if st.sidebar.button("📘 BRIEFING / GUIDE"):
    st.session_state['page'] = 'briefing'

st.sidebar.divider()
st.sidebar.markdown(f"**STATUS:** <span style='color:#00ff41;'>● ONLINE</span>", unsafe_allow_html=True)
st.sidebar.markdown(f"**SIGNAL:** {config['signal']}")

# --- 7. MAIN INTERFACE ---

if st.session_state['page'] == 'briefing':
    # --- HALAMAN BRIEFING (KEMBALI LENGKAP) ---
    st.markdown("<h1 style='text-align:center; color:red;'>🚨 BRIEFING ROOM: THE SINGULARITY 🚨</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#00ffff;'>SOVEREIGN AUDIT INSTRUMENT v40.5</p>", unsafe_allow_html=True)
    st.divider()

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 🏛️ FILOSOFI & TUJUAN")
        st.markdown(f"""<div class='briefing-box'>
        <b>Sentinel v{VERSION}</b> mendeteksi <i>Void Zone</i>: Titik di mana bandar paling aman secara finansial untuk mengeluarkan angka karena minimnya pemasang.
        </div>""", unsafe_allow_html=True)
        st.markdown("<p class='step-header'>• Void Selection</p>", unsafe_allow_html=True)
        st.write("Menganalisis akumulasi titik data terendah dari 550 sampel.")
        st.markdown("<p class='step-header'>• Shadow Defense</p>", unsafe_allow_html=True)
        st.write("Mengunci celah manipulasi ±1 digit.")
    
    with c2:
        st.markdown("### 🕹️ SOP OPERASIONAL")
        st.info(f"TARGET: {target} | JAM TUTUP: {config['close']}")
        st.markdown("<p class='step-header'>1. Critical Sync</p>", unsafe_allow_html=True)
        st.write("Sync dilakukan 12-15 menit sebelum jam tutup pasar.")
        st.markdown("<p class='step-header'>2. Strategi 60:20:20</p>", unsafe_allow_html=True)
        st.write("60% Main Pred, 20% Shadow Up, 20% Shadow Down.")

elif st.session_state['page'] == 'war-room':
    # --- HALAMAN EKSEKUSI (DENGAN ALERTI DRIFT) ---
    eternal_mem = load_memory()
    data_pool = st.session_state.get('pool', [])
    
    if data_pool:
        # Core Calculation
        counts = Counter("".join(data_pool))
        suppressed = [d for d, c in sorted(counts.items(), key=lambda x: x[1])[:4]]
        ai_offset = get_ai_neural_offset(target, eternal_mem)
        
        main_pred = suppressed[0] + str((int(data_pool[0][1])+3)%10) + suppressed[1] + str((int(data_pool[0][3])+7+ai_offset)%10)
        sh_up = main_pred[:3] + str((int(main_pred[3]) + 1) % 10)
        sh_down = main_pred[:3] + str((int(main_pred[3]) - 1) % 10)
        
        # Drift Detection (KEMBALI AKTIF)
        is_drift = detect_extreme_drift(eternal_mem, main_pred)

        c_head1, c_head2 = st.columns([3, 1])
        with c_head1:
            st.markdown(f"## <span class='status-pulse'></span> ATTACKING: {target.upper()}", unsafe_allow_html=True)
        with c_head2:
            if st.button("⬅️ EXIT WAR-ZONE"):
                st.session_state['page'] = 'briefing'
                st.rerun()

        if is_drift:
            st.markdown("<div class='critical-alert'>🚨 DETEKSI INTERVENSI MANUAL BANDAR: JANGAN ALL-IN! 🚨</div>", unsafe_allow_html=True)

        st.markdown("<div class='war-card'>", unsafe_allow_html=True)
        st.markdown(f"<span style='color:#00ffff;'>CONFIDENCE: {config['trust']}% | CLOSE: {config['close']}</span>", unsafe_allow_html=True)
        st.markdown(f"<p class='main-pred'>{main_pred}</p>", unsafe_allow_html=True)
        st.progress(config['trust']/100)
        st.markdown("</div>", unsafe_allow_html=True)

        # Tabs Terintegrasi
        t_def, t_intel, t_noise = st.tabs(["🛡️ DEFENSE SYSTEM", "📜 INTEL LOG", "🎭 NOISE TOOLS"])
        
        with t_def:
            col_u, col_d = st.columns(2)
            with col_u: st.error(f"**SHADOW UP (+1)**\n## {sh_up}")
            with col_d: st.error(f"**SHADOW DOWN (-1)**\n## {sh_down}")
            st.caption("Gunakan jaring pengaman ini untuk mematikan celah manipulasi ±1.")

        with t_intel:
            if eternal_mem:
                st.table(pd.DataFrame([l.split(" | ") for l in eternal_mem[-10:]], columns=["Time", "Server", "Result"]))
            if st.button("✅ LOCK RESULT TO DB"):
                if save_memory(main_pred, target): st.success("Target Terkunci.")

        with t_noise:
            st.write("Pasang angka acak ini dengan nominal kecil sebagai kamuflase:")
            st.code(f"{random.randint(1000,9999)} | {random.randint(1000,9999)}", language="text")

st.markdown("---")
st.caption(f"SENTINEL v{VERSION} | OPERATIONAL SOVEREIGNTY | {datetime.now().year}")
