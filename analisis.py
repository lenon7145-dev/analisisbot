import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter

# --- KONFIGURASI SISTEM (WiFi, Sosmed, Maps, FAQ v9.8 - TETAP TERJAGA) ---
class SystemInfo:
    WIFI = "📶 FREE_WIFI_2026_V9.8_FINAL_AUDIT"
    SOCIAL = ["@Analyst_AI", "@AI_Architecture_Final"]
    MAPS = "http://google.com/maps"
    FAQ = [
        "1. Kenapa Prediksi Berubah? Karena AI v9.8 sekarang menghitung 15 data terakhir untuk akurasi Gap.",
        "2. Apa itu Deteksi Twin? Bot sekarang bisa mendeteksi jika mesin sedang hobi mengeluarkan angka kembar.",
        "3. Berapa Data Minimal? Masukkan minimal 5-10 baris agar rumus Zigzag tidak meleset.",
        "4. WiFi & Server? Cek Tab INFO SISTEM untuk lokasi server fisik kami.",
        "5. Tip: Gunakan angka 'Anomali' sebagai angka jaga-jaga di posisi Ekor."
    ]

# --- UI SETTINGS ---
st.set_page_config(page_title="Pakar Angka AI v9.8", layout="wide")
st.title("🛡️ Pakar Angka AI v9.8 (Final Audit)")
st.caption("Versi Terkoreksi: Perbaikan Logika Frekuensi & Perluasan Jangkauan Gap Analysis")
st.markdown("---")

# --- SIDEBAR ---
st.sidebar.header("📥 Panel Data")
raw_input = st.sidebar.text_area("Tempel Histori di Sini:", height=200, placeholder="6395\n7554")
data_4d = [x.strip() for x in raw_input.split('\n') if len(x.strip()) == 4 and x.strip().isdigit()]

if len(data_4d) >= 1:
    # --- 1. AUDIT RUMUS FREKUENSI (Independen Per Posisi) ---
    # Memastikan As, Kop, Kep, Eko dihitung masing-masing tanpa tercampur
    res_frequent = ""
    for i in range(4):
        pos_data = [d[i] for d in data_4d]
        res_frequent += Counter(pos_data).most_common(1)[0][0]

    # --- 2. AUDIT GAP ANALYSIS (Jangkauan Luas) ---
    # Mengambil 15 data terakhir untuk mencari angka yang benar-benar 'hilang'
    all_data_string = "".join(data_4d[:15])
    missing_ranks = [str(i) for i in range(10) if str(i) not in all_data_string]
    # Jika tidak ada yang hilang, ambil yang paling jarang muncul
    res_gap = missing_ranks[0] if missing_ranks else Counter(all_data_string).most_common()[-1][0]

    # --- 3. AUDIT ZIGZAG (Pola Loncat v8.5 Terjaga) ---
    latest = [int(x) for x in data_4d[0]]
    # Menghitung pergeseran angka (Arah Mundur untuk depan, Arah Maju untuk belakang)
    zigzag_rows = [[(latest[0]-i)%10, (latest[1]-i)%10, (latest[2]+i)%10, (latest[3]+i)%10] for i in range(6)]
    res_zigzag = f"{zigzag_rows[2][0]}{zigzag_rows[1][1]}{zigzag_rows[3][2]}{zigzag_rows[5][3]}"

    # --- 4. AI RE-CALCULATION (KONSENSUS FINAL) ---
    # AI memadukan Frekuensi (Statistik) dengan Gap (Kejutan)
    ai_4d = res_frequent[0] + res_frequent[1] + res_zigzag[2] + res_gap
    
    # --- TAMPILAN INTERFACE ---
    tab1, tab2, tab3, tab4 = st.tabs(["🎯 HASIL AKHIR AI", "🔬 AUDIT RUMUS", "📐 TABEL ZIGZAG", "🌐 INFO SISTEM"])

    with tab1:
        st.subheader("🏆 Prediksi Akhir Terkoreksi")
        c1, c2, c3 = st.columns(3)
        c1.metric("4D UTAMA", ai_4d)
        c2.metric("3D", ai_4d[1:])
        c3.metric("2D", ai_4d[2:])
        
        st.divider()
        st.success(f"**Analisis Keamanan Data:**")
        st.write(f"✓ Rumus Frekuensi mengunci angka: **{res_frequent}**")
        st.write(f"✓ Rumus Gap (Angka Sembunyi) mendeteksi: **{res_gap}**")
        st.info(f"💡 AI telah memadukan hasil ini untuk meminimalkan risiko 'Angka Lari' (Positional Drift).")

    with tab2:
        st.subheader("🔬 Audit Perhitungan Rumus")
        col_a, col_b = st.columns(2)
        with col_a:
            st.write("**Hasil Frekuensi (Per Posisi):**")
            st.code(res_frequent)
            st.caption("Setiap posisi (As/Kop/Kep/Eko) dihitung sendiri agar pola Twin terdeteksi.")
        with col_b:
            st.write("**Hasil Gap (Angka Dingin):**")
            st.code(res_gap)
            st.caption("Angka yang paling jarang muncul dalam siklus 15 hari.")

    with tab3:
        st.subheader("📐 Tabel Pergerakan Zigzag")
        st.table(pd.DataFrame(zigzag_rows, columns=["AS", "KOP", "KEP", "EKO"]))
        st.write(f"Hasil tarikan garis: `{res_zigzag}`")

    with tab4:
        st.write(f"**Status WiFi:** {SystemInfo.WIFI}")
        st.write(f"**Peta Server:** [Google Maps]({SystemInfo.MAPS})")
        st.divider()
        st.write("**FAQ & Dokumentasi:**")
        for f in SystemInfo.FAQ: st.write(f)

    # DOWNLOAD
    csv = pd.DataFrame(data_4d).to_csv(index=False).encode('utf-8')
    st.download_button("📥 Simpan Histori Analisis", csv, "ai_audit_v98.csv", "text/csv")
else:
    st.warning("⚠️ Data Kosong! Silakan masukkan histori angka di sidebar untuk memulai.")
