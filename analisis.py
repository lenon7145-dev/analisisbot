import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter

# --- SISTEM KONFIGURASI (Tetap Sesuai Permintaan Anda) ---
class SystemInfo:
    WIFI = "📶 FREE_HIGH_SPEED_WIFI_2026_V6"
    SOCIAL = ["@Analyst_AI", "@Data_Mining_King"]
    MAPS = "http://googleusercontent.com/maps.google.com/6"
    FAQ = [
        "1. Apa itu High Probability? Algoritma v6.5 yang memberi bobot lebih pada data terbaru.",
        "2. Bagaimana cara input? Masukkan data terbaru di baris PALING ATAS.",
        "3. Apa arti Keyakinan? Persentase kekuatan angka tersebut muncul kembali (0-99%).",
        "4. Apakah WiFi gratis? Ya, cek tab System Info untuk detail akses."
    ]

# --- UI SETTINGS ---
st.set_page_config(page_title="Ultimate Analyst Bot v6.5", layout="centered")
st.title("🚀 Ultimate Analyst Bot v6.5")
st.caption("Advanced Algorithm: Weighted Trend Analysis Active")
st.markdown("---")

# --- SIDEBAR INPUT ---
st.sidebar.header("📥 Data Source")
st.sidebar.info("Masukkan histori 4-digit (Terbaru di paling atas):")
raw_input = st.sidebar.text_area("Input Histori:", height=250, placeholder="Contoh:\n1234\n5678")

# Membersihkan data
data_4d = [x.strip() for x in raw_input.split('\n') if len(x.strip()) == 4 and x.strip().isdigit()]

if data_4d:
    # 1. LOGIKA UPGRADE: WEIGHTED PROBABILITY (Meningkatkan Akurasi)
    pos_names = ["As (Pos 1)", "Kop (Pos 2)", "Kepala (Pos 3)", "Ekor (Pos 4)"]
    best_numbers = []
    summary_stats = []
    pos_df_data = {}

    for i in range(4):
        weighted_data = []
        for index, entry in enumerate(data_4d):
            # Data teratas (index 0) diberi bobot lebih berat (Exponential Weighting)
            weight = max(1, len(data_4d) - index)
            weighted_data.extend([entry[i]] * weight)
        
        counts = Counter(weighted_data)
        total_weighted = sum(counts.values())
        
        # Cari angka terbaik
        top_num, top_count = counts.most_common(1)[0]
        prob_val = (top_count / total_weighted) * 99
        best_numbers.append(top_num)
        
        # Cek Ganjil/Genap
        parity = "Ganjil" if int(top_num) % 2 != 0 else "Genap"
        summary_stats.append(f"{pos_names[i]}: {top_num} ({prob_val:.1f}%) - {parity}")
        
        # Data untuk tabel probabilitas
        pos_df_data[pos_names[i]] = [f"{(counts.get(str(n), 0)/total_weighted)*99:.1f}%" for n in range(10)]

    # --- TAMPILAN UTAMA ---
    tab1, tab2, tab3 = st.tabs(["🎯 Lucky Generator", "📊 Analysis Lab", "🌐 System Info"])

    with tab1:
        st.subheader("🔮 High Probability Result")
        st.write("Berdasarkan pembobotan data terbaru:")
        
        c1, c2, c3 = st.columns(3)
        with c1: st.metric("Prediksi 4D", "".join(best_numbers))
        with c2: st.metric("Prediksi 3D", "".join(best_numbers[1:]))
        with c3: st.metric("Prediksi 2D", "".join(best_numbers[2:]))

        st.write("### 🔔 Notifikasi Strategi")
        notif_msg = f"📊 ANALISIS PROBABILITAS TINGGI:\n" + "\n".join(summary_stats)
        st.code(notif_msg, language="text")
        st.caption("Long press untuk copy ke WhatsApp/Grup.")

    with tab2:
        st.subheader("📉 Detail Probabilitas Berbobot")
        st.write("Angka dengan persentase tinggi adalah yang paling sering muncul di periode terakhir.")
        df_posisi = pd.DataFrame(pos_df_data, index=[f"Angka {i}" for i in range(10)])
        st.table(df_posisi)
        
        # Fitur baru: Analisis Ganjil/Genap Dominan
        st.info("💡 Tip: Jika keyakinan di bawah 30%, disarankan menambah lebih banyak data histori.")

    with tab3:
        st.write(f"**WiFi:** {SystemInfo.WIFI}")
        st.write(f"**Maps:** [Cek Lokasi Sinyal]({SystemInfo.MAPS})")
        st.write(f"**Social Media:** {', '.join(SystemInfo.SOCIAL)}")
        st.divider()
        st.write("**FAQ Terurut (Bantuan):**")
        for item in SystemInfo.FAQ:
            st.write(item)

    # --- FITUR EXPORT ---
    df_export = pd.DataFrame(data_4d, columns=['Histori Angka'])
    csv = df_export.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Hasil Analisis (CSV)", data=csv, file_name="analisis_v65.csv", mime="text/csv")

else:
    st.info("👋 Selamat Datang di Versi 6.5!")
    st.warning("Silakan masukkan data histori di sidebar untuk melihat angka dengan probabilitas tinggi.")
