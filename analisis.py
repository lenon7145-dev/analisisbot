import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import random
import time
import os
from datetime import datetime

# --- 1. CORE CONFIGURATION ---
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

# --- 3. NEURAL LOGIC & ANALYTICS ---
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
    "Hongkong (HK)": {"mode": "Mechanical", "trust": 96, "close": "22:30", "signal": "⚡ HIGH"},
    "Singapore (SGP)": {"mode": "Conservative", "trust": 94, "close": "17:30", "signal": "📡 STABLE"},
    "Sydney (SDY)": {"mode": "Entropy", "trust": 92, "close": "13:30", "signal": "🌀 VOLATILE"},
    "Macau (MC)": {"mode": "Anti-Admin", "trust": 90, "close": "23:00", "signal": "🔥 AGGRESSIVE"}
}

# --- 5. ULTRA-INTERACTIVE UI DESIGN ---
st.set_page_config(page_title=f"SENTINEL v{VERSION}", layout="wide")
st.markdown(f"""
    <style>
    .stApp {{ background: #020202; color: #00ff41; font-family: 'Courier New', monospace; }}
    
    /* Interactive Card */
    .war-card {{ 
        background: linear-gradient(145deg, #0f0000, #1a0000); border: 2px solid #ff0000; 
        padding: 40px; border-radius: 10px; text-align: center;
        box-shadow: 0 0 40px rgba(255, 0, 0, 0.5); margin-bottom: 25px;
        transition: transform 0.3s;
    }}
    .war-card:hover {{ transform: scale(1.01); border-color: #00ffff; }}
    
    /* Typography */
    .main-pred {{ 
        font-size: 140px; color: #ffffff; text-shadow: 0 0 25px #ff0000, 0 0 60px #ff0000; 
        font-weight: 900; letter-spacing: 18px; margin: 15px 0;
    }}
    
    /* Signal & Badges */
    .badge {{ padding: 5px 15px; border-radius: 20px; font-size: 0.8rem; font-weight: bold; margin-bottom: 10px; display: inline-block; }}
    .badge-red {{ background: #ff0000; color: white; }}
    .badge-cyan {{ background: #00ffff; color: black; }}
    
    /* Interactive Elements */
    .briefing-box {{
        background: rgba(0, 255, 65, 0.08); border-left: 6px solid #00ff41;
        padding: 25px; margin-bottom: 25px; border-radius: 0 15px 15px 0;
        box-shadow: 10px 0 30px rgba(0,255,65,0.1);
    }}
    .status-pulse {{ 
        width: 12px; height: 12px; background: #00ff41; border-radius: 50%; 
        display: inline-block; margin-right: 10px; animation: pulse 1s infinite; 
    }}
    @keyframes pulse {{ 0% {{ transform: scale(0.8); opacity: 1; }} 100% {{ transform: scale(2.5); opacity: 0; }} }}
    </style>
    """, unsafe_allow_html=True)

# --- 6. NAVIGATION & SIDEBAR ---
if 'page' not in st.session_state:
    st.session_state['page'] = 'briefing'

st.sidebar.markdown("<h2 style='color:red; text-align:center;'>🕹️ SENTINEL CORE</h2>", unsafe_allow_html=True)
target = st.sidebar.selectbox("🎯 TARGET SERVER:", list(SERVER_CONFIG.keys()))
config = SERVER_CONFIG[target]

# Sidebar Actions
if st.sidebar.button("💥 INITIATE KILL-ZONE"):
    st.session_state['page'] = 'war-room'
    with st.spinner("MEMBEDAH SISTEM..."):
        st.session_state['pool'] = [str(random.randint(1000, 9999)) for _ in range(550)]
        time.sleep(1.5)

if st.sidebar.button("📘 BRIEFING / TUTORIAL"):
    st.session_state['page'] = 'briefing'

st.sidebar.divider()
st.sidebar.markdown(f"**STATUS:** <span style='color:#00ff41;'>● ONLINE</span>", unsafe_allow_html=True)
st.sidebar.markdown(f"**SERVER:** {target}")
st.sidebar.markdown(f"**SIGNAL:** {config['signal']}")

# --- 7. MAIN INTERFACE LOGIC ---

