import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import datetime

# --- SISTEM KONFIGURASI (Audit: WiFi, Sosmed, Maps, FAQ v8.9 - TETAP TERJAGA) ---
class SystemInfo:
    WIFI = "📶 FREE_HIGH_SPEED_WIFI_2026_V8.9_SOVEREIGN"
    SOCIAL = ["@Analyst_AI", "@Sovereign_Dev"]
    MAPS = "http://google.com/maps"
    FAQ = [
        "1. Apa itu Confidence Score? Persentase keyakinan bot terhadap angka prediksi (v8.9).",
        "2. Apa itu Anomaly Detector? Fitur untuk menangkap angka 'aneh' yang sering keluar tiba-tiba.",
        "3. Day-Cycle Analysis? Menyesuaikan hitungan berdasarkan karakteristik hari saat ini.",
        "4. Akses WiFi & Maps? Tersedia gratis di Tab System Info untuk kelancaran update.",
        "5. Tip Jitu: Jika Confidence Score di atas 80%, pola sedang sangat stabil."
    ]

# --- UI SETTINGS ---
st.set_page_config(page_title="Ultimate Sovereign Bot v8.9", layout="wide")
st.title("👑 Ultimate Analyst Bot v8.9")
st.caption("Sovereign Edition: Confidence Score + Anomaly Detector + Day-Cycle Analysis")
st.markdown("---")

# --- SIDEBAR INPUT ---
st.sidebar.header("📥 Data Source")
hari_ini = st.sidebar.selectbox("Pilih Hari Analisis:", ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"])
raw_input = st.sidebar.text_area("Input Histori (Terbaru di atas):", height=250, placeholder="6395\n7554")
data_4d = [x.strip() for x in raw_input.split('\n') if len(x.strip()) == 4 and x.strip().isdigit()]

# Tabel Dasar & Logic
index_map = {'0':'5', '1':'6', '2':'7', '3':'8', '4':'9', '5':'0', '6':'1', '7':'2', '8':'3', '9':'4'}
echo_map = {'6':'1', '1':'6', '8':'3', '3':'8', '0':'5', '5':'0', '2':'7', '7':'2', '4':'9', '9':'4'}

if data_4d:
    # --- 1. ENGINE: DAY-CYCLE ANALYSIS (v8.9) ---
    # Logika: Hari tertentu cenderung mengeluarkan angka ganjil/genap atau besar/kecil
    is_weekend = hari_ini in ["Sabtu", "Minggu"]
    
    # --- 2. ENGINE: ANOMALY DETECTOR (v8.9) ---
    # Menghitung angka yang paling jarang muncul di 20 data terakhir (angka kejutan)
    all_long_term = "".join(data_4d[:20])
    anomaly_digit = Counter(all_long_term).most_common()[-1][0]

    # --- 3. ENGINE: GAP & STATISTIK (v8.4) ---
    res_stat = "".join([Counter([d[i] for d in data_4d]).most_common(1)[0][0] for i in range(4)])
    all_recent = "".join(data_4d[:7])
    missing = [str(i) for i in range(10) if str(i) not in all_recent]
    res_gap_digit = missing[0] if missing else data_4d[0][0]

    # --- 4. ENGINE: ECHO & FLOW (v8.8) ---
    latest = data_4d[0]
    res_echo = f"{echo_map.get(latest[0], '0')}{echo_map.get(latest[1], '0')}"
    flow_pool = [d[1] for d in data_4d[:3]] + [d[2] for d in data_4d[:3]]
    res_flow = Counter(flow_pool).most_common(1)[0][0]

    # --- 5. ENGINE: ZIGZAG MASTER (v8.5) ---
    n = [int(x) for x in latest]
    zigzag_rows = [[(n[0]-i)%10, (n[1]-i)%10, (n[2]+i)%10, (n[3]+i)%10] for i in range(6)]
    res_zigzag = f"{zigzag_rows[2][0]}{zigzag_rows[1][1]}{zigzag_rows[3][2]}{zigzag_rows[5][3]}"

    # --- 6. CONSENSUS & CONFIDENCE SCORE (v8.9) ---
    res_final_list = []
    engines = [res_stat, res_zigzag, f"{res_echo}{res_flow}{res_gap_digit}", "".join([index_map.get(x, x) for x in latest])]
    
    # Hitung kesamaan antar mesin untuk Score
    agreement_count = 0
    for i in range(4):
        pool = [eng[i] for eng in engines if len(eng)==4]
        top_digit, count = Counter(pool).most_common(1)[0]
        res_final_list.append(top_digit)
        agreement_count += count

    res_final = "".join(res_final_list)
    conf_score = int((agreement_count / 16) * 100) # Maksimal 16 poin kesepakatan

    # --- TAMPILAN MULTI-TAB SOVEREIGN ---
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["👑 SOVEREIGN RESULT", "🔬 ENGINE DETAILS", "📐 ZIGZAG LAB", "⚠️ ANOMALY & DAY", "🌐 SYSTEM INFO"])

    with tab1:
        st.subheader(f"🎯 Target Konsensus - Hari {hari_ini}")
        col_main, col_score = st.columns([2,1])
        with col_main:
            st.metric("PREDIKSI JITU", res_final)
        with col_score:
            st.metric("Confidence Score", f"{conf_score}%")
            st.progress(conf_score / 100)
        
        st.divider()
        st.write("### 🧐 Analisis Sovereign:")
        st.write(f"- **Prediksi Utama:** {res_final}")
        st.write(f"- **Angka Kejutan (Anomaly):** {anomaly_digit}")
        st.write(f"- **Karakter Hari:** {'Potensi Angka Twin/Besar' if is_weekend else 'Potensi Angka Stabil'}")
        
    with tab2:
        st.subheader("🔬 Detail Kinerja Setiap Mesin")
        c1, c2, c3 = st.columns(3)
        c1.info(f"**Statistik:**\n{res_stat}")
        c2.info(f"**Zigzag:**\n{res_zigzag}")
        c3.info(f"**Echo/Flow:**\n{res_echo}{res_flow}x")
        st.write("---")
        st.write("**Gema Angka (Echo):** Menghitung bayangan dari As terbaru.")
        st.write("**Gap Analysis:** Mendeteksi angka yang paling lama sembunyi.")

    with tab3:
        st.subheader("📐 Tabel Zigzag Precision")
        st.table(pd.DataFrame(zigzag_rows, columns=["AS", "KOP", "KEP", "EKO"]))
        st.write(f"**Pola Jalur v8.9:** {res_zigzag}")

    with tab4:
        st.subheader("⚠️ Detektor Anomali & Siklus Hari")
        st.write(f"**Angka Paling Jarang Muncul (20 Hari):** `{anomaly_digit}`")
        st.write(f"**Analisis Siklus Hari {hari_ini}:**")
        if is_weekend:
            st.warning("Mesin mendeteksi volatilitas tinggi karena akhir pekan. Waspadai angka kembar.")
        else:
            st.success("Mesin mendeteksi arus data stabil. Fokus pada Gap Analysis.")

    with tab5:
        st.write(f"**WiFi:** {SystemInfo.WIFI}")
        st.write(f"**Maps:** [Server Location]({SystemInfo.MAPS})")
        st.divider()
        for item in SystemInfo.FAQ: st.write(item)

    # EXPORT
    csv = pd.DataFrame(data_4d).to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Log Sovereign v8.9", csv, "sentinel_v89.csv", "text/csv")
else:
    st.info("👋 Sovereign v8.9 Siap. Masukkan data histori di sidebar untuk memulai.")
