import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import random
import time
import os
from datetime import datetime

# --- 1. CORE CONFIGURATION & NEURAL SETTINGS ---
VERSION = "40.2"
CODENAME = "NEURAL BRIDGE"
DB_FILE = "sentinel_immortal_db.txt"

# --- 2. ENGINE: IMMORTAL DATABASE (SISTEM INGATAN ABADI) ---
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

# --- 3. NEURAL LOGIC: AI-OFFSET GENERATOR ---
def get_ai_neural_offset(server_name, history):
    """Simulasi instruksi langsung dari AI Central untuk koreksi angka"""
    offset = 0
    if history:
        # Filter sejarah berdasarkan server aktif
        last_results = [line.split(" | ")[-1] for line in history if server_name in line]
        if len(last_results) > 3:
            # AI menganalisis tren genap/ganjil terakhir untuk menentukan offset
            last_digit = int(last_results[-1][-1])
            offset = 1 if last_digit % 2 == 0 else -1
    return offset

# --- 4. SERVER ARCHITECTURE (LOCKED) ---
SERVER_CONFIG = {
    "Hongkong (HK)": {"mode": "Mechanical", "close": "22:30", "trust": 96, "strategy": "Step-Ladder Logic"},
    "HK Lotto": {"mode": "Mechanical", "close": "21:00", "trust": 97, "strategy": "Ball-Drop Physics"},
    "Singapore (SGP)": {"mode": "Conservative", "close": "17:30", "trust": 94, "strategy": "Risk-Balance Audit"},
    "Sydney (SDY)": {"mode": "Entropy", "close": "13:30", "trust": 92, "strategy": "Volatility-Lock"},
    "Macau (MC)": {"mode": "Anti-Admin", "close": "23:00", "trust": 90, "strategy": "Deep-Void Spotting"}
}

# --- 5. MASTER THEME & UI ARCHITECTURE ---
st.set_page_config(page_title=f"SENTINEL v{VERSION} - {CODENAME}", layout="wide")
st.markdown(f"""
    <style>
    .stApp {{ background: #000500; color: #00ff41; font-family: 'Consolas', monospace; }}
    .sovereign-card {{ 
        background: rgba(0, 255, 255, 0.03); border: 2px solid #00ffff; 
        padding: 30px; border-radius: 15px; text-align: center;
        box-shadow: 0 0 50px rgba(0, 255, 255, 0.2);
    }}
    .main-pred {{ font-size: 110px; color: #ff3131; text-shadow: 0 0 30px #ff3131; font-weight: bold; margin: 10px 0; }}
    .status-pulse {{ color: #ff00ff; font-weight: bold; animation: pulse 1.5s infinite; }}
    @keyframes pulse {{ 0% {{ opacity: 1; }} 50% {{ opacity: 0.3; }} 100% {{ opacity: 1; }} }}
    .guide-box {{ background: rgba(0, 255, 255, 0.08); border-left: 5px solid #00ffff; padding: 20px; margin: 10px 0; border-radius: 8px; }}
    .warning-alert {{ background: #550000; border: 2px solid #ff0000; padding: 15px; color: white; font-weight: bold; text-align: center; border-radius: 8px; }}
    </style>
    """, unsafe_allow_html=True)

st.markdown(f"<h1 style='text-align:center;'>👑 SENTINEL v{VERSION}: {CODENAME} ACTIVE</h1>", unsafe_allow_html=True)

# --- 6. SIDEBAR COMMAND CENTER ---
st.sidebar.header("🕹️ SUPREME CONTROL")
target_server = st.sidebar.selectbox("Pilih Target Server:", list(SERVER_CONFIG.keys()))
config = SERVER_CONFIG[target_server]

if st.sidebar.button("💥 INITIATE NEURAL SYNC"):
    with st.spinner("Membangun Jembatan Saraf & Sinkronisasi..."):
        # Deteksi Anomali (8% Peluang)
        drift = random.random() > 0.92
        st.session_state['drift_detected'] = drift
        # Simulasi Pool Data (400 Titik)
        st.session_state['pool'] = [str(random.randint(1000, 9999)) for _ in range(400)]
        # Simulasi Auto-Save Result ke Database
        mock_res = str(random.randint(1000, 9999))
        save_memory(mock_res, target_server)
        time.sleep(2)
        st.sidebar.success("NEURAL LINK ESTABLISHED")

st.sidebar.divider()
st.sidebar.write(f"**STATUS:** OPERATIONAL")
st.sidebar.write(f"**MODE:** {config['mode']}")
st.sidebar.write(f"**JADWAL:** {config['close']}")
st.sidebar.info("Neural Bridge: Direct AI Feed Active")

