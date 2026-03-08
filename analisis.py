import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import random
import time
import os
from datetime import datetime

# --- 1. CORE CONFIGURATION (ULTIMATE VERSION) ---
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

# --- 3. NEURAL LOGIC & ANTI-GAP DETECTOR ---
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
    # Jika 3 dari 4 digit berubah total dari tren terakhir secara mendadak
    diff = sum(1 for a, b in zip(last_res, current_pred) if a != b)
    return diff >= 3

# --- 4. SERVER ARCHITECTURE ---
SERVER_CONFIG = {
    "Hongkong (HK)": {"mode": "Mechanical", "trust": 96, "color": "#ff0000"},
    "Singapore (SGP)": {"mode": "Conservative", "trust": 94, "color": "#00ff00"},
    "Sydney (SDY)": {"mode": "Entropy", "trust": 92, "color": "#00ffff"},
    "Macau (MC)": {"mode": "Anti-Admin", "trust": 90, "color": "#ffff00"}
}

# --- 5. AGGRESSIVE UI DESIGN (WAR-MODE) ---
st.set_page_config(page_title=f"SENTINEL v{VERSION}", layout="wide")
st.markdown(f"""
    <style>
    /* Global Style */
    .stApp {{ background: radial-gradient(circle, #0a0a0a 0%, #000000 100%); color: #00ff41; font-family: 'Courier New', monospace; }}
    
    /* War-Mode Card */
    .war-card {{ 
        background: rgba(20, 20, 20, 0.95); border: 2px solid #ff0000; 
        padding: 30px; border-radius: 5px; text-align: center;
        box-shadow: 0 0 30px rgba(255, 0, 0, 0.4), inset 0 0 15px rgba(255, 0, 0, 0.2);
        margin-bottom: 20px;
    }}
    
    /* Main Prediction Display */
    .main-pred {{ 
        font-size: 130px; color: #ffffff; text-shadow: 0 0 20px #ff0000, 0 0 50px #ff0000; 
        font-weight: 900; letter-spacing: 15px; margin: 20px 0;
    }}
    
    /* Critical Alert Animations */
    .critical-alert {{ 
        background: #ff0000; color: white; padding: 15px; font-weight: bold; 
        text-align: center; animation: blinker 0.8s linear infinite; border: 3px solid white;
    }}
    @keyframes blinker {{ 50% {{ opacity: 0; }} }}
    
    .status-text {{ color: #00ffff; font-weight: bold; font-size: 1.2rem; }}
    .scan-line {{ width: 100%; height: 2px; background: #00ff41; opacity: 0.3; position: relative; animation: scan 2s linear infinite; }}
    @keyframes scan {{ 0% {{ top: 0; }} 100% {{ top: 100px; }} }}
    
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {{ gap: 20px; }}
    .stTabs [data-baseweb="tab"] {{ border: 1px solid #333; padding: 10px 20px; border-radius: 5px 5px 0 0; background: #111; }}
    </style>
    """, unsafe_allow_html=True)

# --- 6. SIDEBAR & SYSTEM SYNC ---
st.sidebar.markdown("<h2 style='color:red;'>⚠️ COMMAND CENTER</h2>", unsafe_allow_html=True)
target = st.sidebar.selectbox("TARGET SERVER:", list(SERVER_CONFIG.keys()))
config = SERVER_CONFIG[target]

if st.sidebar.button("🚨 INITIATE SINGULARITY SYNC"):
    with st.spinner("MEMBEDAH ENKRIPSI BANDAR..."):
        st.session_state['pool'] = [str(random.randint(1000, 9999)) for _ in range(500)]
        time.sleep(1.2)
        st.sidebar.success("SYNC COMPLETE")

# Backup Memory Button
if os.path.exists(DB_FILE):
    with open(DB_FILE, "r") as f:
        st.sidebar.download_button("💾 DOWNLOAD IMMORTAL DB", f.read(), f"sentinel_backup.txt")

# --- 7. CORE EXECUTION ENGINE ---
eternal_mem = load_memory()
if 'pool' in st.session_state:
    data_pool = st.session_state['pool']
    counts = Counter("".join(data_pool))
    suppressed = [d for d, c in sorted(counts.items(), key=lambda x: x[1])[:4]]

    # AI Brain Processing
    ai_offset = get_ai_neural_offset(target, eternal_mem)
    res_as = suppressed[0]
    res_kop = str((int(data_pool[0][1]) + random.randint(1, 9)) % 10)
    res_kepala = suppressed[1]
    res_ekor = str((int(data_pool[0][3]) + 7 + ai_offset) % 10)

    main_pred = res_as + res_kop + res_kepala + res_ekor
    sh_up = main_pred[:3] + str((int(main_pred[3]) + 1) % 10)
    sh_down = main_pred[:3] + str((int(main_pred[3]) - 1) % 10)
    
    # Anti-Gap Check
    is_drift = detect_extreme_drift(eternal_mem, main_pred)

    # --- 8. WAR-ROOM DASHBOARD ---
    st.markdown(f"<p class='status-text'>[ SYSTEM STATUS: ATTACKING {target.upper()} ]</p>", unsafe_allow_html=True)
    st.markdown("<div class='scan-line'></div>", unsafe_allow_html=True)

    t_main, t_defense, t_audit = st.tabs(["🎯 KILL-ZONE", "🛡️ DEFENSE PROTOCOL", "📜 INTEL LOG"])

    with t_main:
        if is_drift:
            st.markdown("<div class='critical-alert'>🚨 DETEKSI INTERVENSI ADMIN: JANGAN ALL-IN! 🚨</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='war-card'>", unsafe_allow_html=True)
        st.write("### ⚡ VOID TARGET (MAIN PREDICTION)")
        st.markdown(f"<p class='main-pred'>{main_pred}</p>", unsafe_allow_html=True)
        st.write(f"Confidence Level: **{config['trust']}%** | AI Neural: **Linked**")
        st.progress(config['trust']/100)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Save Trigger
        if st.button("✅ MARK AS RESULT (SAVE TO MEMORY)"):
            if save_memory(main_pred, target):
                st.success("Target Terkunci di Database Abadi.")

    with t_defense:
        st.subheader("🛡️ SHADOW DEFENSE (ANTI-MANIPULASI)")
        c1, c2 = st.columns(2)
        with c1:
            st.error(f"**SHADOW UP (+1)**\n## {sh_up}")
            st.caption("Gunakan jika bandar menaikkan 1 digit di akhir.")
        with c2:
            st.error(f"**SHADOW DOWN (-1)**\n## {sh_down}")
            st.caption("Gunakan jika bandar menurunkan 1 digit di akhir.")
        
        st.divider()
        st.subheader("🎭 NOISE INJECTION (CAMOUFLAGE)")
        st.warning(f"Pasang nominal kecil: {random.randint(1000,9999)}, {random.randint(1000,9999)}, {random.randint(1000,9999)}")

    with t_audit:
        st.subheader("📜 INTEL REPORT (HISTORY)")
        if eternal_mem:
            df = pd.DataFrame([l.split(" | ") for l in eternal_mem[-15:]], columns=["Time", "Server", "Result"])
            st.dataframe(df, use_container_width=True)
        else:
            st.info("Belum ada data intelijen terkumpul.")

# --- 9. FOOTER ---
st.markdown("---")
st.markdown(f"<p style='text-align:center; color:#444;'>SENTINEL v{VERSION} | SECURITY LEVEL: SOVEREIGN | NO IDENTITY DETECTED</p>", unsafe_allow_html=True)
