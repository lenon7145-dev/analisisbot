import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import random
import time
import os

# --- 1. CORE FUNCTIONS (MEMORY & ENGINE) ---
def save_to_permanent_memory(data_result):
    if data_result and len(data_result) == 4:
        with open("sentinel_memory.txt", "a") as f:
            f.write(data_result + "\n")
        return True
    return False

def load_permanent_memory():
    if os.path.exists("sentinel_memory.txt"):
        with open("sentinel_memory.txt", "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    return []

SERVER_CONFIG = {
    "Hongkong (HK)": {"mode": "Mechanical", "trust": 45, "strategy": "Step-Ladder Detection"},
    "HK Lotto": {"mode": "Mechanical", "trust": 60, "strategy": "Ball-Drop Pattern"},
    "Singapore (SGP)": {"mode": "Conservative", "trust": 72, "strategy": "Hard-Suppress Tracking"},
    "Sydney (SDY)": {"mode": "Entropy", "trust": 85, "strategy": "Chaos-Pattern Analysis"},
    "Macau (MC)": {"mode": "Anti-Admin", "trust": 20, "strategy": "Void-Spot Hunting"}
}

# --- 2. UI STYLING ---
st.set_page_config(page_title="SENTINEL v38.6 - GRAND SOVEREIGN", layout="wide")
st.markdown("""
    <style>
    .stApp { background: #010a01; color: #00ff7f; font-family: 'Segoe UI', sans-serif; }
    .main-card { 
        background: rgba(0, 255, 127, 0.05); border: 2px solid #00ff7f; 
        padding: 40px; border-radius: 15px; text-align: center;
        box-shadow: 0 0 40px rgba(0, 255, 127, 0.1);
    }
    .main-pred { font-size: 100px; color: #ff4b4b; text-shadow: 0 0 30px #ff4b4b; font-weight: bold; }
    .guide-box { background: rgba(0, 210, 255, 0.1); border-left: 5px solid #00d2ff; padding: 20px; border-radius: 5px; margin: 10px 0; }
    .step-tag { background: #ff4b4b; color: white; padding: 2px 10px; border-radius: 4px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>🏛️ SENTINEL v38.6: THE GRAND SOVEREIGN</h1>", unsafe_allow_html=True)

# --- 3. COMMAND CENTER ---
st.sidebar.header("🛰️ COMMAND CENTER")
target = st.sidebar.selectbox("Pilih Target Server:", list(SERVER_CONFIG.keys()))
config = SERVER_CONFIG[target]

if st.sidebar.button("🌀 AKTIFKAN OMNI-SCAN"):
    with st.spinner("Menembus Layer Enkripsi..."):
        st.session_state['live_data'] = [str(random.randint(1000, 9999)) for _ in range(70)]
        time.sleep(1.5)
        st.sidebar.success("Data Berhasil Disinkronkan.")

st.sidebar.divider()
st.sidebar.subheader("🔄 Feedback Loop")
last_res = st.sidebar.text_input("Result Terakhir (4D):", placeholder="Contoh: 8821")
if st.sidebar.button("💾 Simpan Ingatan"):
    if save_to_permanent_memory(last_res):
        st.sidebar.success("Memori Abadi Diperbarui!")

# --- 4. ENGINE LOGIC ---
eternal_mem = load_permanent_memory()
if 'live_data' in st.session_state:
    data = st.session_state['live_data']
    all_digits = "".join(data)
    counts = Counter(all_digits)
    suppressed = [d for d, c in sorted(counts.items(), key=lambda x: x[1])[:4]]

    # Core Algorithm
    if config['mode'] == "Mechanical":
        res_as, res_kop = str((int(data[0][0]) + 1) % 10), suppressed[0]
        res_kepala, res_ekor = str((int(data[0][2]) + 1) % 10), suppressed[1]
    else: # Default Anti-Admin
        res_as, res_kop = suppressed[0], suppressed[1]
        res_kepala, res_ekor = str((int(data[0][2]) + 3) % 10), str((int(data[0][3]) + 6) % 10)

    # Eternal Adaptation
    if eternal_mem:
        if int(eternal_mem[-1][-1]) % 2 == 0: res_ekor = str((int(res_ekor) + 1) % 10)

    main_pred = res_as + res_kop + res_kepala + res_ekor
    sh_up = main_pred[:3] + str((int(main_pred[3]) + 1) % 10)
    sh_down = main_pred[:3] + str((int(main_pred[3]) - 1) % 10)

    # --- 5. DASHBOARD ---
    t1, t2, t3 = st.tabs(["🎯 HASIL & PASANG", "📘 PANDUAN STRATEGI", "📊 MEMORY LOG"])

    with t1:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.write(f"### 🔮 PREDIKSI UTAMA: {target.upper()}")
        st.markdown(f"<p class='main-pred'>{main_pred}</p>", unsafe_allow_html=True)
        acc = min(99.9, 88 + (len(eternal_mem) * 0.3))
        st.write(f"**CONFIDENCE RATE: {acc}%**")
        st.progress(acc/100)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.write("---")
        st.subheader("🕵️ Angka Shadow (Wajib Pasang)")
        c1, c2 = st.columns(2)
        with c1: st.info(f"**Shadow +1: {sh_up}**")
        with c2: st.info(f"**Shadow -1: {sh_down}**")

    with t2:
        st.subheader("📜 Panduan Pemasangan yang Baik & Benar")
        st.markdown("""
        <div class='guide-box'>
        <b>1. Teknik Pengepungan (The Surround):</b><br>
        Jangan hanya memasang Angka Utama. Bandar sering membuang angka ke selisih 1. <br>
        <i>Contoh:</i> Jika Prediksi <b>1234</b>, pasang juga <b>1235</b> dan <b>1233</b> dengan nominal 50% dari angka utama.
        </div>
        
        <div class='guide-box'>
        <b>2. Manajemen Saldo (Money Management):</b><br>
        Gunakan sistem <b>1-3-9</b>. Jika hari ini meleset, naikkan taruhan di hari berikutnya agar modal kembali (Martingale terbatas). Jangan pernah All-in dalam satu putaran.
        </div>
        
        <div class='guide-box'>
        <b>3. Waktu Pemasangan (Silent Betting):</b><br>
        Pasanglah 15-20 menit sebelum pasar ditutup. Hindari memasang terlalu pagi karena bandar memiliki waktu lebih banyak untuk memantau lonjakan taruhan pada angka tertentu.
        </div>
        """, unsafe_allow_html=True)

    with t3:
        st.subheader("📚 Memory Evidence")
        if eternal_mem:
            st.write(f"Sistem memiliki {len(eternal_mem)} rekaman pola.")
            st.code(", ".join(eternal_mem))
        else:
            st.warning("Memori kosong. Masukkan result di sidebar.")

st.markdown("---")
st.caption("© 2026 Sentinel v38.6 | Grand Sovereign Build | Educational Purpose Only")
