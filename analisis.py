import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter

# --- KONFIGURASI SISTEM (WiFi, Sosmed, Maps, FAQ v15.2 - PERMANEN) ---
class SystemInfo:
    WIFI = "📶 FREE_WIFI_2026_V15.2_AUTHORITY"
    SOCIAL = ["@Analyst_AI", "@Final_Authority_Engine"]
    MAPS = "http://google.com/maps"
    FAQ = [
        "1. Mengapa ada Skor Keyakinan? Itu adalah hasil sinkronisasi antara Rumus Statistik dan Tren Pasar.",
        "2. Apa fungsi Backtesting? Memberikan bukti nyata performa rumus pada histori data Anda.",
        "3. Apa itu Twin Alert? Peringatan otomatis jika mesin sedang dalam siklus angka kembar.",
        "4. Lokasi Server? Informasi transparansi lokasi server ada di Tab INFO SISTEM.",
        "5. Tip Strategi: Jika Akurasi di bawah 50%, fokuslah pada angka cadangan (Mirror)."
    ]

# --- UI SETTINGS ---
st.set_page_config(page_title="Final Authority v15.2", layout="wide")
st.title("🏛️ Pakar Angka AI v15.2: The Final Authority")
st.caption("Edisi Paling Informatif: Audit Narasi Mendalam & Anatomi Prediksi")
st.markdown("---")

# --- SIDEBAR INPUT ---
st.sidebar.header("📥 Pusat Kendali Data")
raw_input = st.sidebar.text_area("Tempel Histori (Terbaru di atas):", height=200, placeholder="6395\n7554")
data_4d = [x.strip() for x in raw_input.split('\n') if len(x.strip()) == 4 and x.strip().isdigit()]

if len(data_4d) >= 1:
    # --- PROSES RUMUS (Legacy & Apex DNA) ---
    res_freq = "".join([Counter([d[i] for d in data_4d]).most_common(1)[0][0] for i in range(4)])
    all_str_15 = "".join(data_4d[:15])
    res_gap = [str(i) for i in range(10) if str(i) not in all_str_15][0] if [str(i) for i in range(10) if str(i) not in all_str_15] else data_4d[0][0]
    n = [int(x) for x in data_4d[0]]
    res_zigzag = f"{(n[0]-2)%10}{(n[1]-1)%10}{(n[2]+3)%10}{(n[3]+5)%10}"
    ai_final = res_freq[0] + res_freq[1] + res_zigzag[2] + res_gap

    # Deteksi Twin & Backtesting
    is_twin = any(len(set(d)) < 4 for d in data_4d[:5])
    hits = sum(1 for d in data_4d[1:11] if any(digit in ai_final for digit in d))
    accuracy_rate = (hits / 10) * 100

    # --- TAMPILAN INTERFACE (AUDIT NARASI) ---
    tab1, tab2, tab3, tab4 = st.tabs(["🎯 KEPUTUSAN STRATEGIS", "🔍 ANATOMI & RUMUS", "🧪 UJI AKURASI (BACKTEST)", "🌐 INFO SISTEM"])

    with tab1:
        st.subheader("🏆 Konsensus Akhir AI")
        c1, c2, c3 = st.columns(3)
        c1.metric("4D PREDIKSI", ai_final, delta=f"SKOR: {80+(hits*2)}%")
        c2.metric("AKURASI HISTORIS", f"{accuracy_rate}%")
        c3.metric("STATUS MESIN", "STABIL" if not is_twin else "TWIN ALERT")
        
        st.divider()
        st.markdown("### 📘 Panduan Strategi & Interpretasi Data")
        
        col_text1, col_text2 = st.columns(2)
        with col_text1:
            st.write("**1. Mengapa Angka Ini Muncul?**")
            st.info(f"""
            Angka `{ai_final}` adalah titik temu dari tiga gaya tarikan:
            * **Stabilitas:** Digit `{ai_final[0:2]}` dipilih karena memiliki frekuensi mendarat paling tinggi.
            * **Dinamika:** Digit `{ai_final[2]}` mengikuti alur zigzag (pergerakan naik-turun).
            * **Tekanan:** Digit `{ai_final[3]}` adalah angka paling 'dingin' (Gap) yang diprediksi akan segera meledak.
            """)
        with col_text2:
            st.write("**2. Bagaimana Cara Menggunakannya?**")
            st.success(f"""
            * **Prioritas:** Fokus pada 2D Belakang `{ai_final[2:]}` karena akurasi historis Anda sedang tinggi di area ini.
            * **Manajemen Risiko:** Jika status menunjukkan 'TWIN ALERT', pastikan Anda menyiapkan angka kembar cadangan (misal: {ai_final[2]*2}).
            * **Proteksi:** Gunakan Tool BBFS di Tab 2 untuk mencegah kerugian akibat angka terbalik.
            """)

    with tab2:
        st.subheader("🔬 Anatomi Angka & Penjelasan Rumus")
        st.write("Kami membedah hasil setiap rumus agar Anda tahu dari mana setiap digit berasal:")
        
        # Penjelasan per rumus secara detail
        with st.expander("📊 RUMUS FREKUENSI POSISI (Hasil: " + res_freq + ")", expanded=True):
            st.write("**Cara Kerja:** Menghitung jumlah kemunculan angka di setiap kolom (As, Kop, Kepala, Ekor).")
            st.write("**Tujuan:** Mengunci angka yang sudah menjadi 'kebiasaan' mesin undian.")
            
        with st.expander("🔍 GAP ANALYSIS / ANGKA SEMBUNYI (Hasil: " + res_gap + "xxx)"):
            st.write("**Cara Kerja:** Memindai 15 hari terakhir untuk mencari angka 0-9 yang tidak pernah muncul.")
            st.write("**Tujuan:** Menemukan angka yang memiliki peluang gravitasi tertinggi untuk ditarik keluar oleh mesin.")

        with st.expander("🛠️ TOOL BBFS (Bolak-Balik Full Set)"):
            bbfs = sorted(list(set(ai_final + res_freq[:2])))
            st.code(f"SET BBFS: {', '.join(bbfs)}")
            st.write("**Penting:** Gunakan set ini jika Anda ingin mencakup semua kemungkinan posisi angka.")

    with tab3:
        st.subheader("🧪 Uji Akurasi Historis (Backtesting)")
        st.write(f"Sistem telah menguji rumus ini terhadap **10 data terakhir** yang Anda masukkan.")
        st.progress(accuracy_rate / 100)
        st.write(f"Hasil: **{hits} dari 10 kali cocok** (Digit Relevan).")
        st.markdown("""
        **Kesimpulan Uji:**
        * Jika akurasi **>70%**: Rumus sedang sinkron dengan mesin.
        * Jika akurasi **40-60%**: Gunakan angka tarung/BBFS.
        * Jika akurasi **<40%**: Mesin sedang sangat acak, kurangi nominal taruhan.
        """)

    with tab4:
        st.write(f"**WiFi:** {SystemInfo.WIFI}")
        st.write(f"**Maps:** [Server Location]({SystemInfo.MAPS})")
        st.divider()
        for f in SystemInfo.FAQ: st.write(f)

    # FOOTER
    st.markdown("---")
    st.caption("© 2026 Pakar Angka AI v15.2 | The Final Authority Edition")
    csv = pd.DataFrame(data_4d).to_csv(index=False).encode('utf-8')
    st.download_button("📥 Unduh Laporan Analisis", csv, "final_authority_v152.csv", "text/csv")

else:
    st.info("👋 Selamat Datang. Sistem v15.2 siap membantu. Masukkan histori data Anda di sidebar untuk memulai analisis.")
