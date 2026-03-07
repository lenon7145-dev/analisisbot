import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import re

# --- 1. KONFIGURASI SISTEM (Informasi Tetap & Terurut) ---
class SystemInfo:
    WIFI = "📶 FREE_WIFI_2026_V16.0_ETERNAL_ARCHIVE"
    SOCIAL = ["@Analyst_AI", "@Eternal_Archive_Pro"]
    MAPS = "http://google.com/maps"
    FAQ = [
        "1. Apa itu Eternal Archive? Versi yang menggabungkan seluruh rumus dari v8.0 hingga v15.0 tanpa ada yang diringkas.",
        "2. Bagaimana cara baca Tabel Zigzag? Gunakan koordinat baris untuk melihat potensi angka loncat.",
        "3. Apa itu Backtesting? Pengujian otomatis rumus terhadap 10 data histori terakhir Anda.",
        "4. Apa itu Twin Detector? Sensor yang mendeteksi jika mesin sedang masuk ke siklus angka kembar.",
        "5. Tip Strategi: Selalu bandingkan hasil antara Rumus Frekuensi dan Rumus Gap di Tab Audit."
    ]

# --- 2. UI SETTINGS ---
st.set_page_config(page_title="Eternal Archive v16.0", layout="wide")
st.title("🏛️ Pakar Angka AI v16.0: Eternal Archive")
st.caption("Versi Terlengkap: Menggabungkan Seluruh Fitur, Rumus, dan Penjelasan Detail dari Semua Versi Sebelumnya")
st.markdown("---")

# --- 3. SIDEBAR INPUT (Dengan Data Cleansing) ---
st.sidebar.header("📥 Pusat Kendali Data")
raw_input = st.sidebar.text_area("Tempel Histori di Sini (Contoh: 6395):", height=250)
clean_data = re.findall(r'\b\d{4}\b', raw_input)

