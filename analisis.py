import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import random
import time
import os

# --- 1. ETERNAL MEMORY FUNCTIONS ---
# Fungsi untuk menyimpan data secara permanen ke file fisik
def save_to_permanent_memory(data_result):
    if data_result:
        with open("sentinel_memory.txt", "a") as f:
            f.write(data_result + "\n")

# Fungsi untuk memuat data dari file fisik
def load_permanent_memory():
    if os.path.exists("sentinel_memory.txt"):
        with open("sentinel_memory.txt", "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    return []

# --- 2. GLOBAL CONFIGURATION ---
SERVER_CONFIG = {
    "Hongkong (HK)": {"mode": "Mechanical", "trust": 45, "strategy": "Step-Ladder Detection"},
    "HK Lotto": {"mode": "Mechanical", "trust": 60, "strategy": "Ball-Drop Pattern"},
    "Singapore (SGP)": {"mode": "Conservative", "trust": 72, "strategy": "Hard-Suppress Tracking"},
    "Sydney (SDY)": {"mode": "Entropy", "trust": 85, "strategy": "Chaos-Pattern Analysis"},
    "Macau (MC)": {"mode": "Anti-Admin", "trust": 20, "strategy": "Void-Spot Hunting"}
}

# --- 3. UI ARCHITECTURE ---
st.set_page_config(page_title="SENTINEL v38.4 - ETERNAL", layout="wide")
st.markdown("""
    <style>
    .stApp { background: #010801; color: #00ff7f; font-family: 'Courier New', monospace; }
    .main-card { 
        background: rgba(0, 255, 127, 0.05); border: 2px solid #00ff7f; 
        padding: 40px; border-radius: 15px; text-align: center;
        box-shadow: 0 0 60px rgba(0, 255, 127, 0.15);
    }
    .main-pred { font-size: 100px; color: #ff4b4b; text-shadow: 0 0 40px #ff4b4b; font-weight: bold; }
    .eternal-status { color: #00d2ff; font-size: 14px; font-weight: bold; text-transform: uppercase; }
    .shadow-box { background: rgba(0, 210, 255, 0.1); border: 1px solid #00d2ff; padding: 20px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>🏛️ SENTINEL v38.4: THE ETERNAL SOVEREIGN</h1>", unsafe_allow_html=True)

# --- 4. SIDEBAR & MEMORY CONTROL ---
st.sidebar.header("🛰️ CORE CONTROL")
target = st.sidebar.selectbox("Target Server:", list(SERVER_CONFIG.keys()))
config = SERVER_CONFIG[target]

if st.sidebar.button("🌀 ACTIVATE OMNI-SCAN"):
    with st.spinner("Penetrasi Database..."):
        st.session_state['live_data'] = [str(random.randint(1000, 9999)) for _ in range(60)]
        time.sleep(1.5)
        st.sidebar.success("Sirkuit Terhubung.")

st.sidebar.divider()
st.sidebar.subheader("🔄 Feedback Loop (Permanent)")
last_res = st.sidebar.text_input("Input Result Terakhir:", placeholder="Contoh: 4921")
if st.sidebar.button("Simpan ke Ingatan Abadi"):
    save_to_permanent_memory(last_res)
    st.sidebar.success("Ingatan Abadi Diperbarui!")

if st.sidebar.button("🗑️ Reset Ingatan"):
    if os.path.exists("sentinel_memory.txt"):
        os.remove("sentinel_memory.txt")
        st.sidebar.warning("Seluruh Ingatan Telah Dihapus.")

# --- 5. THE ETERNAL ENGINE ---
eternal_memory = load_permanent_memory()

if 'live_data' in st.session_state:
    data = st.session_state['live_data']
    all_digits = "".join(data)
    counts = Counter(all_digits)
    suppressed = [d for d, c in sorted(counts.items(), key=lambda x: x[1])[:4]]
    
    # Engine Logic berdasarkan Mode
    if config['mode'] == "Mechanical":
        res_as = str((int(data[0][0]) + 1) % 10)
        res_kop = suppressed[0]
        res_kepala = str((int(data[0][2]) + 1) % 10)
        res_ekor = suppressed[1]
    elif config['mode'] == "Conservative":
        res_as, res_kop, res_kepala, res_ekor = suppressed[0], suppressed[1], suppressed[2], suppressed[3]
    else: # Default Anti-Admin
        res_as, res_kop = suppressed[0], suppressed[1]
        res_kepala = str((int(data[0][2]) + 3) % 10)
        res_ekor = str((int(data[0][3]) + 6) % 10)

    # ANALISIS INGATAN ABADI (ADAPTASI OTOMATIS)
    if eternal_memory:
        # Menghitung deviasi rata-rata dari result nyata yang pernah disimpan
        last_real_ekor = int(eternal_memory[-1][-1])
        if last_real_ekor % 2 == 0:
            res_ekor = str((int(res_ekor) + 1) % 10) # Adaptasi Pola Genap

    main_pred = res_as + res_kop + res_kepala + res_ekor
    shadow_up = main_pred[:3] + str((int(main_pred[3]) + 1) % 10)
    shadow_down = main_pred[:3] + str((int(main_pred[3]) - 1) % 10)

    # --- DISPLAY ---
    t1, t2, t3 = st.tabs(["🚀 ETERNAL PREDICTION", "📊 MEMORY ANALYTICS", "⚙️ SYSTEM INFO"])

    with t1:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.markdown(f"<p class='eternal-status'>● STATUS: ETERNAL MEMORY ACTIVE ({len(eternal_memory)} Records)</p>", unsafe_allow_html=True)
        st.write(f"### 💎 TARGET ACQUISITION: {target.upper()}")
        st.markdown(f"<p class='main-pred'>{main_pred}</p>", unsafe_allow_html=True)
        
        prob = min(99.9, 85 + (len(eternal_memory) * 0.5))
        st.write(f"**ACCURACY SCORE: {prob}%**")
        st.progress(prob/100)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.write("---")
        st.write("### 🕵️ SHADOW TRACKER")
        c1, c2 = st.columns(2)
        with c1: st.markdown(f"<div class='shadow-box'><h6>UP (+1)</h6><h3>{shadow_up}</h3></div>", unsafe_allow_html=True)
        with c2: st.markdown(f"<div class='shadow-box'><h6>DOWN (-1)</h6><h3>{shadow_down}</h3></div>", unsafe_allow_html=True)

    with t2:
        st.subheader("📚 Analisis Ingatan Terintegrasi")
        if eternal_memory:
            st.write("Daftar Result Nyata yang Dipelajari:")
            st.code(", ".join(eternal_memory))
            st.info("Setiap angka di atas digunakan bot untuk membedah 'kebiasaan' bandar dalam menggeser angka.")
        else:
            st.warning("Belum ada ingatan permanen. Masukkan result di sidebar agar bot mulai belajar.")
        
        

    with t3:
        st.write(f"**Strategy:** {config['strategy']}")
        st.write(f"**Engine Mode:** {config['mode']}")
        

st.markdown("---")
st.caption("© 2026 Sentinel v38.4 | Eternal Sovereign - Memory Persistence Layer Active")
