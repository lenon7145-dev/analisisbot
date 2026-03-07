import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter

# --- SISTEM KONFIGURASI (Audit: WiFi, Sosmed, Maps, FAQ v9.0) ---
class SystemInfo:
    WIFI = "📶 FREE_WIFI_2026_V9.0_INDONESIA"
    SOCIAL = ["@Analyst_AI", "@Pakar_Angka"]
    MAPS = "http://google.com/maps"
    FAQ = [
        "1. Skor Keyakinan? Menunjukkan seberapa kompak semua rumus setuju pada angka tersebut.",
        "2. Apa itu Angka Bayangan? Angka lawan (Mistik/Index) yang sering muncul bergantian.",
        "3. Apa itu Angka Sembunyi? Angka yang sudah lama tidak keluar dan berpotensi muncul.",
        "4. Cara Pakai? Masukkan hasil terakhir di kotak kiri, lalu baca penjelasan di tiap tab.",
        "5. Tip: Perhatikan 'Angka Kuat' di Tab Analisis Detail untuk pasangan 2D."
    ]

# --- UI SETTINGS ---
st.set_page_config(page_title="Pakar Angka v9.0", layout="wide")
st.title("🤖 Pakar Angka v9.0 (Edisi Penjelasan Detail)")
st.caption("Versi Bahasa Indonesia: Lebih Mudah Dimengerti & Transparan")
st.markdown("---")

# --- SIDEBAR INPUT ---
st.sidebar.header("📥 Masukkan Data")
raw_input = st.sidebar.text_area("Tempel Histori (Angka terbaru di paling atas):", height=250, placeholder="Contoh:\n6395\n7554")
data_4d = [x.strip() for x in raw_input.split('\n') if len(x.strip()) == 4 and x.strip().isdigit()]

# Tabel Dasar Penjelas
index_map = {'0':'5', '1':'6', '2':'7', '3':'8', '4':'9', '5':'0', '6':'1', '7':'2', '8':'3', '9':'4'}
mistik_map = {'1':'0', '2':'5', '3':'8', '4':'7', '6':'9', '0':'1', '5':'2', '8':'3', '7':'4', '9':'6'}

if data_4d:
    # --- 1. PROSES RUMUS 1: FREKUENSI (Angka Paling Sering) ---
    res_frequent = "".join([Counter([d[i] for d in data_4d]).most_common(1)[0][0] for i in range(4)])
    
    # --- 2. PROSES RUMUS 2: GAP (Angka Sembunyi) ---
    all_recent = "".join(data_4d[:8])
    missing = [str(i) for i in range(10) if str(i) not in all_recent]
    res_sembunyi = missing[0] if missing else data_4d[0][0]

    # --- 3. PROSES RUMUS 3: BAYANGAN (Index/Mistik) ---
    terbaru = data_4d[0]
    res_bayangan = "".join([index_map.get(x, x) for x in terbaru])

    # --- 4. PROSES RUMUS 4: ZIGZAG (Pola Loncat) ---
    n = [int(x) for x in terbaru]
    zigzag_rows = [[(n[0]-i)%10, (n[1]-i)%10, (n[2]+i)%10, (n[3]+i)%10] for i in range(6)]
    res_zigzag = f"{zigzag_rows[2][0]}{zigzag_rows[1][1]}{zigzag_rows[3][2]}{zigzag_rows[5][3]}"

    # --- 5. KONSENSUS & SKOR KEYAKINAN ---
    final_digits = []
    rumus_list = [res_frequent, res_zigzag, res_bayangan, f"{res_sembunyi}{res_sembunyi}{res_sembunyi}{res_sembunyi}"]
    setuju_poin = 0
    
    for i in range(4):
        pool = [r[i] for r in rumus_list]
        pemenang, jumlah = Counter(pool).most_common(1)[0]
        final_digits.append(pemenang)
        setuju_poin += jumlah

    hasil_akhir = "".join(final_digits)
    skor_yakin = int((setuju_poin / 16) * 100)

    # --- TAMPILAN UTAMA ---
    t1, t2, t3, t4 = st.tabs(["🏆 HASIL UTAMA", "🔬 DETAIL RUMUS", "📐 TABEL ZIGZAG", "🌐 INFO SISTEM"])

    with t1:
        st.subheader("🎯 Prediksi Angka Terbaik")
        c1, c2 = st.columns([2,1])
        with c1:
            st.metric("ANGKA JADI", hasil_akhir)
            st.write(f"**Penjelasan Singkat:** Angka ini dipilih karena paling banyak didukung oleh rumus statistik dan pola loncat (Zigzag).")
        with c2:
            st.metric("Tingkat Keyakinan", f"{skor_yakin}%")
            st.progress(skor_yakin / 100)
        
        st.divider()
        st.subheader("💡 Saran Strategi 2D")
        st.write(f"Pasangan angka belakang yang kuat: **{hasil_akhir[2:]}** atau cadangan **{res_bayangan[2:]}**.")

    with t2:
        st.subheader("🔬 Penjelasan Detail Setiap Rumus")
        
        st.markdown(f"""
        1. **Rumus Frekuensi (Paling Sering): `{res_frequent}`**
           - Cara kerja: Bot melihat dari semua histori, angka mana yang paling sering muncul di posisi AS, KOP, KEPALA, dan EKOR.
        
        2. **Rumus Angka Sembunyi (Gap): `{res_sembunyi}`**
           - Cara kerja: Bot mencari angka yang sudah 'libur' atau tidak keluar dalam 8 hari terakhir. Angka **{res_sembunyi}** adalah yang paling lama sembunyi.
        
        3. **Rumus Bayangan (Index): `{res_bayangan}`**
           - Cara kerja: Mengubah hasil terakhir `{terbaru}` ke angka lawannya (contoh: 0 jadi 5, 1 jadi 6). Ini sering terjadi di mesin undian.
        
        4. **Rumus Zigzag (Pola Loncat): `{res_zigzag}`**
           - Cara kerja: Menghitung pergerakan naik-turun angka dari hasil terakhir.
        """)

    with t3:
        st.subheader("📐 Tabel Pola Loncat (Zigzag)")
        st.table(pd.DataFrame(zigzag_rows, columns=["AS", "KOP", "KEPALA", "EKOR"]))
        st.info("Tabel ini menunjukkan kemungkinan angka jika polanya bergeser 1-5 langkah ke depan atau ke belakang.")

    with t4:
        st.write(f"**Koneksi:** {SystemInfo.WIFI}")
        st.write(f"**Lokasi Server:** [Klik di Sini]({SystemInfo.MAPS})")
        st.divider()
        st.write("**Tanya Jawab (FAQ):**")
        for f in SystemInfo.FAQ: st.write(f)

    # DOWNLOAD
    csv = pd.DataFrame(data_4d).to_csv(index=False).encode('utf-8')
    st.download_button("📥 Simpan Histori Saya", csv, "histori_angka.csv", "text/csv")
else:
    st.info("👋 Selamat Datang! Silakan masukkan list angka Anda di kotak sebelah kiri untuk mulai menghitung.")
