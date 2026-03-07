import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter

# --- SISTEM KONFIGURASI (WiFi, Sosmed, Maps, FAQ v13.5 - TETAP LENGKAP) ---
class SystemInfo:
    WIFI = "📶 FREE_WIFI_2026_V13.5_TRANSPARENT"
    SOCIAL = ["@Analyst_AI", "@Transparent_Architect_Pro"]
    MAPS = "http://google.com/maps"
    FAQ = [
        "1. Mengapa hasil setiap rumus dimunculkan? Agar Anda bisa membandingkan akurasi setiap metode secara langsung.",
        "2. Apa itu Gap Analysis? Pencarian angka yang memiliki 'kekosongan' statistik dalam periode lama.",
        "3. Apa itu Zigzag Engine? Penghitungan langkah vertikal dari angka terakhir yang keluar.",
        "4. WiFi & Server? Akses tetap tersedia gratis di Tab INFO SISTEM.",
        "5. Tip: Jika tiga rumus menghasilkan angka yang sama, itu adalah angka dengan probabilitas ledakan tertinggi."
    ]

# --- UI SETTINGS ---
st.set_page_config(page_title="Transparent Architect v13.5", layout="wide")
st.title("🏗️ Pakar Angka AI v13.5: Transparent Architect")
st.caption("Edisi Transparan: Menampilkan Semua Hasil Rumus & Penjelasan Teknis Mendalam")
st.markdown("---")

# --- SIDEBAR INPUT ---
st.sidebar.header("📥 Panel Data Histori")
raw_input = st.sidebar.text_area("Tempel Histori (Terbaru di atas):", height=200, placeholder="6395\n7554")
data_4d = [x.strip() for x in raw_input.split('\n') if len(x.strip()) == 4 and x.strip().isdigit()]

if len(data_4d) >= 1:
    # --- PROSES PERHITUNGAN SEMUA RUMUS (TRANSPARAN) ---
    
    # 1. RUMUS FREKUENSI POSISI
    res_freq = "".join([Counter([d[i] for d in data_4d]).most_common(1)[0][0] for i in range(4)])
    
    # 2. RUMUS GAP ANALYSIS (ANGKA SEMBUNYI)
    all_str_15 = "".join(data_4d[:15])
    missing = [str(i) for i in range(10) if str(i) not in all_str_15]
    res_gap = missing[0] if missing else Counter(all_str_15).most_common()[-1][0]
    
    # 3. RUMUS ZIGZAG (POLA LONCAT)
    n = [int(x) for x in data_4d[0]]
    zigzag_rows = [[(n[0]-i)%10, (n[1]-i)%10, (n[2]+i)%10, (n[3]+i)%10] for i in range(6)]
    res_zigzag = f"{zigzag_rows[2][0]}{zigzag_rows[1][1]}{zigzag_rows[3][2]}{zigzag_rows[5][3]}"
    
    # 4. RUMUS MIRROR (INDEX/BAYANGAN)
    index_map = {'0':'5', '1':'6', '2':'7', '3':'8', '4':'9', '5':'0', '6':'1', '7':'2', '8':'3', '9':'4'}
    res_mirror = "".join([index_map.get(x, x) for x in data_4d[0]])

    # --- TAMPILAN INTERFACE ---
    tab1, tab2, tab3, tab4 = st.tabs(["🎯 KONSENSUS AKHIR AI", "🔬 HASIL & DETAIL RUMUS", "🛠️ TOOLS GENERATOR", "🌐 INFO SISTEM"])

    with tab1:
        st.subheader("🏆 Prediksi Gabungan AI")
        ai_final = res_freq[0] + res_freq[1] + res_zigzag[2] + res_gap
        col1, col2, col3 = st.columns(3)
        col1.metric("4D UTAMA", ai_final)
        col2.metric("3D CADANGAN", ai_final[1:])
        col3.metric("2D REKOMENDASI", ai_final[2:])
        st.info(f"💡 **Analisis Singkat:** Angka `{ai_final}` dipilih setelah AI menyaring hasil dari 4 rumus murni di bawah ini.")

    with tab2:
        st.subheader("🔬 Audit Transparan: Hasil & Logika Rumus")
        st.write("Berikut adalah hasil perhitungan dari setiap rumus yang ditambahkan ke sistem:")
        
        # Grid untuk menampilkan hasil tiap rumus dan penjelasannya
        col_r1, col_r2 = st.columns(2)
        
        with col_r1:
            st.success(f"### 📊 Rumus Frekuensi\n**HASIL: {res_freq}**")
            st.write("**Penjelasan Detail:** Rumus ini bekerja dengan membedah histori dan menghitung digit mana yang paling dominan di setiap posisi (As, Kop, Kepala, Ekor).")
            st.caption("Logika: Angka yang sering muncul cenderung memiliki ritme yang stabil di mesin.")
            
            st.warning(f"### 🔍 Rumus Gap Analysis\n**HASIL: {res_gap}xxx**")
            st.write("**Penjelasan Detail:** Mencari angka yang 'hilang' atau tidak muncul sama sekali dalam 15-20 periode terakhir.")
            st.caption("Logika: Menurut hukum probabilitas, angka yang lama vakum memiliki tekanan tinggi untuk segera keluar.")

        with col_r2:
            st.info(f"### 📐 Rumus Zigzag Engine\n**HASIL: {res_zigzag}**")
            st.write("**Penjelasan Detail:** Menghitung pergerakan naik-turun angka dari hasil terakhir (v8.5). Menggunakan baris koordinat 2-1-3-5.")
            st.caption("Logika: Menangkap pola pergeseran angka yang tidak statis dan bersifat dinamis.")
            
            st.error(f"### 🪞 Rumus Mirror (Index)\n**HASIL: {res_mirror}**")
            st.write("**Penjelasan Detail:** Mengonversi angka terakhir menggunakan tabel mistik/index (v8.0).")
            st.caption("Logika: Seringkali mesin mengeluarkan angka 'bayangan' atau lawan dari angka kemarin.")

    with tab3:
        st.subheader("🛠️ Tools Generator (BBFS & Tarung)")
        bbfs = sorted(list(set(ai_final + res_freq[:2])))
        st.code(f"BBFS SET: {', '.join(bbfs)}", language="text")
        st.write(f"**Angka Tarung 2D:** {res_freq[2:]} VS {res_gap}{res_zigzag[3]}")

    with tab4:
        st.write(f"**WiFi:** {SystemInfo.WIFI}")
        st.write(f"**Peta Server:** [Klik Maps]({SystemInfo.MAPS})")
        st.divider()
        st.write("**FAQ Lengkap:**")
        for f in SystemInfo.FAQ: st.write(f)

    # DOWNLOAD LOG
    csv = pd.DataFrame(data_4d).to_csv(index=False).encode('utf-8')
    st.download_button("📥 Unduh Laporan v13.5", csv, "architect_v135.csv", "text/csv")

else:
    st.info("👋 Selamat Datang di v13.5. Masukkan histori angka Anda untuk melihat semua rumus bekerja secara transparan.")
