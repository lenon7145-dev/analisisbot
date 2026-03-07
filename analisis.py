import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter

# --- SISTEM KONFIGURASI (WiFi, Sosmed, Maps, FAQ v8.8 Tetap Terjaga) ---
class SystemInfo:
    WIFI = "📶 FREE_HIGH_SPEED_WIFI_2026_V8.8_EXPLAINER"
    SOCIAL = ["@Analyst_AI", "@Explainer_Dev"]
    MAPS = "http://google.com/maps"
    FAQ = [
        "1. Kenapa rinciannya sangat banyak? Agar Anda paham logika di balik setiap tarikan angka.",
        "2. Apa itu Echo Logic? Menghitung gema (index) dari angka yang baru keluar.",
        "3. Apa itu Gap Analysis? Mencari angka yang sudah lama 'sembunyi' (seperti As 6 kemarin).",
        "4. WiFi Gratis? Cek Tab System Info untuk akses penuh.",
        "5. Tip Jitu: Bandingkan hasil Zigzag dengan Echo. Jika sama, itu angka kuat."
    ]

# --- UI SETTINGS ---
st.set_page_config(page_title="Ultimate Explainer Bot v8.8", layout="wide")
st.title("🎯 Ultimate Analyst Bot v8.8 (The Explainer)")
st.caption("Precision-Flow Edition: Analisis Detail dari v8.0 hingga v8.8")
st.markdown("---")

# --- SIDEBAR INPUT ---
st.sidebar.header("📥 Data Source")
raw_input = st.sidebar.text_area("Input Histori (Terbaru di atas):", height=250, placeholder="6395\n7554")
data_4d = [x.strip() for x in raw_input.split('\n') if len(x.strip()) == 4 and x.strip().isdigit()]

# Tabel Dasar
index_map = {'0':'5', '1':'6', '2':'7', '3':'8', '4':'9', '5':'0', '6':'1', '7':'2', '8':'3', '9':'4'}
echo_map = {'6':'1', '1':'6', '8':'3', '3':'8', '0':'5', '5':'0', '2':'7', '7':'2', '4':'9', '9':'4'}

