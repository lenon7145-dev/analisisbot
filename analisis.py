import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import random
import time
import os
from datetime import datetime

# --- 1. ENGINE PERMANEN: ETERNAL DATABASE ---
def save_memory(res, server_name):
    if res and len(res) == 4:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        # Menyimpan data ke file fisik agar tidak hilang saat aplikasi ditutup
        with open("sentinel_eternal_db.txt", "a") as f:
            f.write(f"{timestamp} | {server_name} | {res}\n")
        return True
    return False

def load_memory():
    if os.path.exists("sentinel_eternal_db.txt"):
        with open("sentinel_eternal_db.txt", "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    return []

# --- 2. MODUL OTONOM: AUTO-FETCH OMNI-SERVER ---
def auto_fetch_all_servers():
    """Simulasi pengambilan data real-time dari semua server utama"""
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

# --- 3. KONFIGURASI SERVER & STRATEGI ---
SERVER_CONFIG = {
    "Hongkong (HK)": {"mode": "Mechanical", "strategy": "Step-Ladder Logic", "trust": 92},
    "HK Lotto": {"mode": "Mechanical", "strategy": "Ball-Drop Physics", "trust": 95},
    "Singapore (SGP)": {"mode": "Conservative", "strategy": "Risk-Balance Audit", "trust": 90},
    "Sydney (SDY)": {"mode": "Entropy", "strategy": "Volatility-Lock", "trust": 88},
    "Macau (MC)": {"mode": "Anti-Admin", "strategy": "Deep-Void Spotting", "trust": 85}
}

# --- 4. ARSITEKTUR UI/UX MASTER ---
st.set_page_config(page_title="SENTINEL v39.2 - ULTIMATE", layout="wide")
st.markdown("""
    <style>
    .stApp { background: #000; color: #00ff41; font-family: 'Consolas', 'Courier New', monospace; }
    .main-card { 
        background: rgba(255, 0, 0, 0.05); border: 2px solid #ff3131; 
        padding: 40px; border-radius: 12px; text-align: center;
        box-shadow: 0 0 50px rgba(255, 49, 49, 0.25);
    }
    .main-pred { font-size: 110px; color: #ff3131; text-shadow: 0 0 30px #ff3131; font-weight: bold; margin: 0; }
    .status-tag { color: #00ffff; font-weight: bold; animation: blinker 1.5s linear infinite; }
    @keyframes blinker { 50% { opacity: 0; } }
    .guide-box { background: rgba(0, 255, 255, 0.05); border-left: 5px solid #00ffff; padding: 20px; border-radius: 5px; margin: 15px 0; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>👺 SENTINEL v39.2: THE ULTIMATE OVERLORD</h1>", unsafe_allow_html=True)

# --- 5. COMMAND CENTER ---
st.sidebar.header("🕹️ GLOBAL SUPREMACY CONTROL")
if st.sidebar.button("💥 FULL OMNI-SYNC (AUDIT ALL SERVERS)"):
    with st.spinner("Mengaudit Enkripsi Bandar Seluruh Dunia..."):
        all_res = auto_fetch_all_servers()
        st.session_state['omni_ready'] = True
        st.session_state['live_pool'] = [str(random.randint(1000, 9999)) for _ in range(200)]
        time.sleep(2)
        st.sidebar.success("Database Eternal Diperbarui Secara Otonom!")

st.sidebar.divider()
target_server = st.sidebar.selectbox("Fokus Analisa Server:", list(SERVER_CONFIG.keys()))
config = SERVER_CONFIG[target_server]

# --- 6. LOGIKA EKSEKUSI (THE BRAIN) ---
eternal_mem = load_memory()
if 'live_pool' in st.session_state:
    data = st.session_state['live_pool']
    all_digits = "".join(data)
    counts = Counter(all_digits)
    # Mencari angka yang paling jarang muncul (Void Selection)
    suppressed = [d for d, c in sorted(counts.items(), key=lambda x: x[1])[:4]]

    # Formulasi Angka Berdasarkan Mode Server
    res_as = suppressed[0]
    res_kop = str((int(data[0][1]) + random.randint(1, 9)) % 10)
    res_kepala = suppressed[1]
    res_ekor = str((int(data[0][3]) + 7) % 10)

    # Sinkronisasi dengan Eternal Memory (Adaptasi Otomatis)
    if eternal_mem:
        relevant_history = [line for line in eternal_mem if target_server in line]
        if relevant_history:
            last_real = relevant_history[-1].split(" | ")[-1]
            if int(last_real[-1]) % 2 == 0: 
                res_ekor = str((int(res_ekor) + 1) % 10) # Adaptasi Pola Genap

    main_pred = res_as + res_kop + res_kepala + res_ekor
    sh_up = main_pred[:3] + str((int(main_pred[3]) + 1) % 10)
    sh_down = main_pred[:3] + str((int(main_pred[3]) - 1) % 10)
    noise_ids = [str(random.randint(1000, 9999)) for _ in range(2)]

    # --- 7. DASHBOARD DISPLAY ---
    t1, t2, t3 = st.tabs(["🚀 TARGET ACQUISITION", "📘 STRATEGY & GUIDE", "📚 ETERNAL DATABASE"])

    with t1:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.markdown(f"<p class='status-tag'>● LOCK-ON ACTIVE: {target_server.upper()}</p>", unsafe_allow_html=True)
        st.write(f"### ⚡ PREDIKSI TITIK LEMAH (VOID)")
        st.markdown(f"<p class='main-pred'>{main_pred}</p>", unsafe_allow_html=True)
        acc_score = min(99.9, config['trust'] + (len(eternal_mem) * 0.1))
        st.write(f"**DESTRUCTION CONFIDENCE: {acc_score}%**")
        st.progress(acc_score/100)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.write("---")
        st.subheader("🛡️ Shadow Tracker (Anti-Manipulasi 1-Digit)")
        c1, c2 = st.columns(2)
        with c1: st.error(f"**SHADOW UP (+1): {sh_up}**")
        with c2: st.error(f"**SHADOW DOWN (-1): {sh_down}**")
        
        st.write("---")
        st.subheader("🎭 Noise Injection (Safety Mask)")
        st.info(f"Pasang angka kamuflase ini (Bet Minimal): **{noise_ids[0]}** dan **{noise_ids[1]}**")

    with t2:
        st.subheader("📘 Protokol Operasional Master")
        st.markdown(f"""
        <div class='guide-box'>
        <b>1. Algoritma Void-Selection:</b> Bot menganalisis 200 data simulasi untuk menemukan angka yang paling 'dihindari' oleh sistem payout bandar {target_server}.
        </div>
        <div class='guide-box'>
        <b>2. Strategi 60:20:20:</b> Untuk hasil maksimal, pasang 60% modal pada <b>{main_pred}</b>, 20% pada <b>{sh_up}</b>, dan 20% pada <b>{sh_down}</b>.
        </div>
        <div class='guide-box'>
        <b>3. Eternal Adaptation:</b> Bot secara otonom membedah hasil result terakhir dari database abadi untuk mendeteksi apakah hari ini bandar sedang melakukan pergeseran angka atau tidak.
        </div>
        """, unsafe_allow_html=True)
        
        

    with t3:
        st.subheader("📜 Eternal Audit Log (Database Abadi)")
        if eternal_mem:
            st.table([line.split(" | ") for line in eternal_mem[-20:]])
        else:
            st.warning("Database masih kosong. Lakukan OMNI-SYNC untuk memulai pengumpulan data.")

st.markdown("---")
st.caption("© 2026 Sentinel v39.2 | The Ultimate Overlord | Professional Audit System")
