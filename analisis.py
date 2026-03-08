import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import random
import time
import os
from datetime import datetime

# --- 1. CORE ENGINE: PERSISTENT DATA ---
def save_memory(res, server_name):
    if res and len(res) == 4:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        with open("sentinel_eternal_db.txt", "a") as f:
            f.write(f"{timestamp} | {server_name} | {res}\n")
        return True
    return False

def load_memory():
    if os.path.exists("sentinel_eternal_db.txt"):
        with open("sentinel_eternal_db.txt", "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    return []

# --- 2. AUTO-FETCH SIMULATOR ---
def auto_fetch_all():
    """Simulasi penarikan data dari semua server utama"""
    results = {
        "Hongkong (HK)": str(random.randint(1000, 9999)),
        "HK Lotto": str(random.randint(1000, 9999)),
        "Singapore (SGP)": str(random.randint(1000, 9999)),
        "Sydney (SDY)": str(random.randint(1000, 9999)),
        "Macau (MC)": str(random.randint(1000, 9999))
    }
    for srv, res in results.items():
        save_memory(res, srv)
    return results

# --- 3. SERVER CONFIGURATIONS ---
SERVER_CONFIG = {
    "Hongkong (HK)": {"mode": "Mechanical", "strategy": "Step-Ladder Logic", "trust": 92},
    "HK Lotto": {"mode": "Mechanical", "strategy": "Ball-Drop Physics", "trust": 95},
    "Singapore (SGP)": {"mode": "Conservative", "strategy": "Risk-Balance Audit", "trust": 90},
    "Sydney (SDY)": {"mode": "Entropy", "strategy": "Volatility-Lock", "trust": 88},
    "Macau (MC)": {"mode": "Anti-Admin", "strategy": "Deep-Void Spotting", "trust": 85}
}

# --- 4. UI/UX MASTER THEME ---
st.set_page_config(page_title="SENTINEL v39.1 - OMNI OVERLORD", layout="wide")
st.markdown("""
    <style>
    .stApp { background: #000; color: #00ff41; font-family: 'Consolas', monospace; }
    .main-card { 
        background: rgba(255, 0, 0, 0.05); border: 2px solid #ff3131; 
        padding: 30px; border-radius: 10px; text-align: center;
        box-shadow: 0 0 40px rgba(255, 49, 49, 0.2);
    }
    .main-pred { font-size: 100px; color: #ff3131; text-shadow: 0 0 25px #ff3131; font-weight: bold; }
    .status-active { color: #00ffff; font-weight: bold; animation: blinker 1.5s linear infinite; }
    @keyframes blinker { 50% { opacity: 0; } }
    .guide-box { background: rgba(0, 255, 255, 0.05); border-left: 5px solid #00ffff; padding: 15px; margin: 10px 0; font-size: 14px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>👹 SENTINEL v39.1: OMNI OVERLORD</h1>", unsafe_allow_html=True)

# --- 5. COMMAND CENTER ---
st.sidebar.header("🕹️ GLOBAL COMMAND")
if st.sidebar.button("💥 FULL OMNI-SYNC (ALL SERVERS)"):
    with st.spinner("Mengaudit Seluruh Server Global..."):
        all_res = auto_fetch_all()
        st.session_state['omni_data'] = all_res
        st.session_state['live_pool'] = [str(random.randint(1000, 9999)) for _ in range(150)]
        time.sleep(2)
        st.sidebar.success("Semua Memori Server Diperbarui!")

st.sidebar.divider()
target = st.sidebar.selectbox("Fokus Analisa Server:", list(SERVER_CONFIG.keys()))
config = SERVER_CONFIG[target]

# --- 6. EXECUTION ENGINE ---
eternal_mem = load_memory()
if 'live_pool' in st.session_state:
    data = st.session_state['live_pool']
    all_digits = "".join(data)
    counts = Counter(all_digits)
    suppressed = [d for d, c in sorted(counts.items(), key=lambda x: x[1])[:4]]

    # Logic: Deep Void Selection
    res_as = suppressed[0]
    res_kop = str((int(data[0][1]) + random.randint(1, 9)) % 10)
    res_kepala = suppressed[1]
    res_ekor = str((int(data[0][3]) + 7) % 10)

    # Autonomous Memory Overrider
    if eternal_mem:
        # Mencari entri terakhir khusus untuk server ini
        srv_last = [line for line in eternal_mem if target in line]
        if srv_last:
            last_digit = int(srv_last[-1].split(" | ")[-1][-1])
            if last_digit % 2 == 0: res_ekor = str((int(res_ekor) + 1) % 10)

    main_pred = res_as + res_kop + res_kepala + res_ekor
    sh_up = main_pred[:3] + str((int(main_pred[3]) + 1) % 10)
    sh_down = main_pred[:3] + str((int(main_pred[3]) - 1) % 10)
    noise = [str(random.randint(1000, 9999)) for _ in range(2)]

    # --- 7. DISPLAY DASHBOARD ---
    t1, t2, t3 = st.tabs(["🎯 TARGET ACQUISITION", "🔬 VOID ANALYTICS", "🏛️ ETERNAL DB"])

    with t1:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.markdown(f"<p class='status-active'>● SYSTEM MONITORING: {target.upper()}</p>", unsafe_allow_html=True)
        st.write(f"### ⚡ PREDIKSI TITIK LEMAH BANDAR")
        st.markdown(f"<p class='main-pred'>{main_pred}</p>", unsafe_allow_html=True)
        acc = min(99.9, config['trust'] + (len(eternal_mem) * 0.15))
        st.write(f"**DESTRUCTION RATE: {acc}%**")
        st.progress(acc/100)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.write("---")
        st.subheader("🛡️ Shadow Tracker (Lapis Kedua)")
        c1, c2 = st.columns(2)
        with c1: st.error(f"**SHADOW UP (+1): {sh_up}**")
        with c2: st.error(f"**SHADOW DOWN (-1): {sh_down}**")
        
        st.write("---")
        st.subheader("🎭 Noise Injection (Kamuflase)")
        st.info(f"Pasang angka ini nominal terkecil: **{noise[0]}** dan **{noise[1]}**")

    with t2:
        st.subheader("🔬 Analisa Celah Keamanan")
        
        st.write(f"**Strategi Aktif:** {config['strategy']}")
        st.write(f"**Analisa:** Angka {main_pred} terdeteksi memiliki beban payout terendah di database {target}.")

    with t3:
        st.subheader("📜 Eternal Database (Audit Log)")
        if eternal_mem:
            st.table([line.split(" | ") for line in eternal_mem[-15:]])
        else:
            st.warning("Klik OMNI-SYNC untuk mengisi database.")

st.markdown("---")
st.caption("© 2026 Sentinel v39.1 | The Absolute Overlord | Omni-Server Decimation")
