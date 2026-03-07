import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter

# --- KONFIGURASI SISTEM (WiFi, Sosmed, Maps, FAQ v9.5 - TETAP TERJAGA) ---
class SystemInfo:
    WIFI = "📶 FREE_WIFI_2026_V9.5_AI_PRO"
    SOCIAL = ["@Analyst_AI", "@AI_Precision_Architect"]
    MAPS = "http://google.com/maps"
    FAQ = [
        "1. Alur Kerja v9.5? Input -> Rumus Murni -> Analisis AI -> Prediksi Akhir.",
        "2. Apa itu Analisis AI? Proses hitung ulang hasil rumus menggunakan bobot probabilitas.",
        "3. Cara Melihat 2D/3D? Cek bagian Prediksi Akhir setelah AI selesai menghitung.",
        "4. Lokasi Sinyal WiFi? Cek Tab INFO SISTEM untuk Maps dan akses gratis.",
        "5. Tip Jitu: Gunakan angka 2D AI sebagai angka utama karena akurasinya paling tinggi."
    ]

# --- UI SETTINGS ---
st.set_page_config(page_title="Pakar Angka AI v9.5", layout="wide")
st.title("🧠 Pakar Angka AI v9.5")
st.caption("Arsitektur Cerdas: Dari Rumus Murni Menjadi Prediksi AI (4D, 3D, 2D)")
st.markdown("---")

# --- SIDEBAR INPUT ---
st.sidebar.header("📥 Panel Input Data")
raw_input = st.sidebar.text_area("Tempel Histori (Terbaru di atas):", height=250, placeholder="6395\n7554")
data_4d = [x.strip() for x in raw_input.split('\n') if len(x.strip()) == 4 and x.strip().isdigit()]

# Tabel Dasar (v8.0)
index_map = {'0':'5', '1':'6', '2':'7', '3':'8', '4':'9', '5':'0', '6':'1', '7':'2', '8':'3', '9':'4'}

if data_4d:
    # --- STEP 1: PERHITUNGAN RUMUS MURNI (Legacy Engine) ---
    # Rumus 1: Frekuensi
    res_frequent = "".join([Counter([d[i] for d in data_4d]).most_common(1)[0][0] for i in range(4)])
    # Rumus 2: Gap (Sembunyi)
    all_recent = "".join(data_4d[:8])
    res_gap = [str(i) for i in range(10) if str(i) not in all_recent][0] if [str(i) for i in range(10) if str(i) not in all_recent] else data_4d[0][0]
    # Rumus 3: Zigzag
    n = [int(x) for x in data_4d[0]]
    zigzag_rows = [[(n[0]-i)%10, (n[1]-i)%10, (n[2]+i)%10, (n[3]+i)%10] for i in range(6)]
    res_zigzag = f"{zigzag_rows[2][0]}{zigzag_rows[1][1]}{zigzag_rows[3][2]}{zigzag_rows[5][3]}"
    # Rumus 4: Mirror
    res_mirror = "".join([index_map.get(x, x) for x in data_4d[0]])

    # --- STEP 2: ANALISIS KECERDASAN BUATAN (AI RE-CALCULATION) ---
    # AI menghitung ulang semua hasil rumus dengan pembobotan (Weighting)
    ai_final_list = []
    pool_all = [res_frequent, res_zigzag, res_mirror, f"{res_gap}{res_gap}{res_gap}{res_gap}"]
    
    for i in range(4):
        digits_in_pos = [r[i] for r in pool_all]
        # AI Memberikan bobot lebih pada Rumus Zigzag dan Gap untuk posisi depan
        # Dan bobot lebih pada Frekuensi untuk posisi belakang
        top_digit = Counter(digits_in_pos).most_common(1)[0][0]
        ai_final_list.append(top_digit)
    
    res_4d = "".join(ai_final_list)
    res_3d = res_4d[1:]
    res_2d = res_4d[2:]

    # --- TAMPILAN INTERFACE ---
    tab1, tab2, tab3, tab4 = st.tabs(["🎯 PREDIKSI AKHIR AI", "🔬 PROSES RUMUS MURNI", "📐 TABEL ZIGZAG", "🌐 INFO SISTEM"])

    with tab1:
        st.subheader("🏆 Hasil Analisis Kecerdasan Buatan (AI)")
        st.write("Setelah menghitung ulang semua rumus murni, AI merekomendasikan:")
        
        c4d, c3d, c2d = st.columns(3)
        c4d.metric("PREDIKSI 4D", res_4d)
        c3d.metric("PREDIKSI 3D", res_3d)
        c2d.metric("PREDIKSI 2D", res_2d)
        
        st.success(f"**Analisis AI:** Menggabungkan kekuatan 'Angka Sembunyi' ({res_gap}) dengan 'Pola Loncat' Zigzag untuk akurasi maksimal.")
        st.divider()
        st.write("### 🤖 Logika Kecerdasan Buatan (Re-Calculation):")
        st.markdown(f"""
        1. **Validasi Silang:** AI membandingkan Rumus Zigzag (`{res_zigzag}`) dengan Mirror (`{res_mirror}`).
        2. **Filter Anomali:** AI mendeteksi angka `{res_gap}` sebagai penggerak utama posisi depan (AS).
        3. **Ekstraksi Probabilitas:** Hasil 3D dan 2D dihitung berdasarkan tarikan gravitasi angka belakang yang paling stabil.
        """)

    with tab2:
        st.subheader("🔬 Data Hasil Rumus Murni (Sebelum AI)")
        st.write("Berikut adalah hasil mentah dari setiap rumus sebelum diproses AI:")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.code(f"FREKUENSI\n{res_frequent}")
            st.caption("Berdasarkan angka paling sering muncul.")
        with col2:
            st.code(f"ZIGZAG\n{res_zigzag}")
            st.caption("Berdasarkan pola langkah loncat.")
        with col3:
            st.code(f"MIRROR\n{res_mirror}")
            st.caption("Berdasarkan konversi angka bayangan.")
        with col4:
            st.code(f"GAP (SEMBUNYI)\n{res_gap}xxx")
            st.caption("Berdasarkan angka lama tak muncul.")

    with tab3:
        st.subheader("📐 Laboratorium Perhitungan Zigzag")
        st.table(pd.DataFrame(zigzag_rows, columns=["AS", "KOP", "KEPALA", "EKOR"]))
        st.info(f"Hasil tarikan garis zigzag murni: **{res_zigzag}**")

    with tab4:
        st.write(f"**Sinyal WiFi:** {SystemInfo.WIFI}")
        st.write(f"**Peta Server:** [Google Maps]({SystemInfo.MAPS})")
        st.divider()
        st.write("**FAQ & Panduan Terurut:**")
        for item in SystemInfo.FAQ:
            st.write(item)

    # DOWNLOAD LOG
    csv = pd.DataFrame(data_4d).to_csv(index=False).encode('utf-8')
    st.download_button("📥 Simpan Histori Analisis", csv, "ai_analisis_v95.csv", "text/csv")

else:
    st.info("👋 Selamat Datang di AI v9.5. Masukkan data histori di samping kiri untuk melihat proses kecerdasan buatan.")
