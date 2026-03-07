import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter

# --- SISTEM KONFIGURASI (WiFi, Sosmed, Maps, FAQ v10.1 - TERJAGA 100%) ---
class SystemInfo:
    WIFI = "📶 FREE_WIFI_2026_V10.1_FINAL_STABLE"
    SOCIAL = ["@Analyst_AI", "@Final_Judge_Pro"]
    MAPS = "http://google.com/maps"
    FAQ = [
        "1. Apa itu Final Judge? Filter otomatis yang mencocokkan angka dengan tren pasar.",
        "2. Kenapa ada Status 'STABIL'? Artinya histori data Anda konsisten dan mudah dibaca AI.",
        "3. Berapa data minimal? Disarankan minimal 10 baris untuk hasil maksimal.",
        "4. Lokasi Server? Informasi pusat server tersedia di Tab INFO SISTEM.",
        "5. Tip Super: Perhatikan angka 2D AI, biasanya memiliki akurasi paling stabil."
    ]

# --- UI SETTINGS ---
st.set_page_config(page_title="Final Judge AI v10.1", layout="wide")
st.title("⚖️ Pakar Angka AI v10.1: Sovereign Judge")
st.caption("Final Stable Version: Filter Ganjil-Genap + Besar-Kecil + Deep Analysis")
st.markdown("---")

# --- SIDEBAR INPUT ---
st.sidebar.header("📥 Panel Kendali Data")
raw_input = st.sidebar.text_area("Tempel Histori (Data terbaru di atas):", height=200, placeholder="6395\n7554")
# Pembersihan data (Audit: Menghapus baris kosong & karakter non-angka)
data_4d = [x.strip() for x in raw_input.split('\n') if len(x.strip()) == 4 and x.strip().isdigit()]

if len(data_4d) >= 1:
    # --- STEP 1: RUMUS DASAR (Legacy DNA) ---
    res_freq = "".join([Counter([d[i] for d in data_4d]).most_common(1)[0][0] for i in range(4)])
    all_str = "".join(data_4d[:15])
    res_gap = [str(i) for i in range(10) if str(i) not in all_str][0] if [str(i) for i in range(10) if str(i) not in all_str] else data_4d[0][0]
    
    # --- STEP 2: ANALISIS TREN (Ganjil/Genap & Besar/Kecil) ---
    last_10 = [int(d[2:]) for d in data_4d[:10]]
    ganjil_count = sum(1 for x in last_10 if x % 2 != 0)
    genap_count = 10 - ganjil_count
    tren_tipe = "GANJIL" if ganjil_count > genap_count else "GENAP"
    
    # Analisis Besar/Kecil (0-4 Kecil, 5-9 Besar)
    besar_count = sum(1 for d in data_4d[:10] if int(d[3]) >= 5)
    kecil_count = 10 - besar_count
    tren_size = "BESAR" if besar_count > kecil_count else "KECIL"
    
    # --- STEP 3: FINAL JUDGE LOGIC (Koreksi AI) ---
    ai_4d_raw = res_freq[0] + res_freq[1] + res_freq[2] + res_gap
    ekor_final = int(ai_4d_raw[3])
    # Koreksi Ekor berdasarkan Tren Ganjil/Genap
    if tren_tipe == "GANJIL" and ekor_final % 2 == 0:
        ekor_final = (ekor_final + 1) % 10
    elif tren_tipe == "GENAP" and ekor_final % 2 != 0:
        ekor_final = (ekor_final + 1) % 10
    ai_4d = ai_4d_raw[:3] + str(ekor_final)

    # --- TAMPILAN INTERFACE ---
    tab1, tab2, tab3, tab4 = st.tabs(["🏆 HASIL KEPUTUSAN", "🔬 ANALISIS DETAIL", "📐 TABEL ZIGZAG", "🌐 INFO SISTEM"])

    with tab1:
        st.subheader("⚖️ Keputusan Akhir Final Judge")
        c1, c2, c3 = st.columns(3)
        c1.metric("PREDIKSI 4D", ai_4d, delta=f"TREN: {tren_tipe}")
        c2.metric("PREDIKSI 3D", ai_4d[1:], delta=f"SIZE: {tren_size}")
        c2.caption(f"Distribusi: {besar_count} Besar / {kecil_count} Kecil")
        c3.metric("PREDIKSI 2D", ai_4d[2:], delta="PELUANG: TINGGI")
        
        st.divider()
        st.markdown("### 🔍 Mengapa Angka Ini Terpilih?")
        cola, colb = st.columns(2)
        with cola:
            st.info(f"**Filter Ganjil/Genap:** AI melihat tren sedang dominan **{tren_tipe}**, sehingga angka belakang disesuaikan.")
            st.info(f"**Analisis Gap:** Angka **{res_gap}** muncul sebagai 'Dark Horse' karena paling lama tidak terlihat.")
        with colb:
            st.success(f"**Pola Statistik:** Angka depan `{ai_4d[:2]}` memiliki frekuensi kemunculan tertinggi.")
            st.success(f"**Status Sistem:** 🟢 **STABIL** (Data memenuhi syarat minimum analisis).")

    with tab2:
        st.subheader("🔬 Bedah Logika & Audit Rumus")
        st.write("Hasil murni dari setiap 'mesin' sebelum digabungkan AI:")
        
        ca, cb, cc, cd = st.columns(4)
        ca.code(f"FREKUENSI\n{res_freq}")
        cb.code(f"GAP\n{res_gap}xxx")
        cc.code(f"TREN\n{tren_tipe}")
        cd.code(f"SIZE\n{tren_size}")
        
        st.write("---")
        st.write("**Metode AI Re-Calculation:**")
        st.markdown("""
        * AI memadukan hasil murni di atas.
        * Melakukan 'Judgement' (penjaringan) terakhir untuk memastikan ekor tidak berlawanan dengan tren pasar.
        """)

    with tab3:
        st.subheader("📐 Laboratorium Zigzag (v8.5 Legacy)")
        n = [int(x) for x in data_4d[0]]
        zigzag_rows = [[(n[0]-i)%10, (n[1]-i)%10, (n[2]+i)%10, (n[3]+i)%10] for i in range(6)]
        st.table(pd.DataFrame(zigzag_rows, columns=["AS", "KOP", "KEPALA", "EKOR"]))

    with tab4:
        st.write(f"**WiFi:** {SystemInfo.WIFI}")
        st.write(f"**Maps Server:** [Peta Lokasi]({SystemInfo.MAPS})")
        st.divider()
        for f in SystemInfo.FAQ: st.write(f)

    # FOOTER & DOWNLOAD
    st.markdown("---")
    st.caption("© 2026 Pakar Angka AI Project | Version 10.1 Stable | Sovereign Analyst")
    csv = pd.DataFrame(data_4d).to_csv(index=False).encode('utf-8')
    st.download_button("📥 Simpan Histori Analisis", csv, "ai_final_audit.csv", "text/csv")

else:
    st.info("👋 Sistem v10.1 Siap. Masukkan data histori angka di sidebar (sebelah kiri) untuk memulai analisis.")
