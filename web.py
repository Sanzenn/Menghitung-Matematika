import streamlit as st
from streamlit_option_menu import option_menu

# navigasi sidebar
with st.sidebar :
    selected = option_menu('Hitung Luas', 
        ['Hitung Luas Persegi Panjang',
          'Hitung Luas Segitiga'], 
     default_index=0)

    # halaman hitung luas persegi panjang
     
if (selected == 'Hitung Luas Persegi Panjang') :
      st.title('Hitung Luas Persegi Panjang')
      panjang =st.number_input ("Masukkan Nilai Panjang",0)
      lebar =st.number_input ("Masukkan Nilai Lebar",0)
      hitung =st.button("Hitung Luas")

      if hitung :
         luas = panjang * lebar
         st.write ("Luas Persegi Panjang Adalah = ", luas)
         st.success(f"Luas Persegi Panjang Adalah ={luas}")
    


if(selected == 'Hitung Luas Segitiga'):
    st.title('Hitung Luas Segitiga')

    alas =st.slider("Masukkan Nilai Alas",0,100)
    tinggi =st.slider("Masukkan Nilai Tinggi",0,100)
    hitung =st.button ("Hitung Luas")
            
    if hitung :
       luas = 0.5 * alas * tinggi
       st.success(f"Luas Segitiga Adalah = {luas}")