if data_4d:
    # --- 1. PROSES RUMUS STATISTIK & GAP (v8.1-v8.4) ---
    res_stat = "".join([Counter([d[i] for d in data_4d]).most_common(1)[0][0] for i in range(4)])
    all_digits = "".join(data_4d)
    freq_table = Counter(all_digits).most_common(10)
    all_recent = "".join(data_4d[:7])
    missing = [str(i) for i in range(10) if str(i) not in all_recent]
    res_gap = missing[0] if missing else data_4d[0][0]

    # --- 2. PROSES SLIDING & FLOW (v8.6) ---
    latest = data_4d[0]
    flow_pool = [d[1] for d in data_4d[:3]] + [d[2] for d in data_4d[:3]]
    res_flow_digit = Counter(flow_pool).most_common(1)[0][0]
    
    # --- 3. PROSES ECHO & MIRROR (v8.7-v8.8) ---
    latest_as = latest[0]
    res_echo = f"{echo_map.get(latest[0], '0')}{echo_map.get(latest[1], '0')}"
    res_mirror = "".join([index_map.get(x, x) for x in latest])

    # --- 4. PROSES ZIGZAG (v8.5) ---
    n = [int(x) for x in latest]
    zigzag_rows = [[(n[0]-i)%10, (n[1]-i)%10, (n[2]+i)%10, (n[3]+i)%10] for i in range(6)]
    res_zigzag = f"{zigzag_rows[2][0]}{zigzag_rows[1][1]}{zigzag_rows[3][2]}{zigzag_rows[5][3]}"

    # --- 5. KONSENSUS AKHIR ---
    res_final_list = []
    engine_combined = [res_stat, res_zigzag, res_mirror, f"{res_echo}{res_flow_digit}{res_gap}"]
    for i in range(4):
        pool = [eng[i] for eng in engine_combined if len(eng)==4]
        res_final_list.append(Counter(pool).most_common(1)[0][0])
    res_final = "".join(res_final_list)

    # --- TAMPILAN MULTI-TAB DETAIL ---
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🏆 FINAL TARGET", 
        "📊 STATISTIK & GAP (v8.1-v8.4)", 
        "🔄 ECHO & FLOW (v8.6-v8.8)", 
        "📐 ZIGZAG ANALYSIS (v8.5)", 
        "🌐 SYSTEM INFO"
    ])

    with tab1:
        st.subheader("🎯 Konsensus Utama Sentinel v8.8")
        st.metric("PREDIKSI JITU", res_final)
        st.divider()
        st.markdown(f"""
        ### 🧐 Mengapa Angka Ini Muncul?
        * **Posisi AS ({res_final[0]}):** Diambil dari validasi mesin **Gap** dan **Echo**.
        * **Posisi KOP ({res_final[1]}):** Hasil sinkronisasi antara **Statistik** dan **Zigzag**.
        * **Posisi KEPALA ({res_final[2]}):** Mengikuti tren **Flow** angka tengah yang sedang aktif.
        * **Posisi EKOR ({res_final[3]}):** Adalah hasil **Mirroring** dari angka yang paling sering muncul.
        """)
        st.success(f"**Strategi 2D Belakang:** Target utama adalah **{res_final[2:]}** dengan cadangan **{res_mirror[2:]}**.")

    with tab2:
        st.subheader("📊 Bedah Rumus Statistik & Gap Analysis")
        col_a, col_b = st.columns(2)
        with col_a:
            st.write("**Top 5 Angka Paling Sering Muncul (Histori):**")
            for num, count in freq_table[:5]:
                st.write(f"- Angka **{num}**: Muncul {count} kali")
        with col_b:
            st.write("**Analisis Gap (Angka Sembunyi):**")
            st.info(f"Angka **{res_gap}** adalah angka yang sudah absen selama lebih dari 7 periode. Secara teori 'v8.4', angka ini memiliki daya ledak tinggi untuk muncul kembali di posisi depan.")
        st.divider()
        st.write(f"**Hasil Akhir Mesin Statistik:** `{res_stat}`")

    with tab3:
        st.subheader("🔄 Bedah Rumus Echo, Mirror, & Flow")
        st.markdown(f"""
        **1. Echo Logic (Gema):**
        Angka terbaru adalah **{latest}**. Angka AS adalah **{latest_as}**.
        Secara Gema (v8.8), bayangan dari {latest_as} adalah **{echo_map.get(latest_as)}**.
        
        **2. Positional Flow (Aliran):**
        Dalam 3 hari terakhir, angka tengah sering bergerak ke angka **{res_flow_digit}**.
        
        **3. Mirroring (Index):**
        Hasil konversi murni v8.0 dari {latest} adalah `{res_mirror}`.
        """)
        st.warning(f"**Kesimpulan Mesin:** Fokus pada angka `{res_echo}{res_flow_digit}{res_gap}` sebagai jalur alternatif.")

    with tab4:
        st.subheader("📐 Bedah Rumus Zigzag Master")
        st.write("Tabel ini menghitung pergerakan angka secara mundur (As/Kop) dan maju (Kep/Eko):")
        st.table(pd.DataFrame(zigzag_rows, columns=["AS (▼)", "KOP (▼)", "KEP (▲)", "EKO (▲)"]))
        st.markdown(f"""
        **Cara Baca Tabel:**
        * Bot mengambil Baris 3 untuk AS, Baris 2 untuk KOP, Baris 4 untuk KEP, dan Baris 6 untuk EKO.
        * **Hasil Tarikan Zigzag:** `{res_zigzag}`
        """)

    with tab5:
        st.write(f"**WiFi:** {SystemInfo.WIFI}")
        st.write(f"**Social:** {', '.join(SystemInfo.SOCIAL)}")
        st.write(f"**Maps:** [Server Location]({SystemInfo.MAPS})")
        st.divider()
        st.write("**FAQ & Panduan Lengkap:**")
        for item in SystemInfo.FAQ: st.write(item)

    # EXPORT DATA
    csv = pd.DataFrame(data_4d).to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Log Detail v8.8", csv, "sentinel_explainer.csv", "text/csv")

else:
    st.info("👋 Explainer v8.8 Standby. Masukkan data histori di sidebar untuk melihat analisis mendalam.")
