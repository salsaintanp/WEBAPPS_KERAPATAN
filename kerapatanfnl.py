# library yang digunakan

import streamlit as st
import requests
import pandas as pd
import time

from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

# Membuat Option menu pada tampilan

with st.sidebar :
    selected = option_menu (
       menu_title='Main Menu',
       options=['Halaman Utama','Kerapatan Curah','Kerapatan Absolut','Kerapatan Relatif', 'Tabel Kerapatan Air' ] )
    
# Halaman Utama Homescreen

if selected == 'Halaman Utama':
    st.markdown("<h1 style='text-align: center; color: red;'>APLIKASI PERHITUNGAN KERAPATAN</h1>", unsafe_allow_html=True)
    st.markdown('----')

    #Menampilkan animasi pada homescreen
    
    def load_lottie_url(url:str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_animation_1 = 'https://assets6.lottiefiles.com/packages/lf20_hgjskqs0.json'
    lottie_anime_json = load_lottie_url(lottie_animation_1)
    st_lottie(lottie_anime_json, key = 'hello')
    
    st.markdown("<h5 style='text-align: center; color: black;'> Aplikasi yang dapat membantu anda untuk menghitung kerapatan curah, kerapatan absolut, dan kerapatan relatif. </h5>", unsafe_allow_html=True)
    
    #Menampilkan informasi seputar perbedaan kerapatan curah, absolut, relatif
    
    col1, col2, col3, = st.columns([1,2,1])
    col1.markdown(' # Kerapatan Curah')
    col1.markdown (':green[Kerapatan Curah] adalah bobot bahan padat berbentuk butiran dibagi volume curah yaitu volume bahan dalam bentuk tercurah seperti beras pada takaran .')
    col2.markdown("<h1 style='text-align: center; color:green;'>Kerapatan Absolut </h1>", unsafe_allow_html=True)
    col2.markdown(':green[Kerapatan Absolut] adalah bobot bahan dibagi volume nyata bahan. Untuk benda yang bersifat curah, volume nyata adalah volume curah dikurangi volume udara di antara butiran-butiran bahan. Volume celah-celah butiran ini bisa diketahui dengan cara menambahkan cairan (yang akan mengisi celah-celah butiran) yang tidak bereaksi (diserap, diresapatau membentuk ikatan) dengan bahan.')
    col3.markdown(' # Kerapatan Relatif ')
    col3.markdown(':green[Kerapatan Relatif] perbandingan kerapatan bahan dengan kerapatan air pada temperatur dan tekanan yang sama.')

# Halaman Perhitungan Kerapatan Curah

if selected == 'Kerapatan Curah':
    st.markdown("<h3 style='text-align: center; color:red ;'> PERHITUNGAN KERAPATAN CURAH </h3>", unsafe_allow_html=True)
    st.markdown('----')
    
    # Input

    Bobot_gelas_kosong = st.number_input(
        "Masukkan Bobot Gelas kosong (g)",
        step=1e-6,
        format="%.4f")                                
    st.write(f':blue[Bobot Gelas kosong adalah ] { Bobot_gelas_kosong} gram ')
    
    Bobot_gelas_sampel = st.number_input(
        "Masukkan Bobot gelas yang Berisi sampel (g)",
        step=1e-6,
        format="%.4f")
    st.write(f':blue[Bobot Gelas berisi sampel adalah ] { Bobot_gelas_sampel} gram ')
    
    Volume_curah = st.number_input("Masukkan Volume curah(mL)")
    st.write(f':blue[Volume curah adalah ] { Volume_curah} mL')
    
    #Tombol Hasil Perhitungan
    
    tombol = st.button('Lihat hasil perhitungan')
    with st.spinner('Memproses hasil...'):
        time.sleep(2)
        if tombol:
            nilai_Kerapatan = ((Bobot_gelas_sampel) - (Bobot_gelas_kosong)) /(Volume_curah)
            st.success(f"Nilai Kerapatan Absolut adalah {nilai_Kerapatan} g/mL ")
   
  
# Halaman Perhitungan Kerapatan Absolut

if selected == 'Kerapatan Absolut':
    st.markdown("<h3 style='text-align: center; color:red ;'> PERHITUNGAN KERAPATAN ABSOLUT </h3>", unsafe_allow_html=True)
    st.markdown('----')
    
    # Input
    Volume_air_awal = st.number_input("Masukkan Volume Awal Air (mL)")
    st.write(f':blue[Volume awal air adalah ] { Volume_air_awal} mL ')
    
    Bobot_gelas_air = st.number_input(
        "Masukkan Bobot Gelas yang Berisi Air (g)",
        step=1e-6,
        format="%.4f")
    st.write(f':blue[Bobot Gelas yang berisi air adalah ] { Bobot_gelas_air} gram ')
    
    
    Volume_air_akhir = st.number_input("Masukkan Volume Akhir Air(mL)")
    st.write(f':blue[Volume akhir air adalah ] { Volume_air_akhir} mL')
    
    Bobot_gelas_air_Sampel = st.number_input(
        "Masukkan Bobot gelas yang Berisi Air dan Sampel (g)",
        step=1e-6,
        format="%.4f")
    st.write(f':blue[Bobot gelas yang berisi air dan sampel adalah ] { Bobot_gelas_air_Sampel} gram ')
    
    #Tombol Hasil Perhitungan
    
    tombol = st.button('Lihat hasil perhitungan')
    with st.spinner('Memproses hasil...'):
        time.sleep(2)
        if tombol:
            nilai_Kerapatan = ((Bobot_gelas_air_Sampel) - (Bobot_gelas_air)) /((Volume_air_akhir) - (Volume_air_awal))
            st.success(f"Nilai Kerapatan Absolut adalah {nilai_Kerapatan} g/mL ")

    
# Halaman Perhitungan Kerapatan Relatif

if selected == 'Kerapatan Relatif':
    st.markdown("<h3 style='text-align: center; color:red ;'> PERHITUNGAN KERAPATAN RELATIF </h3>", unsafe_allow_html=True)
    st.markdown('----')
    
    #Input
    
    Kerapatan_absolut = st.number_input("Masukkan Kerapatan Absolut (g/mL) ")
    st.write(f':blue[Kerapatan absolut adalah ] {Kerapatan_absolut} g/mL ')
    
    Kerapatan_air = st.number_input("Masukkan kerapatan air pada temperatur dan tekanan yang sama (g/mL)")
    st.info('Kerapatan bisa dilihat pada pilihan menu **Tabel Kerapatan air**', icon="ℹ️")
    st.write(f':blue[Kerapatan air pada temperatur dan tekanan yang sama adalah] {Kerapatan_air} g/mL')
    
    #Tombol Hasil Perhitungan
    
    tombol = st.button('Lihat hasil perhitungan')
    with st.spinner('Memproses hasil...'):
        time.sleep(2)
        if tombol:
            nilai_Kerapatan = (Kerapatan_absolut) /(Kerapatan_air)
            st.success(f"Nilai Kerapatan Absolut adalah {nilai_Kerapatan}  ")
            
# Menampilkan Tabel Kerapatan Air

if selected == 'Tabel Kerapatan Air':
    st.markdown("<h2 style='text-align: center; color: red;'> Tabel Kerapatan air</h2>", unsafe_allow_html=True)
    st.markdown('----')
    def load_data():
        return pd.DataFrame(
              {
                  "Temperatur ": [20,21,22,23,24,25,26,27,27.5,28,29,30,31,32,33,34,35,36,37,38,39,40],
                  "Kerapatan air ":[0.9982,0.9980,0.9978,0.9976,0.9973,0.9971,0.9968,0.9965,0.9964,0.9963,0.9960,0.9957,0.9954,0.9951,0.9947,0.9944,0.9941,0.9937,0.9934,0.9930,0.9926,0.9922],
        }
    )
    st.checkbox("Tampilkan tabel dengan format lebar", value=False, key="use_container_width")
    df = load_data()
    st.dataframe(df, use_container_width=st.session_state.use_container_width)
    