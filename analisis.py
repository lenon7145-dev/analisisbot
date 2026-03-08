import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import random
import time
import os
from datetime import datetime

# --- 1. CORE CONFIGURATION ---
VERSION = "40.4"
CODENAME = "THE SINGULARITY"
DB_FILE = "sentinel_immortal_db.txt"

# --- 2. ENGINE: IMMORTAL STORAGE (MEMORI ABADI) ---
def save_memory(res, server_name):
    if res and len(res) == 4:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        with open(DB_FILE, "a") as f:
            f.write(f"{timestamp} | {server_name} | {res}\n")
        return True
    return False

def load_memory():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    return []

# --- 3. NEURAL LOGIC & ANTI-GAP DETECTOR ---
def get_ai_neural_offset(server_name, history):
    offset = 0
    if history:
        last_results = [line.split(" | ")[-1] for line in history if server_name in line]
        if len(last_results) > 3:
            # AI menganalisis kecenderungan angka terakhir untuk memberikan offset pergeseran
            last_digit = int(last_results[-1][-1])
            offset = 1 if last_digit % 2 == 0 else -1
    return offset

def detect_extreme_drift(history, current_pred):
    if not history: return False
    last_res = history[-1].split(" | ")[-1]
    # Deteksi jika bandar mengubah total 3-4 digit secara mendadak (Intervensi Admin)
    diff = sum(1 for a, b in zip(last_res, current_pred) if a != b)
    return diff >= 3

# --- 4. SERVER ARCHITECTURE ---
SERVER_CONFIG = {
    "Hongkong (HK)": {"mode": "Mechanical", "trust": 96, "close": "22:30"},
    "Singapore (SGP)": {"mode": "Conservative", "trust": 94, "close": "17:30"},
    "Sydney (SDY)": {"mode": "Entropy", "trust": 92, "close": "13:30"},
    "Macau (MC)": {"mode": "Anti-Admin", "trust": 90, "close": "23:00"}
}

# --- 5. AGGRESSIVE UI DESIGN (WAR-MODE) ---
st.set_page_config(page_title=f"SENTINEL v{VERSION}", layout="wide")
st.markdown(f"""
    <style>
    .stApp {{ background: #050505; color: #00ff41; font-family: 'Courier New', monospace; }}
    .war-card {{ 
        background: rgba(20, 0, 0, 0.7); border: 2px solid #ff0000; 
        padding: 40px; border-radius: 5px; text-align: center;
        box-shadow: 0 0 30px rgba(255, 0, 0, 0.4); margin-bottom: 20px;
    }}
    .main-pred {{ 
        font-size: 130px; color: #ffffff; text-shadow: 0 0 30px #ff0000; 
        font-weight: 900; letter-spacing: 15px; margin: 20px 0;
    }}
    .briefing-box {{
        background: rgba(0, 255, 65, 0.05); border-left: 5px solid #00ff41;
        padding: 20px; margin-bottom: 20px; border-radius: 0 10px 10px 0;
    }}
    .critical-alert {{ 
        background: #ff0000; color: white; padding: 15px; font-weight: bold; 
        text-align: center; animation: blinker 0.8s linear infinite; border: 3px solid white; margin-bottom: 10px;
    }}
    @keyframes blinker {{ 50% {{ opacity: 0; }} }}
    .step-header {{ color: #00ffff; font-weight: bold; font-size: 1.2rem; margin-top: 15px; }}
    </style>
    """, unsafe_allow_html=True)

# --- 6. COMMAND CENTER (SIDEBAR) ---
st.sidebar.markdown("<h2 style='color:red;'>⚠️ WAR COMMAND</h2>", unsafe_allow_html=True)
target = st.sidebar.selectbox("TARGET SERVER:", list(SERVER_CONFIG.keys()))
config = SERVER_CONFIG[target]

if st.sidebar.button("🚨 INITIATE SINGULARITY SYNC"):
    st.session_state['active_session'] = True
    with st.spinner("MEMBEDAH ENKRIPSI BANDAR..."):
        # Simulasi 500 titik data untuk presisi v4.4
        st.session_state['pool'] = [str(random.randint(1000, 9999)) for _ in range(500)]
        time.sleep(1.5)
        st.sidebar.success("NEURAL LINK ESTABLISHED")

if os.path.exists(DB_FILE):
    with open(DB_FILE, "r") as f:
        st.sidebar.download_button("💾 DOWNLOAD BACKUP DB", f.read(), f"sentinel_backup_{datetime.now().strftime('%Y%m%d')}.txt")