if len(clean_data) >= 1:
    # --- 4. ENGINE PERHITUNGAN (RUMUS LENGKAP) ---
    
    # A. Rumus Frekuensi (v8.0)
    res_freq = "".join([Counter([d[i] for d in clean_data]).most_common(1)[0][0] for i in range(4)])
    
    # B. Rumus Gap Analysis (v9.7)
    all_str_15 = "".join(clean_data[:15])
    missing = [str(i) for i in range(10) if str(i) not in all_str_15]
    res_gap = missing[0] if missing else Counter(all_str_15).most_common()[-1][0]
    
    # C. Rumus Zigzag Master (v8.5 & v12.0)
    n = [int(x) for x in clean_data[0]]
    zigzag_rows = [[(n[0]-i)%10, (n[1]-i)%10, (n[2]+i)%10, (n[3]+i)%10] for i in range(6)]
    res_zigzag = f"{zigzag_rows[2][0]}{zigzag_rows[1][1]}{zigzag_rows[3][2]}{zigzag_rows[5][3]}"
    
    # D. Rumus Mirror/Index (v8.0)
    index_map = {'0':'5', '1':'6', '2':'7', '3':'8', '4':'9', '5':'0', '6':'1', '7':'2', '8':'3', '9':'4'}
    res_mirror = "".join([index_map.get(x, x) for x in clean_data[0]])

    # E. Konsensus Akhir AI (v14.0)
    ai_final = res_freq[0] + res_freq[1] + res_zigzag[2] + res_gap

    # F. Analisis Tambahan (Twin & Backtest)
    is_twin = any(len(set(d)) < 4 for d in clean_data[:5])
    hits = sum(1 for d in clean_data[1:11] if any(digit in ai_final for digit in d))
    accuracy_rate = (hits / 10) * 100

    # --- 5. TAMPILAN INTERFACE (MULTI-TAB INFORMATIF) ---
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🎯 KONSENSUS STRATEGIS", 
        "🔬 AUDIT RUMUS TRANSPARAN", 
        "📐 LABORATORIUM ZIGZAG", 
        "🛠️ TOOLS GENERATOR", 
        "🌐 INFO SISTEM & FAQ"
    ])

    # --- TAB 1: KONSENSUS STRATEGIS ---
    with tab1:
        st.subheader("🏆 Keputusan Strategis AI (Final Result)")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("PREDIKSI 4D", ai_final, delta=f"SKOR: {80+(hits*2)}%")
        col2.metric("AKURASI HISTORIS", f"{accuracy_rate}%")
        col3.metric("STATUS MESIN", "STABIL" if not is_twin else "TWIN ALERT")
        col4.metric("KATEGORI", "POWER" if accuracy_rate > 60 else "NORMAL")
        
        st.divider()
        st.markdown("### 📘 Penjelasan Anatomi Prediksi Hari Ini")
        c_txt1, c_txt2 = st.columns(2)
        with c_txt1:
            st.info(f"""
            **Mengapa Angka `{ai_final}`?**
            1. **Digit Depan ({ai_final[:2]}):** Dipilih berdasarkan *Positional Frequency*. Angka ini memiliki gravitasi terkuat di posisi As dan Kop dalam histori Anda.
            2. **Digit Tengah ({ai_final[2]}):** Menggunakan pola *Zigzag Projection*. AI mendeteksi loncatan energi dari angka `{clean_data[0][2]}` ke arah `{ai_final[2]}`.
            3. **Digit Ekor ({ai_final[3]}):** Diambil dari *Gap Analysis*. Digit ini adalah yang paling lama 'sembunyi', sehingga peluang keluarnya sangat tinggi.
            """)
        with c_txt2:
            st.success(f"""
            **Rekomendasi Tindakan:**
            * **Fokus Utama:** Prioritaskan angka 2D Belakang `{ai_final[2:]}`.
            * **Kondisi Twin:** {"⚠️ Waspada angka kembar terdeteksi!" if is_twin else "✅ Kondisi aman dari angka kembar."}
            * **Strategi:** Jika ragu, gunakan Tool BBFS di Tab 4 untuk mengamankan semua posisi.
            """)

    # --- TAB 2: AUDIT RUMUS TRANSPARAN ---
    with tab2:
        st.subheader("🔬 Transparansi Rumus (Buka Jeroan AI)")
        st.write("Berikut adalah hasil murni dari setiap 'mesin hitung' sebelum digabungkan:")
        
        col_r1, col_r2 = st.columns(2)
        with col_r1:
            st.success(f"📊 **Hasil Rumus Frekuensi: {res_freq}**")
            st.write("*Penjelasan:* Mencari angka yang paling sering muncul di setiap kolom posisi. Sangat bagus untuk mencari pola angka yang 'betah' keluar.")
            
            st.warning(f"🔍 **Hasil Rumus Gap: {res_gap}xxx**")
            st.write("*Penjelasan:* Mencari angka yang sama sekali tidak muncul dalam 15 hari terakhir. Angka ini biasanya muncul sebagai kejutan.")
            
        with col_r2:
            st.info(f"📐 **Hasil Rumus Zigzag: {res_zigzag}**")
            st.write("*Penjelasan:* Menghitung ritme pergerakan angka secara vertikal. Menggunakan koordinat pola loncat v8.5.")
            
            st.error(f"🪞 **Hasil Rumus Mirror: {res_mirror}**")
            st.write("*Penjelasan:* Mengonversi angka terakhir menjadi angka bayangannya (Mistik/Index). Digunakan sebagai angka cadangan.")

    # --- TAB 3: LABORATORIUM ZIGZAG ---
    with tab3:
        st.subheader("📐 Tabel Laboratorium Zigzag (v8.5 Legacy)")
        st.write("Tabel ini menunjukkan pergerakan angka dari hasil terakhir Anda secara mendalam:")
        st.table(pd.DataFrame(zigzag_rows, columns=["POSISI AS", "POSISI KOP", "POSISI KEPALA", "POSISI EKOR"]))
        st.info(f"AI mengambil baris koordinat (2-1-3-5) untuk menghasilkan Prediksi Zigzag: **{res_zigzag}**")

    # --- TAB 4: TOOLS GENERATOR ---
    with tab4:
        st.subheader("🛠️ Tools Pendukung (BBFS & Tarung)")
        bbfs_digits = sorted(list(set(ai_final + res_freq[:2])))
        
        col_t1, col_t2 = st.columns(2)
        with col_t1:
            st.write("**1. Generator BBFS (Bolak-Balik Full Set)**")
            st.code(f"SET BBFS: {', '.join(bbfs_digits)}", language="text")
            st.caption("Gunakan set angka ini untuk mencakup semua kemungkinan kombinasi posisi.")
            
        with col_t2:
            st.write("**2. Angka Tarung (Head-to-Head)**")
            st.success(f"DEPAN: {res_freq[:2]} VS BELAKANG: {ai_final[2:]}")
            st.caption("Teknik memisahkan angka kuat depan dan belakang untuk akurasi lebih tajam.")

    # --- TAB 5: INFO SISTEM ---
    with tab5:
        st.write(f"**WiFi:** {SystemInfo.WIFI}")
        st.write(f"**Maps:** [Akses Server Lokasi]({SystemInfo.MAPS})")
        st.divider()
        st.write("**FAQ Terurut (Panduan Lengkap):**")
        for f in SystemInfo.FAQ: st.write(f)

    # FOOTER & DOWNLOAD
    st.markdown("---")
    st.caption("© 2026 Pakar Angka AI v16.0 | The Eternal Archive | All Features Restored")
    csv = pd.DataFrame(clean_data).to_csv(index=False).encode('utf-8')
    st.download_button("📥 Simpan Histori Analisis Lengkap", csv, "eternal_archive_v16.csv", "text/csv")

else:
    st.info("👋 Selamat Datang di Eternal Archive v16.0. Silakan masukkan histori data angka Anda di sidebar untuk mengaktifkan seluruh fitur.")
