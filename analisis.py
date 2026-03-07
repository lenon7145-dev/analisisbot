import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter

# --- SISTEM KONFIGURASI (Audit: WiFi, Sosmed, Maps, FAQ Terjaga) ---
class SystemInfo:
    WIFI = "📶 FREE_HIGH_SPEED_WIFI_2026_V8.8"
    SOCIAL = ["@Analyst_AI", "@Precision_Dev"]
    MAPS = "http://google.com/maps"
    FAQ = [
        "1. Apa itu Echo Logic? Menghitung 'gema' angka yang baru meledak (seperti gema dari As 6).",
        "2. Apa itu Positional Flow? Melacak perpindahan angka dari posisi Kop/Kepala ke Ekor.",
        "3. Cara Pakai v8.8? Masukkan 6395 di baris teratas untuk mengaktifkan sensor gema.",
        "4. Dimana Lokasi Server? Cek Tab System Info untuk Maps dan akses WiFi gratis.",
        "5. Tip Jitu: Jika angka Echo muncul di hasil Zigzag, itu adalah angka BOOM."
    ]

# --- UI SETTINGS ---
st.set_page_config(page_title="Ultimate Analyst Bot v8.8", layout="centered")
st.title("🎯 Ultimate Analyst Bot v8.8")
st.caption("Precision-Flow Edition: Echo Logic + Gap Refinement + Flow Analysis")
st.markdown("---")

# --- SIDEBAR INPUT ---
st.sidebar.header("📥 Data Source")
raw_input = st.sidebar.text_area("Input Histori (6395 di atas):", height=250, placeholder="6395\n7554")
data_4d = [x.strip() for x in raw_input.split('\n') if len(x.strip()) == 4 and x.strip().isdigit()]

# Tabel Dasar (Mistik, Index, & Echo)
index_map = {'0':'5', '1':'6', '2':'7', '3':'8', '4':'9', '5':'0', '6':'1', '7':'2', '8':'3', '9':'4'}
echo_map = {'6':'1', '1':'6', '8':'3', '3':'8', '0':'5', '5':'0', '2':'7', '7':'2', '4':'9', '9':'4'}

if data_4d:
    # --- 1. ENGINE: ECHO LOGIC ---
    latest_as = data_4d[0][0]
    latest_kop = data_4d[0][1]
    res_echo = f"{echo_map.get(latest_as, '0')}{echo_map.get(latest_kop, '0')}"

    # --- 2. ENGINE: POSITIONAL FLOW ---
    flow_pool = [d[1] for d in data_4d[:3]] + [d[2] for d in data_4d[:3]]
    res_flow = Counter(flow_pool).most_common(1)[0][0]

    # --- 3. ENGINE: GAP ANALYSIS REFINED ---
    all_recent = "".join(data_4d[:7])
    missing = [str(i) for i in range(10) if str(i) not in all_recent]
    res_gap_digit = missing[0] if missing else data_4d[0][0]

    # --- 4. ENGINE: ZIGZAG MASTER v8.8 ---
    n = [int(x) for x in data_4d[0]]
    zigzag_rows = [[(n[0]-i)%10, (n[1]-i)%10, (n[2]+i)%10, (n[3]+i)%10] for i in range(6)]
    res_zigzag = f"{zigzag_rows[2][0]}{zigzag_rows[1][1]}{zigzag_rows[3][2]}{zigzag_rows[5][3]}"

    # --- 5. PRECISION CONSENSUS ---
    res_final_list = []
    # Menggabungkan Echo, Flow, dan Zigzag
    engine_str = f"{res_echo}{res_flow}{res_gap_digit}"
    engines = [res_zigzag, engine_str, "".join([index_map.get(x, x) for x in data_4d[0]])]
    
    for i in range(4):
        pool = [eng[i] for eng in engines if len(eng)==4]
        if not pool:
            res_final_list.append(data_4d[0][i])
        else:
            res_final_list.append(Counter(pool).most_common(1)[0][0])
    
    res_final = "".join(res_final_list)

    # --- TAMPILAN UTAMA ---
    tab1, tab2, tab3, tab4 = st.tabs(["🎯 Precision Result", "🔬 Flow Analysis", "📐 Zigzag Lab", "🌐 System Info"])

    with tab1:
        st.subheader("🏆 Konsensus Precision v8.8")
        st.metric("PREDIKSI TARGET", res_final)
        
        st.divider()
        st.write("### 🔎 Indikator Mesin")
        c1, c2, c3 = st.columns(3)
        with c1: st.info(f"**Echo (Gema):**\n{res_echo}xx")
        with c2: st.info(f"**Gap Digit:**\n{res_gap_digit}")
        with c3: st.info(f"**Zigzag:**\n{res_zigzag}")

        st.write("### 🔔 Notifikasi Strategi")
        st.code(f"PRECISION v8.8 READY\nTarget: {res_final}\nStatus Gema: AKTIF dari As {latest_as}", language="text")

    with tab2:
        st.subheader("🔬 Laboratorium Gema & Aliran")
        st.write(f"- **Gema Angka Terbaru:** {res_echo} (Potensi Index/Mirror)")
        st.write(f"- **Flow Angka Tengah:** {res_flow} (Kecenderungan turun posisi)")
        st.info(f"Insight: Kasus 6395 membuktikan As 6 meledak dari Gap. v8.8 memantau 'Gema' angka 6 yaitu 1.")

    with tab3:
        st.subheader("📐 Tabel Zigzag Precision")
        st.table(pd.DataFrame(zigzag_rows, columns=["AS", "KOP", "KEP", "EKO"]))
        st.write(f"**Pola Jalur v8.8:** {res_zigzag}")

    with tab4:
        st.write(f"**WiFi:** {SystemInfo.WIFI}")
        st.write(f"**Maps:** [Server Location]({SystemInfo.MAPS})")
        st.divider()
        st.write("**FAQ Precision-Flow:**")
        for item in SystemInfo.FAQ: st.write(item)

    # EXPORT
    csv = pd.DataFrame(data_4d).to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Log v8.8", csv, "analisis_precision.csv", "text/csv")
else:
    st.info("👋 Precision v8.8 Siap. Masukkan histori 6395 untuk memulai analisis Gema.")
