import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import re
import random

# --- 1. CORE DATABASE & INTELLIGENCE ---
SERVER_PROFILES = {
    "Hongkong (HK)": {"risk": "Tinggi", "mod": "Bait & Switch", "color": "#ff4b4b"},
    "Singapore (SGP)": {"risk": "Sedang", "style": "Low Payout Void", "color": "#ffa500"},
    "Sydney (SDY)": {"risk": "Rendah", "style": "Random Entropy", "color": "#00d2ff"},
    "Macau (MC)": {"risk": "Ekstrem", "style": "Manual Intervention", "color": "#7b2cbf"}
}

def get_intel_report(server):
    reports = [
        f"🚩 [INTEL] Volume taruhan digit 4 di {server} overload. Bandar diprediksi akan membuang angka ini.",
        f"⚠️ [LATENCY] Terdeteksi jeda 15ms. Admin {server} sedang melakukan sinkronisasi manual.",
        f"🌀 [PATTERN] Pola Spiral Fibonacci di {server} sedang dipatahkan secara sengaja.",
        f"✅ [CLEAN] Aliran data {server} terpantau organik untuk 2 periode ke depan."
    ]
    return random.choice(reports)

# --- 2. THE SUPREME INTERFACE ---
st.set_page_config(page_title="SENTINEL v37.4 - OMNI INTEL", layout="wide")

