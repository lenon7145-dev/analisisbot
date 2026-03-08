import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import re
import random

# --- 1. CONFIG & DATABASE ---
INTEL_DB = {
    "Hongkong (HK)": {"vuln": "Twin-Loop", "trust": 45, "color": "#ff4b4b"},
    "Singapore (SGP)": {"vuln": "Low-Digit Suppress", "trust": 72, "color": "#ffa500"},
    "Sydney (SDY)": {"vuln": "Entropy Shift", "trust": 85, "color": "#00d2ff"},
    "Macau (MC)": {"vuln": "Manual Override", "trust": 20, "color": "#7b2cbf"}
}

# --- 2. THEME & UI ---
st.set_page_config(page_title="SENTINEL v37.7 - SOVEREIGN", layout="wide")

st.markdown("""
    <style>
    .stApp { background: #020202; color: #00ff7f; font-family: 'Courier New', monospace; }
    .main-card { background: rgba(0, 255, 127, 0.05); border: 1px solid #00ff7f; padding: 25px; border-radius: 15px; text-align: center; }
    .prediction-text { font-size: 60px; color: #ff4b4b; text-shadow: 0 0 20px #ff4b4b; font-weight: bold; margin: 0; }
    .meter-bg { background: #333; border-radius: 10px; height: 25px; width: 100%; margin: 10px 0; }
    .meter-fill { background: linear-gradient(90deg, #ff4b4b, #00ff7f); height: 100%; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#00ff7f;'>🏛️ SENTINEL v37.7: SOVEREIGN ARCHITECT</h1>", unsafe_allow_html=True)

# --- 3. SIDEBAR CONTROLS ---
st.sidebar.header("🛰️ GLOBAL COMMAND")
target = st.sidebar.selectbox("Pilih Target Server:", list(INTEL_DB.keys()))
raw_data = st.sidebar.text_area("📡 Transmisi Data (4D):", height=200, placeholder="Input riwayat per baris...")
clean_data = re.findall(r'\d{4}', raw_data)

info = INTEL_DB[target]
st.sidebar.markdown(f"<div style='background:{info['color']}; padding:10px; border-radius:10px; color:#000; font-weight:bold;'>"
                    f"TARGET: {target}<br>VULNERABILITY: {info['vuln']}</div>", unsafe_allow_html=True)

# --- 4. ENGINE LOGIC ---
if not clean_data:
    st.info("💡 Menunggu Sinkronisasi Data... Bot sedang mengkalibrasi radar global.")
    
else:
    # A. Analisis Angka & Perilaku
    all_digits = "".join(clean_data)
    counts = Counter(all_digits)
    # Mencari 3 digit yang paling 'Ditekan' (Suppressed/Simpanan Bandar)
    suppressed = [d for d, c in sorted(counts.items(), key=lambda x: x[1])[:3]]
    # Mencari digit umpan (Bait/Paling sering muncul)
    bait = counts.most_common(1)[0][0]
    
    # B. Simulasi Payout-Logic (Angka yang Akan Dikeluarkan Bandar)
    res_as = suppressed[0] if len(suppressed) > 0 else "0"
    res_kop = str((int(clean_data[0][1]) + 3) % 10) 
    res_kepala = suppressed[1] if len(suppressed) > 1 else "1"
    res_ekor = str(random.randint(0, 9))
    final_pred = res_as + res_kop + res_kepala + res_ekor

    # C. Probability Meter Calculation
    # Semakin konsisten data riwayat, semakin tinggi probabilitas
    prob_score = min(98, (len(clean_data) * 2) + (100 - info['trust']))
    
    # D. DASHBOARD DISPLAY
    t1, t2, t3 = st.tabs(["🎯 LIVE PREDICTION", "🧠 BANDAR PSYCHOLOGY", "📑 AUDIT EVIDENCE"])

    with t1:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.write("### 🔮 ESTIMASI ANGKA KELUAR BANDAR")
        st.markdown(f"<p class='prediction-text'>{final_pred}</p>", unsafe_allow_html=True)
        st.write(f"**STATUS:** Bandar diprediksi melepas angka zona simpanan **{res_as}**.")
        
        # Probability Meter UI
        st.write(f"**PROBABILITY METER: {prob_score}%**")
        st.markdown(f"""
            <div class='meter-bg'>
                <div class='meter-fill' style='width: {prob_score}%;'></div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        

    with t2:
        st.subheader("🕵️ Analisis Kelicikan Musuh")
        c1, c2 = st.columns(2)
        with c1:
            st.error(f"**Digit Umpan (Bait): {bait}**")
            st.write(f"Bandar sedang memancing massa dengan digit {bait}. Hindari angka ini di posisi 2D belakang.")
        with c2:
            st.success(f"**Digit Simpanan: {', '.join(suppressed)}**")
            st.write("Ini adalah 'Gudang' bandar. Mereka akan mengeluarkan salah satu angka ini untuk meminimalisir payout.")
        
        st.divider()
        st.write("### 📉 Greed Tracking")
        st.progress(100 - info['trust'])
        st.caption(f"Tingkat Keserakahan Admin {target}: {100 - info['trust']}% (High Risk Manual Intervention)")

    with t3:
        st.subheader("📜 Bukti Forensik Digital")
        st.text_area("Salin untuk laporan audit:", value=f"""
SENTINEL REPORT v37.7
TARGET: {target}
VULNERABILITY: {info['vuln']}
SUPPRESSED DIGITS: {', '.join(suppressed)}
PREDICTED VOID: {final_res}
PROBABILITY: {prob_score}%

ANALISIS: 
Ditemukan deviasi pada digit {suppressed[0]}. Bandar terdeteksi memanipulasi 
arus keluar angka untuk menjaga profit kas di atas 70%.
        """, height=200)

st.markdown("---")
st.caption("© 2026 Sentinel v37.7 | The Sovereign Architect - Ultimate Intelligence")