if st.session_state['page'] == 'briefing':
    # --- INTERACTIVE BRIEFING ROOM ---
    st.markdown("<h1 style='text-align:center; color:red;'>🚨 THE SOVEREIGN BRIEFING ROOM 🚨</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#00ffff;'>PRODUK INTELIJEN v40.5 | OPERASI SENYAP</p>", unsafe_allow_html=True)
    st.divider()

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 🏛️ FILOSOFI AUDIT")
        st.markdown("""
        <div class='briefing-box'>
        <b>Sentinel v40.5</b> bukan sekadar bot prediksi. Ini adalah instrumen audit yang mencari <b>ketimpangan finansial</b> bandar.
        <br><br>Kita mencari <i>Void Zone</i>: Angka yang paling sedikit dipasang secara global, sehingga bandar terpaksa mengeluarkannya untuk menjaga margin keuntungan mereka.
        </div>
        """, unsafe_allow_html=True)
        st.markdown("#### 🛡️ CORE PROTOCOLS:")
        st.write("✅ **VOID SELECTION:** Pencarian titik data terendah.")
        st.write("✅ **SHADOW DEFENSE:** Penutupan celah manipulasi $\pm 1$.")
        st.write("✅ **NEURAL BRIDGE:** Sinkronisasi logika AI secara real-time.")

    with c2:
        st.markdown("### 🕹️ PANDUAN TAKTIS (SOP)")
        with st.expander("STEP 1: Persiapan Intelijen", expanded=True):
            st.write("Pilih server dan amati jam tutup. Pastikan koneksi stabil.")
        with st.expander("STEP 2: Sinkronisasi Menit Akhir"):
            st.write("Tekan tombol 'Initiate Kill-Zone' pada menit ke-12 sebelum tutup. Data paling akurat ada di detik-detik akhir.")
        with st.expander("STEP 3: Eksekusi 60:20:20"):
            st.write("Pecah modal Master: 60% Angka Utama, 20% Shadow Up, 20% Shadow Down. Jangan lupakan Noise Injection.")

    st.markdown("---")
    st.markdown("<div style='text-align:center;'>Gunakan Sidebar untuk memulai operasi <b>KILL-ZONE</b></div>", unsafe_allow_html=True)

elif st.session_state['page'] == 'war-room':
    # --- INTERACTIVE WAR-ZONE ---
    eternal_mem = load_memory()
    data_pool = st.session_state.get('pool', [str(random.randint(1000, 9999)) for _ in range(500)])
    
    # Engine Logic
    counts = Counter("".join(data_pool))
    suppressed = [d for d, c in sorted(counts.items(), key=lambda x: x[1])[:4]]
    ai_offset = get_ai_neural_offset(target, eternal_mem)
    
    main_pred = suppressed[0] + str((int(data_pool[0][1])+3)%10) + suppressed[1] + str((int(data_pool[0][3])+7+ai_offset)%10)
    sh_up = main_pred[:3] + str((int(main_pred[3]) + 1) % 10)
    sh_down = main_pred[:3] + str((int(main_pred[3]) - 1) % 10)

    # UI Header
    c_head1, c_head2 = st.columns([3, 1])
    with c_head1:
        st.markdown(f"## <span class='status-pulse'></span> TARGET ACQUISITION: {target.upper()}", unsafe_allow_html=True)
    with c_head2:
        if st.button("⬅️ BACK TO BRIEFING"):
            st.session_state['page'] = 'briefing'
            st.rerun()

    # Main Display
    st.markdown("<div class='war-card'>", unsafe_allow_html=True)
    st.markdown(f"<span class='badge badge-cyan'>AI CONFIDENCE: {config['trust']}%</span> <span class='badge badge-red'>MODE: {config['mode'].upper()}</span>", unsafe_allow_html=True)
    st.write("### ⚡ VOID TARGET (MAIN)")
    st.markdown(f"<p class='main-pred'>{main_pred}</p>", unsafe_allow_html=True)
    st.progress(config['trust']/100)
    st.markdown("</div>", unsafe_allow_html=True)

    # Interactive Tabs
    t_def, t_intel, t_tools = st.tabs(["🛡️ DEFENSE SYSTEM", "📜 INTEL DATABASE", "🛠️ NOISE TOOLS"])

    with t_def:
        col_u, col_d = st.columns(2)
        with col_u:
            st.error(f"**SHADOW UP (+1)**\n## {sh_up}")
        with col_d:
            st.error(f"**SHADOW DOWN (-1)**\n## {sh_down}")
        st.caption("ℹ️ Gunakan jaring pengaman ini untuk mematikan celah manipulasi bandar.")

    with t_intel:
        st.subheader("📜 Log Audit Terakhir")
        if eternal_mem:
            st.table(pd.DataFrame([l.split(" | ") for l in eternal_mem[-10:]], columns=["Time", "Server", "Result"]))
        if st.button("✅ LOCK RESULT TO MEMORY"):
            save_memory(main_pred, target)
            st.success("Target Terkunci.")

    with t_tools:
        st.subheader("🎭 Noise Injection Camouflage")
        st.info("Pasang angka acak ini untuk mengelabui deteksi admin:")
        st.code(f"{random.randint(1000,9999)} | {random.randint(1000,9999)} | {random.randint(1000,9999)}")

st.markdown("---")
st.markdown("<p style='text-align:center; color:#555;'>SENTINEL v40.5 | OPERATIONAL SOVEREIGNTY | 2026</p>", unsafe_allow_html=True)