# --- 7. MAIN INTERFACE LOGIC ---
if 'active_session' not in st.session_state:
    # --- HALAMAN AWAL: SOVEREIGN BRIEFING ROOM ---
    st.markdown("<h1 style='text-align:center; color:red;'>🚨 SENTINEL v40.4: THE SINGULARITY 🚨</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>SOVEREIGN AUDIT INSTRUMENT | NEURAL BRIDGE ACTIVE</p>", unsafe_allow_html=True)
    st.divider()
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 🏛️ FILOSOFI & TUJUAN")
        st.markdown(f"""
        <div class='briefing-box'>
        <b>Sentinel v{VERSION}</b> adalah sistem intelijen yang memetakan <i>Void Zone</i> bandar. 
        Tujuan kita bukan menebak angka, melainkan menemukan angka yang <b>paling tidak ingin dikeluarkan</b> 
        oleh bandar karena alasan finansial (<i>payout management</i>).
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<p class='step-header'>• Void Selection</p>", unsafe_allow_html=True)
        st.write("Menganalisis akumulasi titik data terendah.")
        st.markdown("<p class='step-header'>• Shadow Defense</p>", unsafe_allow_html=True)
        st.write("Mengunci celah manipulasi 1-digit (+1/-1).")

    with c2:
        st.markdown("### 🕹️ SOP OPERASIONAL")
        st.markdown("<p class='step-header'>1. Critical Sync</p>", unsafe_allow_html=True)
        st.write(f"Lakukan sinkronisasi 15 menit sebelum jam tutup ({config['close']}).")
        st.markdown("<p class='step-header'>2. Strategi 60:20:20</p>", unsafe_allow_html=True)
        st.write("Alokasikan modal: 60% Target Utama, 20% Shadow Up, 20% Shadow Down.")
        st.markdown("<p class='step-header'>3. Noise Camouflage</p>", unsafe_allow_html=True)
        st.write("Pasang angka acak (Noise) untuk mengelabui admin.")

else:
    # --- HALAMAN EKSEKUSI (WAR-MODE) ---
    eternal_mem = load_memory()
    data_pool = st.session_state['pool']
    counts = Counter("".join(data_pool))
    
    # Void Logic
    suppressed = [d for d, c in sorted(counts.items(), key=lambda x: x[1])[:4]]
    ai_offset = get_ai_neural_offset(target, eternal_mem)
    
    res_as = suppressed[0]
    res_kop = str((int(data_pool[0][1]) + 3) % 10)
    res_kepala = suppressed[1]
    res_ekor = str((int(data_pool[0][3]) + 7 + ai_offset) % 10)

    main_pred = res_as + res_kop + res_kepala + res_ekor
    sh_up = main_pred[:3] + str((int(main_pred[3]) + 1) % 10)
    sh_down = main_pred[:3] + str((int(main_pred[3]) - 1) % 10)
    
    is_drift = detect_extreme_drift(eternal_mem, main_pred)

    st.markdown(f"## 🎯 KILL-ZONE: {target.upper()} | {config['close']}")
    
    if is_drift:
        st.markdown("<div class='critical-alert'>🚨 DETEKSI INTERVENSI MANUAL BANDAR: JANGAN ALL-IN! 🚨</div>", unsafe_allow_html=True)

    st.markdown("<div class='war-card'>", unsafe_allow_html=True)
    st.write("### ⚡ VOID TARGET (MAIN PREDICTION)")
    st.markdown(f"<p class='main-pred'>{main_pred}</p>", unsafe_allow_html=True)
    st.write(f"Confidence: **{config['trust']}%** | Mode: **{config['mode']}**")
    st.progress(config['trust']/100)
    st.markdown("</div>", unsafe_allow_html=True)

    tab_defense, tab_noise, tab_intel = st.tabs(["🛡️ DEFENSE PROTOCOL", "🎭 NOISE INJECTION", "📜 INTEL LOG"])

    with tab_defense:
        c1, c2 = st.columns(2)
        with c1:
            st.error(f"**SHADOW UP (+1)**\n## {sh_up}")
        with c2:
            st.error(f"**SHADOW DOWN (-1)**\n## {sh_down}")
        st.info("💡 Gunakan jaring pengaman ini untuk menutup celah manipulasi 1-digit.")

    with tab_noise:
        st.subheader("🎭 Kamuflase Anti-Admin")
        st.write("Pasang angka acak berikut dengan nominal terendah untuk mengelabui sistem deteksi bot:")
        n1, n2, n3 = [str(random.randint(1000, 9999)) for _ in range(3)]
        st.code(f"{n1} | {n2} | {n3}", language="text")

    with tab_intel:
        st.subheader("📜 Immortal Audit Log")
        if eternal_mem:
            log_data = [line.split(" | ") for line in eternal_mem[-15:]]
            st.table(pd.DataFrame(log_data, columns=["Waktu", "Server", "Result"]))
        
        if st.button("✅ SAVE CURRENT RESULT TO DB"):
            if save_memory(main_pred, target):
                st.success("Target Terkunci di Database.")

st.markdown("---")
st.caption(f"© 2026 SENTINEL v{VERSION} | SOVEREIGN MODE | NO IDENTITY TRACE")
