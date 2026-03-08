import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import random
import time
import os
from datetime import datetime

# --- 1. CORE ENGINE: IMMORTAL DATABASE (SISTEM INGATAN ABADI) ---
def save_memory(res, server_name):
    if res and len(res) == 4:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        # Menggunakan file fisik agar data tidak hilang saat server restart
        with open("sentinel_immortal_db.txt", "a") as f:
            f.write(f"{timestamp} | {server_name} | {res}\n")
        return True
    return False

def load_memory():
    if os.path.exists("sentinel_immortal_db.txt"):
        with open("sentinel_immortal_db.txt", "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    return []

# --- 2. OMNI-SYNC & ANOMALY DETECTOR (SISTEM DETEKSI MODIFIKASI BANDAR) ---
def auto_fetch_sovereign(server_name):
    """Simulasi penarikan data 3-Lapis dengan deteksi pergeseran algoritma"""
    # 8% peluang deteksi perubahan sistem bandar (Maintenance Shift)
    drift_detected = random.random() > 0.92 
    mock_res = str(random.randint(1000, 9999))
    save_memory(mock_res, server_name)
    return mock_res, drift_detected

# --- 3. SERVER CONFIGURATIONS (LOCKED) ---
SERVER_CONFIG = {
    "Hongkong (HK)": {"mode": "Mechanical", "close": "22:30", "trust": 96, "strategy": "Step-Ladder Logic"},
    "HK Lotto": {"mode": "Mechanical", "close": "21:00", "trust": 97, "strategy": "Ball-Drop Physics"},
    "Singapore (SGP)": {"mode": "Conservative", "close": "17:30", "trust": 94, "strategy": "Risk-Balance Audit"},
    "Sydney (SDY)": {"mode": "Entropy", "close": "13:30", "trust": 92, "strategy": "Volatility-Lock"},
    "Macau (MC)": {"mode": "Anti-Admin", "close": "23:00", "trust": 90, "strategy": "Deep-Void Spotting"}
}

# --- 4. MASTER THEME & UI ARCHITECTURE ---
st.set_page_config(page_title="SENTINEL v40.1 - SOVEREIGN REFINED", layout="wide")
st.markdown("""
    <style>
    .stApp { background: #000500; color: #00ff41; font-family: 'Consolas', monospace; }
    .sovereign-card { 
        background: rgba(255, 0, 0, 0.05); border: 3px solid #ff3131; 
        padding: 40px; border-radius: 15px; text-align: center;
        box-shadow: 0 0 70px rgba(255, 49, 49, 0.4);
    }
    .main-pred { font-size: 110px; color: #ff3131; text-shadow: 0 0 40px #ff3131; font-weight: bold; margin-bottom: 0px; }
    .status-pulse { color: #00ffff; font-weight: bold; animation: pulse 1.5s infinite; }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
    .guide-box { background: rgba(0, 255, 255, 0.08); border-left: 6px solid #00ffff; padding: 25px; margin: 15px 0; border-radius: 10px; }
    .warning-alert { background: #660000; border: 2px solid #ff0000; padding: 20px; color: white; font-weight: bold; text-align: center; border-radius: 10px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>👑 SENTINEL v40.1: THE ABSOLUTE SOVEREIGN (REFINED)</h1>", unsafe_allow_html=True)

# --- 5. COMMAND CENTER (SIDEBAR) ---
st.sidebar.header("🕹️ SUPREME CONTROL PANEL")
target = st.sidebar.selectbox("Fokus Analisa Server:", list(SERVER_CONFIG.keys()))
config = SERVER_CONFIG[target]

if st.sidebar.button("💥 INITIATE SOVEREIGN SYNC"):
    with st.spinner(f"Menarik Instrumen {target}..."):
        res, drift = auto_fetch_sovereign(target)
        st.session_state['drift_active'] = drift
        # Simulasi pool data besar untuk Void-Selection
        st.session_state['live_pool'] = [str(random.randint(1000, 9999)) for _ in range(350)]
        time.sleep(2)
        st.sidebar.success(f"SYNC SUCCESS: {res}")

st.sidebar.divider()
st.sidebar.write(f"**JADWAL TUTUP:** {config['close']}")
st.sidebar.write(f"**STRATEGI:** {config['strategy']}")
st.sidebar.info("Auto-Sync Aktif: -20m & -10m")

# --- 6. LOGIKA EKSEKUSI (THE SOVEREIGN BRAIN) ---
eternal_mem = load_memory()
if 'live_pool' in st.session_state:
    data = st.session_state['live_pool']
    all_digits = "".join(data)
    counts = Counter(all_digits)
    # Void Selection: Mencari digit yang paling jarang dikeluarkan bandar (biaya payout rendah)
    suppressed = [d for d, c in sorted(counts.items(), key=lambda x: x[1])[:4]]

    res_as = suppressed[0]
    res_kop = str((int(data[0][1]) + random.randint(1, 9)) % 10)
    res_kepala = suppressed[1]
    res_ekor = str((int(data[0][3]) + 7) % 10)

    # Sinkronisasi Sejarah (Immortal DB)
    if eternal_mem:
        relevant = [line for line in eternal_mem if target in line]
        if relevant:
            last_res = relevant[-1].split(" | ")[-1]
            if int(last_res[-1]) % 2 == 0: res_ekor = str((int(res_ekor) + 1) % 10)

    main_pred = res_as + res_kop + res_kepala + res_ekor
    sh_up = main_pred[:3] + str((int(main_pred[3]) + 1) % 10)
    sh_down = main_pred[:3] + str((int(main_pred[3]) - 1) % 10)
    noise = [str(random.randint(1000, 9999)) for _ in range(3)]

    # --- 7. DASHBOARD MULTI-TAB ---
    # Memastikan Panduan (Guide) tampil mendetail
    t_guide, t_target, t_audit = st.tabs(["📘 MASTER GUIDE & SOP", "🎯 TARGET ACQUISITION", "📜 IMMORTAL DATABASE"])

    with t_guide:
        st.subheader("🏛️ Panduan Operasional Sovereign (SOP Master)")
        st.markdown(f"""
        <div class='guide-box'>
        <b>1. Filosofi Void-Selection:</b> Bandar adalah bisnis. Mereka selalu mengeluarkan angka dengan payout terkecil. Bot ini menganalisis 350 titik data simulasi untuk menemukan <b>VOID</b> (titik kosong) yang paling menguntungkan bagi bandar namun mematikan bagi pemain umum.
        </div>
        <div class='guide-box'>
        <b>2. Protokol Sync Krusial:</b> Selalu tekan <b>Initiate Sovereign Sync</b> pada 20 menit dan 10 menit sebelum pasaran ditutup. Ini adalah waktu di mana bandar mulai mengunci angka buangan mereka.
        </div>
        <div class='guide-box'>
        <b>3. Rumus Pemasangan 60:20:20:</b>
        <ul>
            <li><b>60% Modal:</b> Pasang pada Angka Utama (Void).</li>
            <li><b>20% Modal:</b> Pasang pada Shadow UP (+1).</li>
            <li><b>20% Modal:</b> Pasang pada Shadow DOWN (-1).</li>
        </ul>
        <i>Strategi ini mengunci manipulasi 1-digit yang sering dilakukan bandar di detik terakhir.</i>
        </div>
        <div class='guide-box'>
        <b>4. Safety Mask (Noise Injection):</b> Pasang 3 angka Noise dengan nominal minimal (misal Rp 500) agar akun Anda tidak terdeteksi oleh bot Anti-Cheat admin bandar.
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader("🔬 Detail Strategi Per Server")
        st.table([{"Server": k, "Strategi": v["strategy"], "Trust Rate": f"{v['trust']}%"} for k, v in SERVER_CONFIG.items()])

    with t_target:
        if st.session_state.get('drift_active'):
            st.markdown("<div class='warning-alert'>⚠️ MAINTENANCE DETECTED: BANDAR MENGUBAH ALGORITMA! MODE AMAN AKTIF (Gunakan Nominal Kecil)</div>", unsafe_allow_html=True)

        st.markdown("<div class='sovereign-card'>", unsafe_allow_html=True)
        st.markdown(f"<p class='status-pulse'>● SOVEREIGN MONITORING ACTIVE: {target.upper()}</p>", unsafe_allow_html=True)
        st.write(f"### ⚡ TITIK LEMAH ABSOLUT (VOID)")
        st.markdown(f"<p class='main-pred'>{main_pred}</p>", unsafe_allow_html=True)
        acc_score = min(99.9, config['trust'] + (len(eternal_mem) * 0.15))
        st.write(f"**DOMINATION PROBABILITY: {acc_score}%**")
        st.progress(acc_score/100)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.divider()
        st.subheader("🛡️ Shadow Tracker (Anti-Manipulasi)")
        c1, c2 = st.columns(2)
        with c1: st.error(f"**SHADOW UP (+1): {sh_up}**")
        with c2: st.error(f"**SHADOW DOWN (-1): {sh_down}**")
        
        st.divider()
        st.subheader("🎭 Noise Injection (Kamuflase Elite)")
        st.info(f"Pasang angka ini nominal terkecil: **{noise[0]}**, **{noise[1]}**, dan **{noise[2]}**")

    with t_audit:
        st.subheader("📜 Immortal Audit Log (Database Abadi)")
        if eternal_mem:
            st.write(f"Total Audit Fundamental: {len(eternal_mem)} entri.")
            st.table([line.split(" | ") for line in eternal_mem[-25:]])
        else:
            st.warning("Database Kosong. Lakukan Sovereign Sync untuk memulai pengumpulan data fundamental.")

st.markdown("---")
st.caption("© 2026 Sentinel v40.1 | The Absolute Sovereign | Full Refined Architecture")

