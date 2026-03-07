import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter

# --- KONFIGURASI SISTEM (Audit: WiFi, Sosmed, Maps, FAQ v9.1 - TETAP LENGKAP) ---
class SystemInfo:
    WIFI = "📶 FREE_WIFI_2026_V9.1_AUDIT_MODE"
    SOCIAL = ["@Analyst_AI", "@Pakar_Angka_V9"]
    MAPS = "http://google.com/maps"
    FAQ = [
        "1. Kenapa angka setiap rumus dimunculkan? Agar Anda bisa memilih rumus mana yang paling akurat hari ini.",
        "2. Apa itu Angka Sembunyi? Angka yang paling lama tidak keluar (Gap Analysis).",
        "3. Apa itu Angka Bayangan? Hasil konversi Index/Mistik dari angka terakhir.",
        "4. WiFi & Maps? Selalu tersedia di Tab INFO SISTEM untuk akses Anda.",
        "5. Update v9.1: Menampilkan semua hasil rumus secara transparan tanpa ada yang disembunyikan."
    ]

# --- PENGATURAN LAYAR ---
st.set_page_config(page_title="Pakar Angka v9.1", layout="wide")
st.title("🤖 Pakar Angka v9.1 (Audit Transparan)")
st.caption("Semua rumus dari v8.0 sampai v9.1 dimunculkan hasilnya secara detail.")
st.markdown("---")

# --- INPUT DATA (SIDEBAR) ---
st.sidebar.header("📥 Input Data Histori")
raw_input = st.sidebar.text_area("Tempel Histori (Terbaru di atas):", height=250, placeholder="6395\n7554")
data_4d = [x.strip() for x in raw_input.split('\n') if len(x.strip()) == 4 and x.strip().isdigit()]

# Tabel Dasar (Index & Mistik) - Fitur v8.0 yang tetap dijaga
index_map = {'0':'5', '1':'6', '2':'7', '3':'8', '4':'9', '5':'0', '6':'1', '7':'2', '8':'3', '9':'4'}

if data_4d:
    # --- [PROSES SEMUA RUMUS - TIDAK ADA YANG DIHAPUS] ---
    
    # 1. RUMUS FREKUENSI (v8.1)
    res_frequent = "".join([Counter([d[i] for d in data_4d]).most_common(1)[0][0] for i in range(4)])
    
    # 2. RUMUS ANGKA SEMBUNYI / GAP (v8.4)
    all_recent = "".join(data_4d[:8])
    missing = [str(i) for i in range(10) if str(i) not in all_recent]
    res_gap = missing[0] if missing else data_4d[0][0]

    # 3. RUMUS BAYANGAN / INDEX (v8.0 & v8.7)
    terbaru = data_4d[0]
    res_index = "".join([index_map.get(x, x) for x in terbaru])

    # 4. RUMUS ZIGZAG / POLA LONCAT (v8.5)
    n = [int(x) for x in terbaru]
    zigzag_rows = [[(n[0]-i)%10, (n[1]-i)%10, (n[2]+i)%10, (n[3]+i)%10] for i in range(6)]
    res_zigzag = f"{zigzag_rows[2][0]}{zigzag_rows[1][1]}{zigzag_rows[3][2]}{zigzag_rows[5][3]}"

    # --- KONSENSUS AKHIR (SKOR KEYAKINAN v8.9) ---
    final_digits = []
    # Gabungkan semua hasil rumus untuk dicarikan angka terkuat
    semua_hasil = [res_frequent, res_zigzag, res_index, f"{res_gap}{res_gap}{res_gap}{res_gap}"]
    total_poin = 0
    for i in range(4):
        pool = [r[i] for r in semua_hasil]
        pemenang, jumlah = Counter(pool).most_common(1)[0]
        final_digits.append(pemenang)
        total_poin += jumlah
    
    hasil_final = "".join(final_digits)
    skor_yakin = int((total_poin / 16) * 100)

    # --- TAMPILAN TAB (AUDIT TRANSPARAN) ---
    t1, t2, t3, t4 = st.tabs(["🏆 HASIL AKHIR", "🔬 PERBANDINGAN RUMUS", "📐 TABEL ZIGZAG", "🌐 INFO SISTEM"])

    with t1:
        st.subheader("🎯 Prediksi Terkuat (Konsensus)")
        col_hasil, col_skor = st.columns([2, 1])
        with col_hasil:
            st.metric("ANGKA JADI (4D)", hasil_final)
            st.write(f"**Saran 2D Belakang:** `{hasil_final[2:]}` atau Cadangan `{res_index[2:]}`")
        with col_skor:
            st.metric("Skor Keyakinan", f"{skor_yakin}%")
            st.progress(skor_yakin / 100)
        
        st.info("💡 Angka Jadi di atas didapat dari hasil penggabungan semua rumus di bawah ini.")

    with t2:
        st.subheader("🔬 Detail Angka dari Setiap Rumus")
        st.write("Berikut adalah hasil murni dari masing-masing rumus tanpa campuran:")
        
        # Menampilkan hasil setiap rumus dalam kotak (Metric)
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Rumus Frekuensi", res_frequent, help="Angka yang paling sering muncul di histori")
        c2.metric("Rumus Zigzag", res_zigzag, help="Angka berdasarkan pola langkah loncat")
        c3.metric("Rumus Bayangan", res_index, help="Hasil konversi Index dari angka terakhir")
        c4.metric("Angka Sembunyi", f"{res_gap}xxx", help="Angka yang paling lama tidak keluar")

        st.divider()
        st.write("### 📖 Penjelasan Detail:")
        st.markdown(f"""
        * **Rumus Frekuensi:** Melihat posisi `{res_frequent}` sebagai angka yang paling mendominasi histori Anda.
        * **Rumus Zigzag:** Menghitung langkah dari `{terbaru}` sehingga muncul angka `{res_zigzag}`.
        * **Rumus Bayangan (Index):** Mengubah `{terbaru}` menjadi lawan angkanya yaitu `{res_index}`.
        * **Angka Sembunyi (Gap):** Angka **{res_gap}** adalah angka yang benar-benar hilang dari 8 hari terakhir. Sangat kuat untuk posisi AS.
        """)

    with t3:
        st.subheader("📐 Tabel Perhitungan Zigzag (v8.5)")
        df_zigzag = pd.DataFrame(zigzag_rows, columns=["AS (-)", "KOP (-)", "KEPALA (+)", "EKOR (+)"])
        st.table(df_zigzag)
        st.write(f"**Jalur yang diambil:** Baris 3, 2, 4, dan 6 (Hasil: `{res_zigzag}`)")

    with t4:
        st.write(f"**Status WiFi:** {SystemInfo.WIFI}")
        st.write(f"**Titik Maps:** [Lokasi Server]({SystemInfo.MAPS})")
        st.write(f"**Sosmed:** {', '.join(SystemInfo.SOCIAL)}")
        st.divider()
        st.write("**FAQ Terurut (v9.1):**")
        for item in SystemInfo.FAQ:
            st.write(item)

    # TOMBOL DOWNLOAD (Fitur Kesayangan Anda agar data tidak hilang)
    csv = pd.DataFrame(data_4d).to_csv(index=False).encode('utf-8')
    st.download_button("📥 Simpan Histori ke CSV", csv, "histori_analisis.csv", "text/csv")

else:
    st.info("👋 Sistem v9.1 Siap. Silakan masukkan angka histori Anda di sebelah kiri.")
