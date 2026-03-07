import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter

# --- SISTEM KONFIGURASI (Sesuai Instruksi Anda) ---
class SystemInfo:
    WIFI = "📶 FREE_HIGH_SPEED_WIFI_2026_V8"
    SOCIAL = ["@Analyst_AI", "@Data_Mining_King"]
    MAPS = "http://googleusercontent.com/maps.google.com/6"
    FAQ = [
        "1. Apa itu God Mode? Penggabungan Statistik, Sniper, Zigzag, Mistik, dan Shio.",
        "2. Rumus Mistik? Mengonversi angka berdasarkan pola getaran angka tradisional.",
        "3. Cara Baca Konsensus? Hasil akhir adalah angka yang paling banyak disetujui semua rumus.",
        "4. FAQ & Info? Cek tab System Info untuk WiFi dan Maps.",
        "5. Strategi: Jika Angka Utama dan Zigzag sama, itu adalah sinyal KUAT."
    ]

# --- UI SETTINGS ---
st.set_page_config(page_title="Ultimate Analyst Bot v8.0", layout="centered")
st.title("🔥 Ultimate Analyst Bot v8.0")
st.caption("God Mode: Statistical + Sniper + Zigzag + Mistik + Shio Engine")
st.markdown("---")

# --- SIDEBAR INPUT ---
st.sidebar.header("📥 Data Source")
raw_input = st.sidebar.text_area("Input Histori (Terbaru di atas):", height=200, placeholder="Contoh: 5436")
data_4d = [x.strip() for x in raw_input.split('\n') if len(x.strip()) == 4 and x.strip().isdigit()]

# --- RUMUS DASAR (MISTIK & INDEX) ---
index_map = {'0':'5', '1':'6', '2':'7', '3':'8', '4':'9', '5':'0', '6':'1', '7':'2', '8':'3', '9':'4'}
mistik_lama = {'1':'0', '2':'5', '3':'8', '4':'7', '6':'9', '0':'1', '5':'2', '8':'3', '7':'4', '9':'6'}
mistik_baru = {'1':'7', '2':'6', '3':'9', '4':'5', '0':'8', '7':'1', '6':'2', '9':'3', '5':'4', '8':'0'}

if data_4d:
    # 1. RUMUS STATISTIK (TREND)
    best_stat = []
    for i in range(4):
        weighted_data = []
        for idx, entry in enumerate(data_4d):
            weight = max(1, len(data_4d) - idx)
            weighted_data.extend([entry[i]] * weight)
        best_stat.append(Counter(weighted_data).most_common(1)[0][0])
    res_stat = "".join(best_stat)

    # 2. RUMUS SNIPER (INDEX)
    res_index = "".join([index_map.get(n, n) for n in best_stat])

    # 3. RUMUS MISTIK (LAMA & BARU)
    res_mistik_l = "".join([mistik_lama.get(n, n) for n in best_stat])
    res_mistik_b = "".join([mistik_baru.get(n, n) for n in best_stat])

    # 4. RUMUS ZIGZAG
    latest = data_4d[0]
    n = [int(x) for x in latest]
    zigzag_rows = []
    for i in range(6):
        row = [(n[0]-i)%10, (n[1]-i)%10, (n[2]+i)%10, (n[3]+i)%10]
        zigzag_rows.append(row)
    res_zigzag = f"{zigzag_rows[1][0]}{zigzag_rows[3][1]}{zigzag_rows[4][2]}{zigzag_rows[5][3]}"

    # --- KONSENSUS AKHIR (THE GOD NUMBER) ---
    final_jitu = []
    engines = [res_stat, res_index, res_mistik_l, res_mistik_b, res_zigzag]
    for i in range(4):
        pool = [engine[i] for engine in engines]
        final_jitu.append(Counter(pool).most_common(1)[0][0])
    res_final = "".join(final_jitu)

    # --- TAMPILAN UTAMA ---
    tab1, tab2, tab3, tab4 = st.tabs(["🎯 Hasil God Mode", "🔮 Mistik & Shio", "📐 Zigzag Lab", "🌐 System Info"])

    with tab1:
        st.subheader("🏆 Angka Jitu Konsensus")
        st.metric("FINAL TARGET (4D)", res_final)
        
        st.divider()
        st.write("### 🚀 Perbandingan Semua Mesin")
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"**Statistik Trend:** {res_stat}")
            st.info(f"**Sniper Index:** {res_index}")
        with col2:
            st.info(f"**Zigzag Pattern:** {res_zigzag}")
            st.info(f"**Mistik Gabungan:** {res_mistik_l}")
        
        st.write("### 🔔 Notifikasi Strategi")
        st.code(f"SYSTEM v8.0 READY:\nPrediksi Konsensus: {res_final}\nCadangan Mistik: {res_mistik_b}", language="text")

    with tab2:
        st.subheader("🧪 Lab Mistik & Karakter Angka")
        st.write("Hasil konversi angka berdasarkan getaran Mistik:")
        st.write(f"- **Mistik Lama:** {res_mistik_l}")
        st.write(f"- **Mistik Baru:** {res_mistik_b}")
        st.write(f"- **Index:** {res_index}")
        
        st.divider()
        st.subheader("🐂 Analisis Karakter (Shio/Parity)")
        # Deteksi Ganjil/Genap & Besar/Kecil
        is_even = "Genap" if int(res_final[3]) % 2 == 0 else "Ganjil"
        is_big = "Besar" if int(res_final[2:]) >= 50 else "Kecil"
        st.success(f"Prediksi Karakter 2D: **{is_even} - {is_big}**")

    with tab3:
        st.subheader("📐 Tabel Zigzag Otomatis")
        st.table(pd.DataFrame(zigzag_rows, columns=["AS (▼)", "KOP (▼)", "KEP (▲)", "EKO (▲)"]))
        st.write(f"**Tarikan Garis Zigzag:** {res_zigzag}")

    with tab4:
        st.write(f"**WiFi:** {SystemInfo.WIFI}")
        st.write(f"**Maps:** [Cek Lokasi]({SystemInfo.MAPS})")
        st.divider()
        st.write("**FAQ Terurut (v8.0):**")
        for item in SystemInfo.FAQ: st.write(item)

    # EXPORT
    csv = pd.DataFrame(data_4d).to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Log v8.0", csv, "analisis_godmode.csv", "text/csv")

else:
    st.info("👋 God Mode v8.0 Aktif. Masukkan histori untuk menjalankan semua rumus sekaligus.")
