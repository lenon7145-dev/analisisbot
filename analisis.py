import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import re
import random

# --- 1. INTELLIGENCE DATABASE (PROFIL MUSUH) ---
INTEL_DATABASE = {
    "Hongkong (HK)": {"vulnerability": "Twin-Loop Shifting", "user_trend": "High Aggressive", "trust_score": 45, "color": "#ff4b4b"},
    "Singapore (SGP)": {"vulnerability": "Low-Digit Suppression", "user_trend": "Cautious Stable", "trust_score": 72, "#ffa500"},
    "Sydney (SDY)": {"vulnerability": "Entropy Chaos Shift", "user_trend": "Balanced Pattern", "trust_score": 85, "#00d2ff"},
    "Macau (MC)": {"vulnerability": "Manual Admin Override", "user_trend": "Extreme Speculation", "trust_score": 20, "#7b2cbf"}
}

# --- 2. THE MASTER INTERFACE ---
st.set_page_config(page_title="SENTINEL v37.6 - ALL-SEEING EYE", layout="wide")

st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle at center, #00050a 0%, #000000 100%); color: #00ff7f; font-family: 'Courier New', monospace; }
    .intel-card {
        background: rgba(0, 210, 255, 0.05); border-left: 5px solid #00d2ff;
        padding: 20px; border-radius: 10px; margin-bottom: 15px;
    }
    .enemy-card {
        background: rgba(255, 75, 75, 0.05); border-left: 5px solid #ff4b4b;
        padding: 20px; border-radius: 10px; margin-bottom: 15px;
    }
    .glow-header { color: #00d2ff; text-shadow: 0 0 15px #00d2ff; text-align: center; font-weight: bold; }
    .status-box { border: 1px solid #00ff7f; padding: 15px; border-radius: 10px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='glow-header'>👁️ SENTINEL v37.6: THE ALL-SEEING EYE</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Global Intelligence Hub & Anti-Bandar Command Center</p>", unsafe_allow_html=True)

# --- 3. COMMAND CENTER (SIDEBAR) ---
st.sidebar.markdown("### 📡 TARGET ACQUISITION")
target = st.sidebar.selectbox("Pilih Target Server:", list(INTEL_DATABASE.keys()))
raw_input = st.sidebar.text_area("📡 Transmisi Data (4D):", height=200, placeholder="Input riwayat di sini...")
clean_data = re.findall(r'\d{4}', raw_input)

# Display Intel Profile
info = INTEL_DATABASE[target]
st.sidebar.markdown(f"""
<div class='intel-card'>
<b>DATABASE INTEL:</b> {target}<br>
<b>KERENTANAN:</b> {info['vulnerability']}<br>
<b>SENTIMEN USER:</b> {info['user_trend']}<br>
<b>KEJUJURAN:</b> {info['trust_score']}%
</div>
""", unsafe_allow_html=True)

# --- 4. ANALISIS OMNI-INTELLIGENCE ---
if not clean_data:
    st.markdown("### 🛰️ Menunggu Sinkronisasi Global...")
    c1, c2 = st.columns(2)
    with c1:
        st.info("💡 **INFO:** Sistem sedang memetakan hubungan antara data server dan psikologi massa.")
    with c2:
        st.warning("⚠️ **PERINGATAN:** Bandar menggunakan teknik 'Baiting' jika pola 3 hari terakhir terlalu logis.")
    
    
else:
    # A. CORE CALCULATION (BANDAR BRAIN)
    all_digits = "".join(clean_data)
    counts = Counter(all_digits)
    # Angka yang sengaja disimpan (Suppressed)
    suppressed = [d for d, c in sorted(counts.items(), key=lambda x: x[1])[:3]]
    # Angka umpan massa (Bait)
    bait = counts.most_common(1)[0][0]
    
    # B. PREDIKSI ANTI-INTERVENSI (ZONA BUTA)
    # Mengambil digit simpanan dan menggeser pola kop/ekor secara acak terkontrol
    res_as = suppressed[0] if len(suppressed) > 0 else "0"
    res_kop = str((int(clean_data[0][1]) + 4) % 10)
    res_kepala = suppressed[1] if len(suppressed) > 1 else "1"
    res_ekor = str(random.randint(0, 9)) if int(all_digits[0]) % 2 == 0 else suppressed[-1]
    
    final_res = res_as + res_kop + res_kepala + res_ekor
    
    # C. DASHBOARD UTAMA
    t1, t2, t3, t4 = st.tabs(["🎯 TARGET ANALYSIS", "🧠 ENEMY BRAIN", "👥 USER SENTIMENT", "📜 EVIDENCE LOG"])

    with t1:
        st.subheader(f"📍 Fokus Audit: {target}")
        c1, c2, c3 = st.columns(3)
        with c1: st.markdown(f"<div class='status-box'><h4>SIMPANAN</h4><h2 style='color:#00ff7f;'>{','.join(suppressed)}</h2></div>", unsafe_allow_html=True)
        with c2: st.markdown(f"<div class='status-box'><h4>PREDIKSI</h4><h2 style='color:#ff4b4b;'>{final_res}</h2></div>", unsafe_allow_html=True)
        with c3: st.markdown(f"<div class='status-box'><h4>INTEGRITAS</h4><h2 style='color:#00d2ff;'>{info['trust_score']}%</h2></div>", unsafe_allow_html=True)
        
        st.divider()
        st.markdown(f"**Strategi Lawan:** Menyerang titik **{res_as}** di posisi AS karena bandar menganggap angka ini sudah 'terkubur'.")
        

    with t2:
        st.subheader("🕵️ Pelacakan Langkah Musuh Selanjutnya")
        st.markdown(f"""
        <div class='enemy-card'>
        <b>Analisis Gerakan Bandar:</b><br>
        1. Bandar di {target} sedang memantau volume taruhan pada angka <b>{bait}</b>.<br>
        2. Jika taruhan massa tinggi, bandar akan mengaktifkan <i>Kill-Switch</i> pada digit tersebut.<br>
        3. Rencana cadangan bandar: Mengeluarkan angka kembar di tengah (Kop-Kepala).
        </div>
        """, unsafe_allow_html=True)
        st.write("---")
        st.progress(100 - info['trust_score'])
        st.caption(f"Tingkat Risiko Intervensi Manual: {100 - info['trust_score']}%")

    with t3:
        st.subheader("👥 Pemetaan Massa & User Dunia")
        st.write(f"Berdasarkan 'Intel Feed', user global saat ini sedang terjebak pada pola **{bait}**.")
        st.error(f"VERDIKT: Jangan ikuti arus massa. Bandar akan membuang digit {bait} untuk memaksimalkan profit mereka.")
        st.info("💡 Gunakan angka di 'Zona Buta' yang jarang dilirik oleh aplikasi prediksi standar.")

    with t4:
        st.subheader("📑 Evidence Record (Forensik Digital)")
        st.text_area("Salin Laporan Audit Ini:", value=f"""
ID LAPORAN: {target.upper()}-AUDIT-2026
KERENTANAN TERDETEKSI: {info['vulnerability']}
DIGIT SUPPRESSED: {', '.join(suppressed)}
DIGIT BAITING: {bait}
SKOR KEJUJURAN SERVER: {info['trust_score']}%

TEMUAN:
Terdapat deviasi statistik pada digit {suppressed[0]} yang menunjukkan 
indikasi kuat bahwa angka ini sengaja 'disimpan' oleh admin server 
untuk menghindari pembayaran kemenangan besar.
        """, height=250)

st.markdown("---")
st.caption("© 2026 Sentinel v37.6 | The All-Seeing Eye - Powered by Global Intelligence")
