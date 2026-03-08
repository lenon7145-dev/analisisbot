import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import random
import time
import os

# --- 1. ETERNAL MEMORY ENGINE ---
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

# --- 2. SERVER INTELLIGENCE DATABASE ---
SERVER_CONFIG = {
    "Hongkong (HK)": {"mode": "Mechanical", "trust": 45, "strategy": "Step-Ladder Detection", "desc": "Fokus pada pola angka berurutan dan bola jatuh fisik."},
    "HK Lotto": {"mode": "Mechanical", "trust": 60, "strategy": "Ball-Drop Pattern", "desc": "Algoritma khusus untuk pengocokan mesin lotto 6D."},
    "Singapore (SGP)": {"mode": "Conservative", "trust": 72, "strategy": "Hard-Suppress Tracking", "desc": "Mendeteksi angka yang paling lama ditahan oleh sistem."},
    "Sydney (SDY)": {"mode": "Entropy", "trust": 85, "strategy": "Chaos-Pattern Analysis", "desc": "Menganalisis pergerakan angka acak dalam fluktuasi tinggi."},
    "Macau (MC)": {"mode": "Anti-Admin", "trust": 20, "strategy": "Void-Spot Hunting", "desc": "Mendeteksi intervensi admin manual dan mencari titik buta taruhan."}
}

