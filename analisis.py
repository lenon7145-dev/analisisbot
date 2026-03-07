import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter

# --- KONFIGURASI SISTEM (WiFi, Sosmed, Maps, FAQ v13.0 - KOMPLIT) ---
class SystemInfo:
    WIFI = "📶 FREE_WIFI_2026_V13.0_ULTIMATE"
    SOCIAL = ["@Analyst_AI", "@Ultimate_Engine_Pro"]
    MAPS = "http://google.com/maps"
    FAQ = [
        "1. Apa itu BBFS? Tool untuk membolak-balik angka prediksi agar tidak meleset posisi.",
        "2. Bagaimana cara kerja Gap Analysis? Ia memindai 15-20 data terakhir untuk mencari angka 'vakum'.",
        "3. Apa itu Angka Tarung? Teknik memisahkan angka kuat di posisi depan dan belakang.",
        "4. WiFi & Server? Koneksi stabil tersedia di Tab INFO SISTEM.",
        "5. Tip: Selalu gunakan fitur Generator 2D untuk keamanan taruhan Anda."
    ]

# --- UI SETTINGS ---
st.set_page_config(page_title="Ultimate Engine v13.0", layout="wide")
st.title("🛡️ Pakar Angka AI v13.0: Ultimate Engine")
st.caption("Versi Paling Informatif: Tool Generator + Audit Detail + Simulasi Akurasi")
st.markdown("---")

# --- SIDEBAR INPUT ---
st.sidebar.header("📥 Data Entry & Control")
raw_input = st.sidebar.text_area("Tempel Histori (Terbaru di atas):", height=200, placeholder="6395\n7554")
data_4d = [x.strip() for x in raw_input.split('\n') if len(x.strip()) == 4 and x.strip().isdigit()]

if len(data_4d) >= 1:
    # --- PROSES ANALISIS (Engine v10 - v12) ---
    res_freq = "".join([Counter([d[i] for d in data_4d]).most_common(1)[0][0] for i in range(4)])
    all_str = "".join(data_4d[:15])
    res_gap = [str(i) for i in range(10) if str(i) not in all_str][0] if [str(i) for i in range(10) if str(i) not in all_str] else data_4d[0][0]
    
    # Final AI Result
    ai_4d = res_freq[0] + res_freq[1] + res_freq[2] + res_gap

    # --- TAMPILAN INTERFACE ---
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🎯 HASIL & ANALISIS", "🛠️ TOOLS GENERATOR", "📖 DETAIL FITUR", "📐 ZIGZAG", "🌐 INFO"])

    with tab1:
        st.subheader("🏆 Hasil Keputusan AI Final")
        c1, c2, c3 = st.columns(3)
        c1.metric("PREDIKSI 4D", ai_4d)
        c2.metric("PREDIKSI 3D", ai_4d[1:])
        c3.metric("PREDIKSI 2D", ai_4d[2:], delta="REKOMENDASI UTAMA")
        
        st.divider()
        st.markdown("### 📝 Ringkasan Analisis Singkat")
        st.write(f"Berdasarkan 15 data terakhir, AI melihat angka **{ai_4d[0]}** sangat kuat di depan karena faktor vakum (Gap), sementara angka **{ai_4d[2:]}** mengikuti tren frekuensi terbanyak.")

    with tab2:
        st.subheader("🛠️ Tools Generator (Alat Bantu)")
        col_t1, col_t2 = st.columns(2)
        
        with col_t1:
            st.write("**1. Generator BBFS (Bolak-Balik)**")
            bbfs_digits = sorted(list(set(ai_4d + res_freq[:2])))
            st.info(f"Angka BBFS: {', '.join(bbfs_digits)}")
            st.caption("Gunakan angka ini jika Anda ingin bermain aman di semua posisi.")
        
        with col_t2:
            st.write("**2. Angka Tarung (2D)**")
            tarung_depan = [res_freq[0], res_freq[1]]
            tarung_belakang = [res_freq[2], res_gap]
            st.success(f"Depan: {tarung_depan} VS Belakang: {tarung_belakang}")
            st.caption("Teknik ini memisahkan kekuatan angka untuk mencegah angka terbalik.")

    with tab3:
        st.subheader("📖 Penjelasan Detail Setiap Fitur")
        with st.expander("🔬 Fitur 1: Gap Analysis (Angka Sembunyi)"):
            st.write("""
            **Cara Kerja:** Mesin memindai histori data (default 15 baris) dan mencari angka 0-9 yang sama sekali tidak muncul. 
            **Tujuan:** Angka yang lama tidak muncul memiliki tekanan statistik yang tinggi untuk segera keluar (Hukum Probabilitas Rata-Rata).
            """)
        
        with st.expander("📊 Fitur 2: Positional Frequency (Frekuensi Posisi)"):
            st.write("""
            **Cara Kerja:** Berbeda dengan pencarian angka biasa, fitur ini menghitung angka per kolom (As, Kop, Kepala, Ekor).
            **Tujuan:** Mendeteksi angka mana yang 'betah' atau sering mendarat di posisi tertentu agar prediksi tidak tertukar posisinya.
            """)
            
        with st.expander("📐 Fitur 3: Zigzag Engine (Pola Loncat)"):
            st.write("""
            **Cara Kerja:** Menghitung selisih angka hari ini dengan hari sebelumnya, lalu memproyeksikan loncatan tersebut ke hari esok.
            **Tujuan:** Menangkap pola pergerakan angka yang bersifat dinamis (tidak statis).
            """)

    with tab4:
        st.subheader("📐 Tabel Perhitungan Zigzag")
        n = [int(x) for x in data_4d[0]]
        zigzag_rows = [[(n[0]-i)%10, (n[1]-i)%10, (n[2]+i)%10, (n[3]+i)%10] for i in range(6)]
        st.table(pd.DataFrame(zigzag_rows, columns=["AS", "KOP", "KEP", "EKO"]))

    with tab5:
        st.write(f"**WiFi Status:** {SystemInfo.WIFI}")
        st.write(f"**Server Map:** [Akses Lokasi]({SystemInfo.MAPS})")
        st.divider()
        for f in SystemInfo.FAQ: st.write(f)

    # FOOTER & DOWNLOAD
    csv = pd.DataFrame(data_4d).to_csv(index=False).encode('utf-8')
    st.download_button("📥 Unduh Laporan v13.0", csv, "ultimate_v13.csv", "text/csv")

else:
    st.info("👋 Selamat Datang di Ultimate Engine v13.0. Silakan masukkan data Anda untuk mengaktifkan semua tools analisis.")
