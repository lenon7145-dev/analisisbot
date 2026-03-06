import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter

# --- SISTEM KONFIGURASI ---
class SystemInfo:
    WIFI = "📶 FREE_HIGH_SPEED_WIFI_2026_V6"
    SOCIAL = ["@Analyst_AI", "@Data_Mining_King"]
    MAPS = "http://googleusercontent.com/maps.google.com/6"
    FAQ = [
        "1. Apa itu Lucky Generator? Algoritma yang memilih angka dengan probabilitas tertinggi.",
        "2. Bagaimana Notifikasi bekerja? Memberikan ringkasan statistik dalam satu klik.",
        "3. Cara Export? Gunakan tombol Download CSV di bagian bawah.",
        "4. Apakah ini bisa untuk 2D? Ya, pilih menu target 2D di tab prediksi."
    ]

# --- UI SETTINGS ---
st.set_page_config(page_title="Ultimate Analyst Bot", layout="centered")

st.title("🚀 Ultimate Analyst Bot v6.1")
st.markdown("---")

# --- SIDEBAR INPUT ---
st.sidebar.header("📥 Data Source")
st.sidebar.info("Masukkan daftar angka 4-digit di bawah ini:")
raw_input = st.sidebar.text_area("Input Histori (Satu baris satu angka):", height=250, placeholder="1234\n5678\n9012")

# Membersihkan data dari baris kosong atau karakter aneh
data_4d = [x.strip() for x in raw_input.split('\n') if len(x.strip()) == 4 and x.strip().isdigit()]

if data_4d:
    # 1. LOGIKA PERHITUNGAN PROBABILITAS POSISI
    pos_names = ["As (Pos 1)", "Kop (Pos 2)", "Kepala (Pos 3)", "Ekor (Pos 4)"]
    best_numbers = []
    summary_stats = []

    # Membuat DataFrame untuk visualisasi statistik
    pos_df_data = {}

    for i in range(4):
        col_data = [d[i] for d in data_4d]
        counts = Counter(col_data)
        total = len(col_data)
        
        # Cari angka terbaik (0-9) di posisi ini
        top_num, top_count = counts.most_common(1)[0]
        prob_val = (top_count / total) * 99
        best_numbers.append(top_num)
        summary_stats.append(f"{pos_names[i]}: {top_num} ({prob_val:.1f}%)")
        
        # Data untuk tabel probabilitas lengkap 0-9
        pos_df_data[pos_names[i]] = [f"{(counts.get(str(n), 0)/total)*99:.1f}%" for n in range(10)]

    # --- TAMPILAN UTAMA ---
    tab1, tab2, tab3 = st.tabs(["🎯 Lucky Generator", "📊 Full Statistics", "🌐 System Info"])

    with tab1:
        st.subheader("🔮 Smart Lucky Generator")
        st.write("Angka terkuat berdasarkan histori Anda:")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Prediksi 4D", "".join(best_numbers))
        with c2:
            st.metric("Prediksi 3D", "".join(best_numbers[1:]))
        with c3:
            st.metric("Prediksi 2D", "".join(best_numbers[2:]))

        st.write("### 🔔 Notifikasi Ringkasan")
        notif_msg = f"📊 ANALISIS DATA SELESAI:\n" + "\n".join(summary_stats)
        st.code(notif_msg, language="text")
        st.caption("Tekan lama pada kotak di atas untuk copy hasil ke WhatsApp.")

    with tab2:
        st.subheader("📉 Detail Probabilitas Posisi (0-9)")
        st.write("Peluang kemunculan tiap angka di setiap posisi (0-99%):")
        df_posisi = pd.DataFrame(pos_df_data, index=[f"Angka {i}" for i in range(10)])
        st.table(df_posisi)

    with tab3:
        st.write(f"**WiFi:** {SystemInfo.WIFI}")
        st.write(f"**Maps:** [Buka Lokasi]({SystemInfo.MAPS})")
        st.write(f"**Social Media:** {', '.join(SystemInfo.SOCIAL)}")
        st.divider()
        st.write("**FAQ Terurut (Bantuan):**")
        for item in SystemInfo.FAQ:
            st.write(item)

    # --- FITUR EXPORT ---
    df_export = pd.DataFrame(data_4d, columns=['Histori Angka'])
    csv = df_export.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Hasil Analisis (CSV)", data=csv, file_name="analisis_data_mobile.csv", mime="text/csv")

else:
    # Tampilan awal jika data kosong
    st.info("👋 Halo! Saya siap membantu analisis data angka Anda.")
    st.warning("Silakan masukkan data histori 4-digit Anda di menu sidebar (samping) untuk memulai.")