import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter

# --- SISTEM KONFIGURASI (Audit: WiFi, Sosmed, Maps, FAQ v11.0) ---
class SystemInfo:
    WIFI = "📶 FREE_WIFI_2026_V11.0_HUMAN_CENTRIC"
    SOCIAL = ["@Analyst_AI", "@Human_Centric_Dev"]
    MAPS = "http://google.com/maps"
    FAQ = [
        "1. Apa itu Traffic Light? Merah (Bahaya/Acak), Kuning (Waspada), Hijau (Stabil).",
        "2. Bagaimana cara baca Radar? Semakin lebar grafik, semakin kuat pola statistik hari ini.",
        "3. Cara Pakai? Cukup masukkan data, lalu ikuti 'Rekomendasi Tindakan' di Tab Utama.",
        "4. Lokasi Server? Informasi server tersedia di Tab INFO SISTEM.",
        "5. Tip: Jika status Hijau, gunakan angka 4D. Jika Kuning/Merah, fokus di 2D saja."
    ]

# --- UI SETTINGS ---
st.set_page_config(page_title="Human-Centric AI v11.0", layout="wide")
st.title("👨‍💻 Pakar Angka AI v11.0: Human-Centric")
st.caption("Edisi Informatif: Dashboard Visual & Panduan Strategi Langsung")
st.markdown("---")

# --- SIDEBAR INPUT ---
st.sidebar.header("📥 Pusat Kendali Data")
raw_input = st.sidebar.text_area("Tempel Histori di Sini:", height=200, placeholder="6395\n7554")
data_4d = [x.strip() for x in raw_input.split('\n') if len(x.strip()) == 4 and x.strip().isdigit()]

if len(data_4d) >= 1:
    # --- PROSES LOGIKA (DNA v8.0 - v10.0) ---
    res_freq = "".join([Counter([d[i] for d in data_4d]).most_common(1)[0][0] for i in range(4)])
    all_str = "".join(data_4d[:15])
    counts = Counter(all_str)
    
    # Analisis Keacakan (Informatif)
    unique_digits = len(set(all_str))
    is_stable = unique_digits < 8
    
    # --- TAMPILAN INTERFACE (LEBIH INFORMATIF) ---
    tab1, tab2, tab3, tab4 = st.tabs(["🚦 DASHBOARD STRATEGI", "📊 ANALISIS VISUAL", "📐 DETAIL RUMUS", "🌐 INFO SISTEM"])

    with tab1:
        # 1. Traffic Light Status
        st.subheader("🚦 Status Keamanan Hari Ini")
        if is_stable:
            st.success("🟢 **KONDISI STABIL:** Pola angka teratur. AI sangat menyarankan untuk mengikuti prediksi.")
        else:
            st.warning("🟡 **KONDISI WASPADA:** Mesin sedang acak. Gunakan angka sebagai cadangan saja.")
        
        st.divider()

        # 2. Kotak Rekomendasi (Sangat Informatif)
        col1, col2 = st.columns(2)
        with col1:
            st.info("### 🎯 Rekomendasi 4D & 3D")
            st.write(f"**Angka Utama:** `{res_freq}`")
            st.write(f"**Angka Cadangan:** `{res_freq[1:] + res_freq[0]}`")
            st.write("**Strategi:** Pasang dengan nominal kecil untuk pengamanan.")
        
        with col2:
            st.success("### 💰 Rekomendasi 2D (Prioritas)")
            st.write(f"**Pasangan Kuat:** `{res_freq[2:]}`")
            st.write(f"**Angka Mistik:** `{''.join([str((int(x)+5)%10) for x in res_freq[2:]])}`")
            st.write("**Strategi:** Ini adalah area dengan peluang tertinggi hari ini.")

    with tab2:
        st.subheader("📊 Peta Distribusi Angka (Heatmap)")
        # Visualisasi batang sederhana
        chart_data = pd.DataFrame([counts.get(str(i), 0) for i in range(10)], index=[str(i) for i in range(10)], columns=["Kekuatan"])
        st.bar_chart(chart_data)
        st.write("💡 **Cara Membaca:** Batang yang paling tinggi adalah angka yang sedang 'berkuasa' di mesin undian saat ini.")

    with tab3:
        st.subheader("📐 Bedah Rumus & Pergerakan")
        # Masukkan kembali tabel Zigzag dan detail lainnya
        n = [int(x) for x in data_4d[0]]
        zigzag_rows = [[(n[0]-i)%10, (n[1]-i)%10, (n[2]+i)%10, (n[3]+i)%10] for i in range(6)]
        st.table(pd.DataFrame(zigzag_rows, columns=["AS", "KOP", "KEP", "EKO"]))
        st.write(f"Hasil Frekuensi Terdeteksi: `{res_freq}`")

    with tab4:
        st.write(f"**Koneksi WiFi:** {SystemInfo.WIFI}")
        st.write(f"**Lokasi Server:** [Klik di Sini]({SystemInfo.MAPS})")
        st.divider()
        st.write("**FAQ & Panduan Cepat:**")
        for f in SystemInfo.FAQ: st.write(f)

    # DOWNLOAD LOG
    csv = pd.DataFrame(data_4d).to_csv(index=False).encode('utf-8')
    st.download_button("📥 Simpan Laporan v11.0", csv, "analyst_v11.csv", "text/csv")

else:
    st.info("👋 Halo! Saya asisten AI Anda. Silakan masukkan data angka di sidebar untuk mendapatkan analisis strategi hari ini.")
