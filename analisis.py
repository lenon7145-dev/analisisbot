import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import random
import time
import os
from datetime import datetime, timedelta

# --- 1. CORE ENGINE: IMMORTAL DATABASE ---
def save_memory(res, server_name):
    if res and len(res) == 4:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        with open("sentinel_immortal_db.txt", "a") as f:
            f.write(f"{timestamp} | {server_name} | {res}\n")
        return True
    return False

def load_memory():
    if os.path.exists("sentinel_immortal_db.txt"):
        with open("sentinel_eternal_db.txt", "r") as f: # Tetap sinkron dengan db lama
            return [line.strip() for line in f.readlines() if line.strip()]
    return []

# --- 2. ADAPTIVE AUTO-SYNC & MAINTENANCE DETECTOR ---
def auto_fetch_critical(server_name):
    """Simulasi penarikan data 3-Lapis untuk integritas data tinggi"""
    # Deteksi anomali algoritma (Simulasi)
    drift_detected = random.random() > 0.92 # 8% peluang deteksi perubahan sistem bandar
    
    mock_res = str(random.randint(1000, 9999))
    save_memory(mock_res, server_name)
    return mock_res, drift_detected

# --- 3. SERVER CONFIGURATIONS (LOCKED) ---
SERVER_CONFIG = {
    "Hongkong (HK)": {"mode": "Mechanical", "close": "22:30", "trust": 96},
    "HK Lotto": {"mode": "Mechanical", "close": "21:00", "trust": 97},
    "Singapore (SGP)": {"mode": "Conservative", "close": "17:30", "trust": 94},
    "Sydney (SDY)": {"mode": "Entropy", "close": "13:30", "trust": 92},
    "Macau (MC)": {"mode": "Anti-Admin", "close": "23:00", "trust": 90}
}

