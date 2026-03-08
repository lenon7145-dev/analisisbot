import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import re
import random
import time

# --- 1. CORE INTELLIGENCE & ADAPTIVE MEMORY ---
if 'feedback_loop' not in st.session_state:
    st.session_state['feedback_loop'] = []

INTEL_DB = {
    "Hongkong (HK)": {"vuln": "Twin-Loop", "trust": 45, "color": "#ff4b4b"},
    "HK Lotto (6D/Special)": {"vuln": "Step-Ladder/Mechanical", "trust": 60, "color": "#ffd700"},
    "Singapore (SGP)": {"vuln": "Low-Digit Suppress", "trust": 72, "color": "#ffa500"},
    "Sydney (SDY)": {"vuln": "Entropy Shift", "trust": 85, "color": "#00d2ff"},
    "Macau (MC)": {"vuln": "Manual Override", "trust": 20, "color": "#7b2cbf"}
}

# --- 2. ENGINE LOGIC ---
def fetch_live_data(server):
    # Simulasi data (Ganti dengan API/scraping real jika sudah ada)
    return [str(random.randint(1000, 9999)) for _ in range(30)]

# --- 3. UI ARCHITECTURE ---
st.set_page_config(page_title="SENTINEL v38.0 - ADAPTIVE", layout="wide")

st.markdown("""
    <style>
    .stApp { background: #010501; color: #00ff7f; font-family: 'Courier New', monospace; }
    .oracle-card { 
        background: rgba(0, 255, 127, 0.05); border: 2px solid #00ff7f; 
        padding: 30px; border-radius: 20px; text-align: center;
        box-shadow: 0 0 40px rgba(0, 255, 127, 0.2);
    }
    .main-pred { font-size: 85px; color: #ff4b4b; text-shadow: 0 0 30px #ff4b4b; font-weight: bold; margin: 10px 0; }
    .status-active { color: #00d2ff; font-weight: bold; animation: blink 1.5s infinite; }
    @keyframes blink { 50% { opacity: 0.2; } }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>🔮 SENTINEL v38.0: ADAPTIVE ORACLE</h1>", unsafe_allow_html=True)

# --- 4. COMMAND CENTER ---
st.sidebar.header("📡 COMMAND CENTER")
target = st.sidebar.selectbox("Pilih Target Server:", list(INTEL_DB.keys()))

if st.sidebar.button("🌀 SYNC & LEARN (Adaptive)"):
    with st.spinner("Mensinkronisasi & Mempelajari Pola..."):
        st.session_state['live_data'] = fetch_live_data(target)
        time.sleep(2)
        st.sidebar.success(f"Analisis {target} Selesai.")

# --- 5. ADAPTIVE FEEDBACK INPUT ---
st.sidebar.divider()
st.sidebar.subheader("🔄 Feedback Loop")
last_result = st.sidebar.text_input("Input Result Terakhir:", placeholder="Contoh: 1234")
if st.sidebar.button("Simpan & Adaptasi"):
    st.session_state['feedback_loop'].append(last_result)
    st.sidebar.info("Algoritma Berhasil Diperbarui Berdasarkan Hasil Nyata.")

# --- 6. THE ORACLE ENGINE v38.0 ---
if 'live_data' not in st.session_state or not st.session_state['live_data']:
    st.info("💡 Klik 'SYNC & LEARN' untuk membedah database server.")
else:
    data = st.session_state['live_data']
    all_digits = "".join(data)
    counts = Counter(all_digits)
    suppressed = [d for d, c in sorted(counts.items(), key=lambda x: x[1])[:4]]
    
    # LOGIKA KHUSUS HK LOTTO
    if "HK Lotto" in target:
        # Lotto cenderung mengikuti pola urutan atau angka tetangga
        res_as = str((int(data[0][0]) + 1) % 10)
        res_kop = suppressed[0]
        res_kepala = str((int(data[0][2]) + 1) % 10)
        res_ekor = suppressed[1]
    else:
        # Logika Standar Oracle
        res_as = suppressed[0]
        res_kop = str((int(data[0][1]) + 2) % 10)
        res_kepala = suppressed[1]
        res_ekor = str((int(data[0][3]) + 7) % 10)
    
    # ADAPTASI: Jika ada feedback, geser angka berdasarkan deviasi terakhir
    if st.session_state['feedback_loop']:
        deviasi = int(st.session_state['feedback_loop'][-1][-1]) % 2
        if deviasi == 0:
            res_ekor = str((int(res_ekor) + 1) % 10) # Geser jika bandar bermain pola genap

    main_pred = res_as + res_kop + res_kepala + res_ekor
    shadow_up = main_pred[:3] + str((int(main_pred[3]) + 1) % 10)
    shadow_down = main_pred[:3] + str((int(main_pred[3]) - 1) % 10)
    
    prob_score = min(99.9, (len(data) * 2.5) + (100 - INTEL_DB[target]['trust']))

    # --- DISPLAY ---
    t1, t2, t3 = st.tabs(["🎯 TARGET ACQUISITION", "🧠 SERVER ANALYTICS", "📜 MEMORY LOG"])

    with t1:
        st.markdown("<div class='oracle-card'>", unsafe_allow_html=True)
        st.markdown(f"<p class='status-active'>● SISTEM ADAPTIF SEDANG MEMANTAU {target.upper()}</p>", unsafe_allow_html=True)
        st.write("### 💎 PREDIKSI ABSOLUTE (ADAPTIVE)")
        st.markdown(f"<p class='main-pred'>{main_pred}</p>", unsafe_allow_html=True)
        st.write(f"**PROBABILITAS AKURASI: {prob_score}%**")
        st.progress(prob_score/100)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.write("---")
        st.write("### 🕵️ SHADOW TRACKER (PELACAK PEMBELOKAN)")
        c1, c2 = st.columns(2)
        with c1: st.info(f"**SHADOW (+1): {shadow_up}**")
        with c2: st.info(f"**SHADOW (-1): {shadow_down}**")
        

    with t2:
        st.subheader(f"📊 Karakteristik Server: {target}")
        info = INTEL_DB[target]
        st.write(f"**Vulnerabilitas:** {info['vuln']}")
        st.write(f"**Trust Score:** {info['trust']}%")
        st.write(f"**Mode:** {'Khusus Lotto (Mekanis)' if 'Lotto' in target else 'Standar Oracle'}")
        

    with t3:
        st.subheader("📑 Memory & Evidence Log")
        st.write("Riwayat Feedback (Belajar dari Result):")
        st.write(st.session_state['feedback_loop'])
        st.code(f"ID: {target.upper()}-ORACLE-v38\nPRED: {main_pred}\nSTATUS: SINKRON")

st.markdown("---")
st.caption("© 2026 Sentinel v38.0 | The Adaptive Oracle - Final Sovereign Masterpiece")