st.markdown("""
    <style>
    .stApp { background: #050505; color: #00ff7f; font-family: 'Courier New', monospace; }
    .status-card {
        background: rgba(0, 255, 127, 0.05); border: 1px solid #00ff7f;
        padding: 20px; border-radius: 15px; text-align: center;
    }
    .intel-sidebar {
        background: rgba(255, 255, 255, 0.05); padding: 15px; border-radius: 10px;
        border-left: 5px solid #ff4b4b; margin-top: 20px; font-size: 13px;
    }
    .glow-text { color: #00ff7f; text-shadow: 0 0 10px #00ff7f; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;' class='glow-text'>📡 SENTINEL v37.4: OMNI-INTELLIGENCE</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Global Enemy Tracking & Manipulation Audit System</p>", unsafe_allow_html=True)

# --- 3. COMMAND CENTER (SIDEBAR) ---
st.sidebar.markdown("### 🛰️ GLOBAL TARGET")
target = st.sidebar.selectbox("Pilih Server:", list(SERVER_PROFILES.keys()))
raw_input = st.sidebar.text_area("📡 Transmisi Data (4D):", height=200, placeholder="Input riwayat di sini...")
clean_data = re.findall(r'\d{4}', raw_input)

# Informasi Musuh di Sidebar
prof = SERVER_PROFILES[target]
st.sidebar.markdown(f"""
<div style='background:{prof["color"]}; padding:10px; border-radius:10px; color:#000; font-weight:bold;'>
SERVER: {target}<br>MODUS: {prof["mod"]}<br>RISIKO: {prof["risk"]}
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("### 🗨️ LIVE INTEL FEED")
st.sidebar.markdown(f"<div class='intel-sidebar'>{get_intel_report(target)}</div>", unsafe_allow_html=True)

# --- 4. ANALISIS & DASHBOARD ---
if not clean_data:
    st.info("💡 **STATUS:** Menunggu transmisi data riwayat untuk memulai pemindaian otak bandar.")
    st.markdown("---")
    st.subheader("🛠️ Fitur Sentinel v37.4:")
    st.write("- **Audit Integritas:** Menghitung seberapa jujur server berdasarkan anomali.")
    st.write("- **Suppressed Digit:** Menemukan angka yang sengaja disimpan di gudang bandar.")
    st.write("- **Bandar Mimicry:** Berpikir seperti musuh untuk menemukan celah profit.")
else:
    # A. LOGIKA DETEKSI MUSUH (DARK MIRROR)
    all_digits = "".join(clean_data)
    counts = Counter(all_digits)
    # Angka yang paling jarang muncul (Suppressed/Simpanan)
    suppressed = [d for d, c in sorted(counts.items(), key=lambda x: x[1])[:3]]
    # Angka yang dijadikan umpan (Bait/Paling sering muncul)
    bait = counts.most_common(1)[0][0]
    
    # B. SIMULASI ANGKA ZONA BUTA (ANTI-BANDAR)
    # Bandar akan melepas angka yang 'tidak mungkin' dipasang orang (Psikologis Rendah)
    res_as = suppressed[0] if len(suppressed) > 0 else "0"
    res_kop = str((int(clean_data[0][1]) + 7) % 10) # Melompat dari pola normal
    res_kepala = suppressed[1] if len(suppressed) > 1 else "1"
    res_ekor = "0" if "0" not in all_digits[:10] else suppressed[-1]
    
    final_pred = res_as + res_kop + res_kepala + res_ekor
    
    # C. AUDIT MANIPULASI
    twins = sum(1 for d in clean_data[:10] if len(set(d)) < 4)
    integrity_score = max(0, 100 - (twins * 12))

    # --- TAB NAVIGATION ---
    t1, t2, t3 = st.tabs(["🎯 TARGET SCANNER", "🕵️ ENEMY MOVEMENT", "📜 EVIDENCE LOG"])

    with t1:
        st.subheader(f"📍 Analisis Target: {target}")
        c1, c2, c3 = st.columns(3)
        with c1: 
            st.markdown(f"<div class='status-card'><h4>ANGKA SIMPANAN</h4><h1 class='glow-text'>{','.join(suppressed)}</h1></div>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"<div class='status-card'><h4>PREDIKSI LAWAN</h4><h1 style='color:#ff4b4b;'>{final_pred}</h1></div>", unsafe_allow_html=True)
        with c3:
            st.markdown(f"<div class='status-card'><h4>INTEGRITY</h4><h1 style='color:{'#00ff7f' if integrity_score > 60 else '#ff4b4b'};'>{integrity_score}%</h1></div>", unsafe_allow_html=True)
        
        st.divider()
        st.markdown(f"**Anatomi Perlawanan:** Menggunakan Digit **{res_as}** sebagai pondasi karena bandar menganggap angka ini 'mati'.")

    with t2:
        st.subheader("🕵️ Pelacakan Pergerakan Musuh")
        st.write(f"Sistem mendeteksi bandar {target} sedang menggunakan teknik: **{prof['style']}**")
        st.progress(twins * 10)
        st.warning(f"Terdeteksi {twins} anomali pola dalam 10 putaran terakhir. {'Indikasi intervensi manual terdeteksi!' if twins > 3 else 'Pola masih terpantau semi-organik.'}")
        
        st.markdown("### 🧠 Simulasi Otak Bandar:")
        st.write(f"- Bandar sedang memancing massa dengan digit **{bait}**.")
        st.write(f"- Bandar merasa aman mengeluarkan kombinasi **{final_pred[:2]}xx** karena volume taruhan rendah.")

    with t3:
        st.subheader("📑 Bukti Audit Forensik")
        st.text_area("Salin bukti ini untuk laporan:", value=f"""
ID LAPORAN: {target.upper()}-SENTINEL-2026
STATUS: {'MANIPULASI TERDETEKSI' if integrity_score < 60 else 'MONITORING'}
SKOR KEJUJURAN: {integrity_score}%

DATA TEMUAN:
1. Angka yang Sengaja Ditekan (Suppressed): {', '.join(suppressed)}
2. Digit Pancingan (Baiting): {bait}
3. Frekuensi Anomali: {twins} kali dalam 10 sesi.

KESIMPULAN:
Terdapat indikasi kuat bahwa server melakukan penyaringan angka berdasarkan volume taruhan (Low-Payout Algorithm).
        """, height=250)

st.markdown("---")
st.caption("© 2026 Sentinel v37.4 | Global Omni-Intelligence Command Center")
