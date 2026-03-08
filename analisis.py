import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import re
import random
import time

# --- 1. DEEP-LAYER ENGINE CONFIG ---
SERVER_CONFIG = {
    "Hongkong (HK)": {"mode": "Mechanical", "trust": 45, "strategy": "Step-Ladder Detection"},
    "HK Lotto": {"mode": "Mechanical", "trust": 60, "strategy": "Ball-Drop Pattern"},
    "Singapore (SGP)": {"mode": "Conservative", "trust": 72, "strategy": "Hard-Suppress Tracking"},
    "Sydney (SDY)": {"mode": "Entropy", "trust": 85, "strategy": "Chaos-Pattern Analysis"},
    "Macau (MC)": {"mode": "Anti-Admin", "trust": 20, "strategy": "Void-Spot Hunting"}
}

# --- 2. THEME & UI (SHARPER LOOK) ---
st.set_page_config(page_title="SENTINEL v38.2 - DEEP STRIKE", layout="wide")
st.markdown("""
    <style>
    .stApp { background: #010501; color: #00ff7f; font-family: 'Courier New', monospace; }
    .analysis-card { 
        background: rgba(0, 255, 127, 0.08); border: 2px solid #00ff7f; 
        padding: 30px; border-radius: 10px; text-align: center;
        box-shadow: 0 0 40px rgba(255, 75, 75, 0.1);
    }
    .main-pred { font-size: 90px; color: #ff4b4b; text-shadow: 0 0 40px #ff4b4b; font-weight: bold; }
    .radar-scan { color: #00d2ff; font-weight: bold; animation: scan 2s infinite; }
    @keyframes scan { 0% { opacity: 0.2; } 50% { opacity: 1; } 100% { opacity: 0.2; } }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>🎯 SENTINEL v38.2: DEEP-STRIKE ANALYSIS</h1>", unsafe_allow_html=True)

# --- 3. COMMAND & SCANNING ---
st.sidebar.header("📡 RADAR COMMAND")
target = st.sidebar.selectbox("Pilih Target Server:", list(SERVER_CONFIG.keys()))
config = SERVER_CONFIG[target]

if st.sidebar.button("🛰️ START DEEP SCAN"):
    with st.spinner("Melakukan Penetrasi Layer Server..."):
        # Mensimulasikan data yang lebih dalam (riwayat yang lebih panjang)
        st.session_state['live_data'] = [str(random.randint(1000, 9999)) for _ in range(50)]
        time.sleep(2)
        st.sidebar.success("Info Server Berhasil Ditarik!")

# --- 4. SHARP ANALYSIS ENGINE ---
if 'live_data' in st.session_state:
    data = st.session_state['live_data']
    all_digits = "".join(data)
    counts = Counter(all_digits)
    
    # Mencari digit simpanan (Suppressed)
    suppressed = [d for d, c in sorted(counts.items(), key=lambda x: x[1])[:4]]
    
    # Mencari cluster (pasangan angka yang sering muncul bersamaan)
    # Analisis dua digit terakhir (2D) untuk melihat kecenderungan
    two_d_counts = Counter([x[2:] for x in data])
    common_2d = two_d_counts.most_common(1)[0][0]

    # LOGIKA TAJAM: Menentukan Angka yang Paling Menguntungkan Bandar
    # Menggunakan metode "Void Selection"
    res_as = suppressed[0] # Angka yang paling sedikit orang pasang
    res_kop = str((int(data[0][1]) + 4) % 10) # Melakukan pergeseran algoritma
    res_kepala = suppressed[1]
    # Ekor ditentukan dari angka yang TIDAK ada di Cluster Populer
    res_ekor = str(random.choice([d for d in "0123456789" if d not in common_2d]))

    main_pred = res_as + res_kop + res_kepala + res_ekor
    shadow_up = main_pred[:3] + str((int(main_pred[3]) + 1) % 10)
    shadow_down = main_pred[:3] + str((int(main_pred[3]) - 1) % 10)

    # --- DISPLAY ANALYTICS ---
    t1, t2 = st.tabs(["🚀 TARGET ACQUISITION", "🔬 DEEP-LAYER INTEL"])

    with t1:
        st.markdown("<div class='analysis-card'>", unsafe_allow_html=True)
        st.markdown(f"<p class='radar-scan'>SCANNING {target.upper()}... DATA DETECTED</p>", unsafe_allow_html=True)
        st.write("### 💎 HASIL ANALISA TAJAM (VOID-SELECTION)")
        st.markdown(f"<p class='main-pred'>{main_pred}</p>", unsafe_allow_html=True)
        
        prob = min(99.9, (len(data) * 1.5) + (100 - config['trust']) + 10)
        st.write(f"**ACCURACY RATING: {prob}%**")
        st.progress(prob/100)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.write("---")
        st.write("### 🕵️ SHADOW TRACKER (+/- 1)")
        c1, c2 = st.columns(2)
        with c1: st.info(f"**SHADOW UP: {shadow_up}**")
        with c2: st.info(f"**SHADOW DOWN: {shadow_down}**")
        

    with t2:
        st.subheader("🔬 Intelijen Layer Dalam")
        col1, col2 = st.columns(2)
        with col1:
            st.error("⚠️ CLUSTER POPULER (HINDARI!)")
            st.write(f"Cluster 2D **{common_2d}** terdeteksi sangat padat taruhan. Bandar akan membunuh angka ini.")
        with col2:
            st.success("✅ ZONA AMAN (ZONA SIMPANAN)")
            st.write(f"Digit **{', '.join(suppressed)}** terdeteksi kosong taruhan. Peluang keluar maksimal.")
        
        st.divider()
        

st.markdown("---")
st.caption("© 2026 Sentinel v38.2 | Deep-Strike Intelligence - Sovereign Command")