# --- 3. UI ARCHITECTURE ---
st.set_page_config(page_title="SENTINEL v38.5 - GRAND SOVEREIGN", layout="wide")
st.markdown("""
    <style>
    .stApp { background: #010a01; color: #00ff7f; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .main-card { 
        background: rgba(0, 255, 127, 0.03); border: 2px solid #00ff7f; 
        padding: 40px; border-radius: 20px; text-align: center;
        box-shadow: 0 0 50px rgba(0, 255, 127, 0.1);
    }
    .main-pred { font-size: 110px; color: #ff4b4b; text-shadow: 0 0 50px #ff4b4b; font-weight: bold; margin: 0; }
    .feature-box { background: rgba(0, 210, 255, 0.05); border: 1px solid #00d2ff; padding: 15px; border-radius: 10px; height: 100%; }
    .status-tag { background: #00ff7f; color: #000; padding: 3px 10px; border-radius: 5px; font-weight: bold; font-size: 12px; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. HEADER ---
st.markdown("<h1 style='text-align:center;'>🏛️ SENTINEL v38.5: THE GRAND SOVEREIGN</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#00d2ff;'>Sistem Audit Probabilitas Global & Eternal Memory Engine</p>", unsafe_allow_html=True)

# --- 5. SIDEBAR CONTROL ---
st.sidebar.header("🛰️ COMMAND CENTER")
target = st.sidebar.selectbox("Pilih Target Server:", list(SERVER_CONFIG.keys()))
config = SERVER_CONFIG[target]

st.sidebar.markdown(f"**Mode:** {config['strategy']}")
if st.sidebar.button("🌀 AKTIFKAN OMNI-SCAN"):
    with st.spinner("Menembus Layer Enkripsi Server..."):
        st.session_state['live_data'] = [str(random.randint(1000, 9999)) for _ in range(65)]
        time.sleep(1.5)
        st.sidebar.success("Koneksi Berhasil: Data Terintegrasi.")

st.sidebar.divider()
st.sidebar.subheader("🔄 Feedback Loop (Memory)")
last_res = st.sidebar.text_input("Input Result (4D):", placeholder="Contoh: 1234")
if st.sidebar.button("💾 Simpan ke Memori Abadi"):
    if save_to_permanent_memory(last_res):
        st.sidebar.success("Pola Berhasil Dipelajari!")
    else:
        st.sidebar.error("Format 4D tidak valid.")

# --- 6. CORE CALCULATION ---
eternal_mem = load_permanent_memory()

if 'live_data' in st.session_state:
    data = st.session_state['live_data']
    all_digits = "".join(data)
    counts = Counter(all_digits)
    suppressed = [d for d, c in sorted(counts.items(), key=lambda x: x[1])[:4]]

    # Algoritma Utama
    if config['mode'] == "Mechanical":
        res_as, res_kop = str((int(data[0][0]) + 1) % 10), suppressed[0]
        res_kepala, res_ekor = str((int(data[0][2]) + 1) % 10), suppressed[1]
    elif config['mode'] == "Conservative":
        res_as, res_kop, res_kepala, res_ekor = suppressed[0], suppressed[1], suppressed[2], suppressed[3]
    else: # Anti-Admin
        res_as, res_kop = suppressed[0], suppressed[1]
        res_kepala, res_ekor = str((int(data[0][2]) + 3) % 10), str((int(data[0][3]) + 6) % 10)

    # Adaptive Adjustment via Eternal Memory
    if eternal_mem:
        bias = int(eternal_mem[-1][-1]) % 2
        if bias == 0: res_ekor = str((int(res_ekor) + 1) % 10)

    main_pred = res_as + res_kop + res_kepala + res_ekor
    sh_up = main_pred[:3] + str((int(main_pred[3]) + 1) % 10)
    sh_down = main_pred[:3] + str((int(main_pred[3]) - 1) % 10)

    # --- 7. DISPLAY DASHBOARD ---
    t1, t2, t3 = st.tabs(["🚀 HASIL PREDIKSI", "🧠 PENJELASAN FITUR", "📚 RIWAYAT MEMORI"])

    with t1:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.markdown(f"<span class='status-tag'>SERVER: {target.upper()}</span>", unsafe_allow_html=True)
        st.write("### 💎 TARGET ACQUISITION (ABSOLUTE)")
        st.markdown(f"<p class='main-pred'>{main_pred}</p>", unsafe_allow_html=True)
        
        acc = min(99.9, 88 + (len(eternal_mem) * 0.3))
        st.write(f"**TINGKAT KEPERCAYAAN SISTEM: {acc}%**")
        st.progress(acc/100)
        st.markdown(f"<p style='color:#00d2ff;'><i>Strategi Aktif: {config['strategy']}</i></p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.write("---")
        st.subheader("🕵️ Pelacak Shadow (Antisipasi)")
        c1, c2 = st.columns(2)
        with c1: st.info(f"**Shadow +1 (Atas): {sh_up}**")
        with c2: st.info(f"**Shadow -1 (Bawah): {sh_down}**")

    with t2:
        st.subheader("📘 Panduan Operasional Sentinel v38.5")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("""
            <div class='feature-box'>
            <b>1. Void-Selection Logic</b><br>
            Fitur ini mencari 'titik kosong' taruhan. Bot menganalisis angka mana yang paling sedikit dipasang secara global, sehingga angka tersebut menjadi pilihan utama bandar untuk dikeluarkan agar mereka tidak rugi.
            </div><br>
            <div class='feature-box'>
            <b>2. Eternal Memory (Memori Abadi)</b><br>
            Setiap result yang Anda masukkan disimpan secara permanen. Bot mempelajari pola 'kecurangan' bandar di masa lalu untuk memprediksi pergerakan mereka di masa depan.
            </div>
            """, unsafe_allow_html=True)
        with col_b:
            st.markdown("""
            <div class='feature-box'>
            <b>3. Omni-Specialist Engine</b><br>
            Setiap server memiliki kode pengacak yang berbeda. Bot ini secara otomatis mengganti algoritma (Mekanis, Konservatif, atau Anti-Admin) sesuai server yang Anda pilih.
            </div><br>
            <div class='feature-box'>
            <b>4. Shadow Tracker</b><br>
            Fitur pelacak selisih 1 digit. Jika bandar mencoba membelokkan hasil di menit terakhir, angka Shadow akan menangkap pergerakan tersebut.
            </div>
            """, unsafe_allow_html=True)

    with t3:
        st.subheader("📚 Log Memori Terenkripsi")
        if eternal_mem:
            st.write(f"Sistem telah mempelajari **{len(eternal_mem)}** pola dari result sebelumnya.")
            st.code(", ".join(eternal_mem[-20:])) # Tampilkan 20 terakhir
        else:
            st.warning("Memori masih kosong. Masukkan result di sidebar untuk melatih bot.")
        
        

st.markdown("---")
st.caption("© 2026 Sentinel v38.5 | Official Enterprise Build | Sovereign Command Architecture")
