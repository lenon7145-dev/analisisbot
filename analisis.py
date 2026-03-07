import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter

# --- SISTEM KONFIGURASI (Audit: WiFi, Sosmed, Maps, FAQ v8.8 Terjaga) ---
class SystemInfo:
    WIFI = "📶 FREE_HIGH_SPEED_WIFI_2026_V8.8_PRO"
    SOCIAL = ["@Analyst_AI", "@Precision_Dev"]
    MAPS = "http://google.com/maps"
    FAQ = [
        "1. Kenapa ada banyak hasil? Agar Anda bisa membandingkan rumus mana yang paling jitu.",
        "2. Apa itu Echo Logic? Menghitung gema angka meledak (seperti gema As 6 jadi 1).",
        "3. Cara Baca Tab? Setiap tab mewakili evolusi rumus dari v8.0 sampai v8.8.",
        "4. WiFi Gratis? Cek Tab System Info untuk akses penuh.",
        "5. Tip: Jika 3 mesin mengeluarkan angka yang sama, itu adalah sinyal KUAT."
    ]

# --- UI SETTINGS ---
st.set_page_config(page_title="Ultimate Analyst Bot v8.8 PRO", layout="wide")
st.title("🎯 Ultimate Analyst Bot v8.8 (Full Transparency)")
st.caption("Precision-Flow Edition: Semua Rumus Ditampilkan Secara Detail")
st.markdown("---")

# --- SIDEBAR INPUT ---
st.sidebar.header("📥 Data Source")
raw_input = st.sidebar.text_area("Input Histori (Terbaru di atas):", height=250, placeholder="6395\n7554")
data_4d = [x.strip() for x in raw_input.split('\n') if len(x.strip()) == 4 and x.strip().isdigit()]

# Tabel Dasar (Mistik, Index, & Echo)
index_map = {'0':'5', '1':'6', '2':'7', '3':'8', '4':'9', '5':'0', '6':'1', '7':'2', '8':'3', '9':'4'}
echo_map = {'6':'1', '1':'6', '8':'3', '3':'8', '0':'5', '5':'0', '2':'7', '7':'2', '4':'9', '9':'4'}

if data_4d:
    # --- PROSES SEMUA RUMUS (DARI V8.0 - V8.8) ---
    
    # 1. RUMUS STATISTIK & GAP (v8.1 - v8.4)
    res_stat = "".join([Counter([d[i] for d in data_4d]).most_common(1)[0][0] for i in range(4)])
    all_recent = "".join(data_4d[:7])
    missing = [str(i) for i in range(10) if str(i) not in all_recent]
    res_gap = missing[0] if missing else data_4d[0][0]

    # 2. RUMUS SLIDING & FLOW (v8.6)
    flow_pool = [d[1] for d in data_4d[:3]] + [d[2] for d in data_4d[:3]]
    res_flow_digit = Counter(flow_pool).most_common(1)[0][0]
    res_sliding = data_4d[0][1:] + data_4d[1][0] # Contoh sliding sederhana

    # 3. RUMUS ECHO & MIRROR (v8.7 - v8.8)
    latest_as = data_4d[0][0]
    latest_kop = data_4d[0][1]
    res_echo = f"{echo_map.get(latest_as, '0')}{echo_map.get(latest_kop, '0')}"
    res_mirror = "".join([index_map.get(x, x) for x in data_4d[0]])

    # 4. RUMUS ZIGZAG (v8.5)
    n = [int(x) for x in data_4d[0]]
    zigzag_rows = [[(n[0]-i)%10, (n[1]-i)%10, (n[2]+i)%10, (n[3]+i)%10] for i in range(6)]
    res_zigzag = f"{zigzag_rows[2][0]}{zigzag_rows[1][1]}{zigzag_rows[3][2]}{zigzag_rows[5][3]}"

    # --- 5. KONSENSUS AKHIR ---
    res_final_list = []
    engine_combined = [res_stat, res_zigzag, res_mirror, f"{res_echo}{res_flow_digit}{res_gap}"]
    for i in range(4):
        pool = [eng[i] for eng in engine_combined if len(eng)==4]
        res_final_list.append(Counter(pool).most_common(1)[0][0])
    res_final = "".join(res_final_list)

    # --- TAMPILAN MULTI-TAB (Audit: Rincian Dimunculkan) ---
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🏆 FINAL TARGET", 
        "📊 STATISTIK & GAP", 
        "🔄 SLIDING & ECHO", 
        "📐 ZIGZAG LAB", 
        "🌐 SYSTEM INFO"
    ])

    with tab1:
        st.subheader("🎯 Konsensus Utama v8.8")
        st.metric("PREDIKSI JITU", res_final, delta="SENTINEL ACTIVE")
        st.write("---")
        st.write("### 🚀 Ringkasan Semua Mesin:")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Statistik", res_stat)
        col2.metric("Zigzag", res_zigzag)
        col3.metric("Mirror", res_mirror)
        col4.metric("Echo/Flow", f"{res_echo}{res_flow_digit}x")

    with tab2:
        st.subheader("📊 Analisis Statistik & Gap (v8.1-v8.4)")
        st.write(f"**Hasil Frekuensi Terbanyak:** `{res_stat}`")
        st.write(f"**Angka Hilang (Gap Analysis):** `{res_gap}`")
        st.info("Mesin ini yang berhasil menebak As 6 kemarin berdasarkan angka yang lama tidak muncul.")

    with tab3:
        st.subheader("🔄 Analisis Sliding, Flow & Echo (v8.6-v8.8)")
        st.write(f"**Gema (Echo) dari As/Kop:** `{res_echo}xx`")
        st.write(f"**Aliran (Flow) Angka Tengah:** `{res_flow_digit}`")
        st.write(f"**Konversi Mirror (v8.0):** `{res_mirror}`")
        st.success(f"Analisis: Angka {res_echo[:1]} adalah bayangan kuat dari {latest_as}.")

    with tab4:
        st.subheader("📐 Tabel Zigzag Precision (v8.5)")
        st.table(pd.DataFrame(zigzag_rows, columns=["AS", "KOP", "KEP", "EKO"]))
        st.write(f"**Hasil Tarikan Jalur:** `{res_zigzag}`")

    with tab5:
        st.write(f"**WiFi:** {SystemInfo.WIFI}")
        st.write(f"**Social:** {', '.join(SystemInfo.SOCIAL)}")
        st.write(f"**Maps:** [Server Location]({SystemInfo.MAPS})")
        st.divider()
        st.write("**FAQ & Dokumentasi:**")
        for item in SystemInfo.FAQ: st.write(item)

    # EXPORT DATA
    csv = pd.DataFrame(data_4d).to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Log Analisis", csv, "sentinel_v88.csv", "text/csv")

else:
    st.info("👋 Sentinel v8.8 Standby. Masukkan data histori di sidebar untuk melihat semua rincian rumus.")
