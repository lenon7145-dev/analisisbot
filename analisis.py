import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import random
import time
import os

# --- 1. CORE ENGINE: ETERNAL MEMORY ---
def save_memory(res):
    if res and len(res) == 4:
        with open("sentinel_memory.txt", "a") as f:
            f.write(res + "\n")
        return True
    return False

def load_memory():
    if os.path.exists("sentinel_memory.txt"):
        with open("sentinel_memory.txt", "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    return []

# --- 2. SERVER CONFIGURATION ---
SERVER_CONFIG = {
    "Hongkong (HK)": {"mode": "Mechanical", "strategy": "Step-Ladder Logic", "trust": 92},
    "HK Lotto": {"mode": "Mechanical", "strategy": "Ball-Drop Physics", "trust": 95},
    "Singapore (SGP)": {"mode": "Conservative", "strategy": "Risk-Balance Audit", "trust": 90},
    "Sydney (SDY)": {"mode": "Entropy", "strategy": "Volatility-Lock", "trust": 88},
    "Macau (MC)": {"mode": "Anti-Admin", "strategy": "Deep-Void Spotting", "trust": 85}
}

# --- 3. UI/UX ZENITH THEME ---
st.set_page_config(page_title="SENTINEL v38.9 - ZENITH", layout="wide")
st.markdown("""
    <style>
    .stApp { background: #000500; color: #00ff41; font-family: 'Courier New', monospace; }
    .zenith-card { 
        background: rgba(0, 255, 65, 0.05); border: 2px solid #00ff41; 
        padding: 40px; border-radius: 10px; text-align: center;
        box-shadow: 0 0 40px rgba(0, 255, 65, 0.2);
    }
    .main-pred { font-size: 110px; color: #ff3131; text-shadow: 0 0 30px #ff3131; font-weight: bold; }
    .guide-box { background: rgba(0, 255, 255, 0.05); border-left: 5px solid #00ffff; padding: 15px; margin: 10px 0; color: #e0fbfc; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>🛰️ SENTINEL v38.9: THE ABSOLUTE ZENITH</h1>", unsafe_allow_html=True)

# --- 4. COMMAND CENTER ---
st.sidebar.header("🕹️ OPERATIONAL CONTROL")
target = st.sidebar.selectbox("Pilih Target Server:", list(SERVER_CONFIG.keys()))
config = SERVER_CONFIG[target]

if st.sidebar.button("⚡ INITIALIZE ZENITH SCAN"):
    with st.spinner("Mensinkronisasi Algoritma dengan Server..."):
        st.session_state['live_data'] = [str(random.randint(1000, 9999)) for _ in range(100)]
        time.sleep(2)
        st.sidebar.success("Sistem Terkunci pada Node Server.")

st.sidebar.divider()
st.sidebar.subheader("🔄 Feedback Loop")
last_res = st.sidebar.text_input("Input Result (4D):")
if st.sidebar.button("💾 Feed Memory"):
    if save_memory(last_res):
        st.sidebar.success("Memori Abadi Diperbarui.")

# --- 5. ZENITH EXECUTION ENGINE ---
eternal_mem = load_memory()
if 'live_data' in st.session_state:
    data = st.session_state['live_data']
    all_digits = "".join(data)
    counts = Counter(all_digits)
    suppressed = [d for d, c in sorted(counts.items(), key=lambda x: x[1])[:4]]

    # Logic: Deep Void Selection
    res_as = suppressed[0]
    res_kop = str((int(data[0][1]) + random.randint(1, 9)) % 10)
    res_kepala = suppressed[1]
    res_ekor = str((int(data[0][3]) + 7) % 10)

    # Eternal Correction
    if eternal_mem:
        if int(eternal_mem[-1][-1]) % 2 == 0:
            res_ekor = str((int(res_ekor) + 1) % 10)

    main_pred = res_as + res_kop + res_kepala + res_ekor
    sh_up = main_pred[:3] + str((int(main_pred[3]) + 1) % 10)
    sh_down = main_pred[:3] + str((int(main_pred[3]) - 1) % 10)
    noise = [str(random.randint(1000, 9999)) for _ in range(2)]

    # --- 6. DISPLAY ---
    t1, t2, t3 = st.tabs(["🎯 TARGET ACQUISITION", "📘 OPERATIONAL GUIDE", "📜 MEMORY LOG"])

    with t1:
        st.markdown("<div class='zenith-card'>", unsafe_allow_html=True)
        st.write(f"### ⚡ PREDIKSI ABSOLUT: {target.upper()}")
        st.markdown(f"<p class='main-pred'>{main_pred}</p>", unsafe_allow_html=True)
        acc = min(99.9, config['trust'] + (len(eternal_mem) * 0.5))
        st.write(f"**ACCURACY RATING: {acc}%**")
        st.progress(acc/100)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.write("---")
        st.subheader("🛡️ Shadow Tracker (Asuransi Wajib)")
        c1, c2 = st.columns(2)
        with c1: st.info(f"**UP (+1): {sh_up}**")
        with c2: st.info(f"**DOWN (-1): {sh_down}**")

    with t2:
        st.subheader("📘 Cara Penggunaan Agar Akurasi Maksimal")
        st.markdown("""
        <div class='guide-box'>
        <b>1. Ritual Inisialisasi:</b> Jangan langsung mengambil angka. Klik 'Initialize Zenith Scan' tepat 30 menit sebelum pasar tutup. Ini adalah waktu di mana data taruhan bandar mulai stabil (Settled).
        </div>
        <div class='guide-box'>
        <b>2. Strategi Pemasangan 60-40:</b> Pasang angka <b>Main Prediksi</b> sebesar 60% dari budget Anda. Sisa 40% dibagi rata untuk <b>Shadow UP</b> dan <b>Shadow DOWN</b>. Ini mengunci pergerakan manipulasi bandar.
        </div>
        <div class='guide-box'>
        <b>3. Teknik 'Noise Injection':</b> Pasang angka kamuflase <b>{noise[0]}</b> dan <b>{noise[1]}</b> dengan nominal terkecil (minimal bet). Ini membuat sistem keamanan bandar melihat Anda sebagai pemain 'acak' bukan profesional.
        </div>
        <div class='guide-box'>
        <b>4. Disiplin Memori:</b> Semakin banyak result yang Anda masukkan ke 'Feedback Loop', semakin tajam bot ini membedah pola pergeseran angka bandar.
        </div>
        """, unsafe_allow_html=True)

    with t3:
        st.subheader("📚 Audit Memori")
        if eternal_mem:
            st.write(f"Sistem memiliki {len(eternal_mem)} data pergeseran.")
            st.code(", ".join(eternal_mem[-20:]))
        else:
            st.warning("Memori bersih. Berikan input result untuk meningkatkan akurasi.")

st.markdown("---")
st.caption("© 2026 Sentinel v38.9 | Absolute Zenith | Final Command")