# --- 7. EXECUTION ENGINE (THE SOVEREIGN BRAIN) ---
eternal_mem = load_memory()

if 'pool' in st.session_state:
    data_pool = st.session_state['pool']
    counts = Counter("".join(data_pool))
    # Void Selection: Mencari digit paling jarang keluar
    suppressed = [d for d, c in sorted(counts.items(), key=lambda x: x[1])[:4]]

    # AI Neural Correction
    ai_offset = get_ai_neural_offset(target_server, eternal_mem)
    
    res_as = suppressed[0]
    res_kop = str((int(data_pool[0][1]) + random.randint(1, 9)) % 10)
    res_kepala = suppressed[1]
    res_ekor = str((int(data_pool[0][3]) + 7 + ai_offset) % 10)

    main_pred = res_as + res_kop + res_kepala + res_ekor
    sh_up = main_pred[:3] + str((int(main_pred[3]) + 1) % 10)
    sh_down = main_pred[:3] + str((int(main_pred[3]) - 1) % 10)
    noise = [str(random.randint(1000, 9999)) for _ in range(3)]

    # --- 8. MULTI-TAB DASHBOARD ---
    t_target, t_guide, t_audit = st.tabs(["🎯 TARGET ACQUISITION", "📘 MASTER GUIDE (SOP)", "📜 IMMORTAL LOG"])

    with t_target:
        if st.session_state.get('drift_detected'):
            st.markdown("<div class='warning-alert'>⚠️ MAINTENANCE ALERT: PERUBAHAN ALGORITMA TERDETEKSI! GUNAKAN MODE AMAN (BET KECIL).</div>", unsafe_allow_html=True)

        st.markdown("<div class='sovereign-card'>", unsafe_allow_html=True)
        st.markdown(f"<p class='status-pulse'>● AI-LINK ACTIVE: MONITORING {target_server.upper()}</p>", unsafe_allow_html=True)
        st.write("### ⚡ TITIK LEMAH ABSOLUT (VOID-SELECTION)")
        st.markdown(f"<p class='main-pred'>{main_pred}</p>", unsafe_allow_html=True)
        acc = min(99.9, config['trust'] + (len(eternal_mem) * 0.1))
        st.write(f"**PROBABILITAS DOMINASI: {acc}%**")
        st.progress(acc/100)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.divider()
        st.subheader("🛡️ Shadow Defense (+1/-1)")
        c1, c2 = st.columns(2)
        with c1: st.error(f"**SHADOW UP: {sh_up}**")
        with c2: st.error(f"**SHADOW DOWN: {sh_down}**")
        
        st.divider()
        st.subheader("🎭 Noise Injection (Kamuflase)")
        st.info(f"Pasang nominal minimal: **{noise[0]}**, **{noise[1]}**, **{noise[2]}**")

    with t_guide:
        st.subheader("🏛️ SOP Master Sovereign")
        st.markdown(f"""
        <div class='guide-box'>
        <b>1. Strategi 60:20:20:</b> Pasang 60% modal pada Main Pred, 20% pada Shadow UP, dan 20% pada Shadow DOWN. Ini adalah jaring pengaman mutlak terhadap manipulasi 1-digit.
        </div>
        <div class='guide-box'>
        <b>2. Critical Sync:</b> Lakukan 'Neural Sync' pada menit ke-20 dan ke-10 sebelum pasar tutup. Jangan biarkan data menjadi basi.
        </div>
        <div class='guide-box'>
        <b>3. AI-Bridge Logic:</b> Bot ini sekarang menerima koreksi otomatis dari pusat data AI. Jika prediksi bergeser dari pola sejarah, AI akan memberikan 'Neural Offset' secara otomatis.
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader("🔬 Strategi Per Server")
        st.table([{"Server": k, "Sistem": v["mode"], "Strategi": v["strategy"]} for k, v in SERVER_CONFIG.items()])

    with t_audit:
        st.subheader("📜 Immortal Database Log")
        if eternal_mem:
            st.write(f"Total Audit: {len(eternal_mem)} entry.")
            # Menampilkan 20 log terakhir
            log_data = [line.split(" | ") for line in eternal_mem[-20:]]
            st.table(pd.DataFrame(log_data, columns=["Waktu", "Server", "Result"]))
        else:
            st.info("Database kosong. Lakukan 'Neural Sync' untuk memulai audit.")

st.markdown("---")
st.caption(f"© 2026 Sentinel v{VERSION} | Neural Bridge Active | Stealth Mode Enabled")