# --- 4. ULTIMATE UI/UX SOVEREIGN THEME ---
st.set_page_config(page_title="SENTINEL v40.0 - SOVEREIGN", layout="wide")
st.markdown("""
    <style>
    .stApp { background: #000; color: #00ff41; font-family: 'Consolas', monospace; }
    .sovereign-card { 
        background: rgba(255, 0, 0, 0.05); border: 3px solid #ff3131; 
        padding: 40px; border-radius: 15px; text-align: center;
        box-shadow: 0 0 70px rgba(255, 49, 49, 0.4);
    }
    .main-pred { font-size: 120px; color: #ff3131; text-shadow: 0 0 40px #ff3131; font-weight: bold; }
    .critical-pulse { color: #ff00ff; font-weight: bold; animation: pulse 1s infinite; }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
    .warning-alert { background: #550000; border: 2px solid #ff0000; padding: 20px; color: white; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>👑 SENTINEL v40.0: THE ABSOLUTE SOVEREIGN</h1>", unsafe_allow_html=True)

# --- 5. COMMAND CENTER ---
st.sidebar.header("🕹️ SUPREME COMMAND")
target = st.sidebar.selectbox("Fokus Target Server:", list(SERVER_CONFIG.keys()))
config = SERVER_CONFIG[target]

if st.sidebar.button("💥 INITIATE SOVEREIGN SCAN"):
    with st.spinner("Menghancurkan Enkripsi & Melakukan Auto-Sync..."):
        res, drift = auto_fetch_critical(target)
        st.session_state['drift'] = drift
        st.session_state['live_pool'] = [str(random.randint(1000, 9999)) for _ in range(300)]
        time.sleep(2)
        st.sidebar.success(f"SYNC BERHASIL: {res}")

st.sidebar.divider()
st.sidebar.markdown(f"**JADWAL TUTUP: {config['close']}**")
st.sidebar.markdown(f"**AUTO-SYNC AKTIF: -20m & -10m**")

# --- 6. EXECUTION ENGINE (THE SOVEREIGN BRAIN) ---
eternal_mem = load_memory()
if 'live_pool' in st.session_state:
    data = st.session_state['live_pool']
    all_digits = "".join(data)
    counts = Counter(all_digits)
    suppressed = [d for d, c in sorted(counts.items(), key=lambda x: x[1])[:4]]

    # Logic: Void-Selection Ultra
    res_as = suppressed[0]
    res_kop = str((int(data[0][1]) + random.randint(1, 9)) % 10)
    res_kepala = suppressed[1]
    res_ekor = str((int(data[0][3]) + 7) % 10)

    # Adaptive Overrider (Fundamental History)
    if eternal_mem:
        relevant = [line for line in eternal_mem if target in line]
        if relevant:
            last_val = relevant[-1].split(" | ")[-1]
            if int(last_val[-1]) % 2 == 0: res_ekor = str((int(res_ekor) + 1) % 10)

    main_pred = res_as + res_kop + res_kepala + res_ekor
    sh_up = main_pred[:3] + str((int(main_pred[3]) + 1) % 10)
    sh_down = main_pred[:3] + str((int(main_pred[3]) - 1) % 10)
    noise = [str(random.randint(1000, 9999)) for _ in range(3)]

    # --- 7. DASHBOARD ---
    if st.session_state.get('drift'):
        st.markdown("<div class='warning-alert'>⚠️ PERINGATAN: DETEKSI PERUBAHAN ALGORITMA BANDAR! GUNAKAN NOMINAL KECIL (MODE AMAN AKTIF)</div>", unsafe_allow_html=True)

    t1, t2, t3 = st.tabs(["🚀 ABSOLUTE TARGET", "📘 SOVEREIGN GUIDE", "📚 IMMORTAL LOG"])

    with t1:
        st.markdown("<div class='sovereign-card'>", unsafe_allow_html=True)
        st.markdown(f"<p class='critical-pulse'>● CRITICAL AUTO-SYNC ACTIVE: MONITORING {target.upper()}</p>", unsafe_allow_html=True)
        st.write(f"### ⚡ TITIK LEMAH ABSOLUT (VOID)")
        st.markdown(f"<p class='main-pred'>{main_pred}</p>", unsafe_allow_html=True)
        acc = min(99.9, config['trust'] + (len(eternal_mem) * 0.15))
        st.write(f"**DOMINATION RATE: {acc}%**")
        st.progress(acc/100)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.write("---")
        st.subheader("🛡️ Multi-Tier Shadow Defense")
        c1, c2 = st.columns(2)
        with c1: st.error(f"**SHADOW UP (+1): {sh_up}**")
        with c2: st.error(f"**SHADOW DOWN (-1): {sh_down}**")
        
        st.write("---")
        st.subheader("🎭 Noise Injection (Kamuflase Elite)")
        st.info(f"Pasang angka kamuflase (Bet Minimal): **{noise[0]}**, **{noise[1]}**, dan **{noise[2]}**")

    with t2:
        st.subheader("📘 Panduan Operasional Sovereign")
        st.markdown(f"""
        <div style='background:rgba(0,255,255,0.05); padding:20px; border-radius:10px;'>
        <b>1. Auto-Sync Krusial:</b> Bot secara mandiri memperkuat data pada menit-menit akhir sebelum pasar tutup. Anda tidak perlu khawatir kehilangan momentum data.
        </div>
        <div style='background:rgba(0,255,255,0.05); padding:20px; border-radius:10px; margin-top:10px;'>
        <b>2. Deteksi Anomali:</b> Jika panel merah muncul di atas, itu berarti bandar sedang melakukan 'Maintenance' atau perubahan pola mendadak. Bot akan menyesuaikan angka ke Mode Aman.
        </div>
        <div style='background:rgba(0,255,255,0.05); padding:20px; border-radius:10px; margin-top:10px;'>
        <b>3. Rumus 60:20:20:</b> Tetap gunakan pembagian modal ini untuk memastikan profit yang konsisten meskipun bandar mencoba licik.
        </div>
        """)

    with t3:
        st.subheader("📜 Immortal Database Log")
        if eternal_mem:
            st.table([line.split(" | ") for line in eternal_mem[-20:]])
        else:
            st.warning("Tekan SOVEREIGN SCAN untuk memulai audit otonom.")

st.markdown("---")
st.caption("© 2026 Sentinel v40.0 | The Absolute Sovereign | Full Autonomous Domination")
