import streamlit as st

st.set_page_config(
    page_title = "Matematika Geometri",
    page_icon = ":trophy:"
)

with st.sidebar:
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("logo.png.jpeg")
    st.title("Bangun Datar")
    pilihan = st.selectbox("Pilihan Bangun Datar", ["Persegi", "Persegi Panjang", "Lingkaran", "Segitiga", "Jajar Genjang"])
    st.caption("Dibuat dengan :heart: oleh **Geisha Fauziyah**")

match pilihan:
    case "Persegi":
        st.title("Persegi")
        st.markdown("Menghitung `luas` dan `keliling` persegi")
        sisi = st.number_input("Masukkan sisi")
        if st.button("Hitung", type="primary"):
            luas = sisi * sisi
            keliling = 4 * sisi
            st.success(f"Luas persegi adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            st.balloons()
    case "Persegi Panjang":
        st.title("Persegi Panjang")
        st.markdown("Menghitung `luas` dan `keliling` persegi panjang")
        panjang = st.number_input("Masukkan Panjang")
        lebar = st.number_input("Masukkan Lebar")
        if st.button("Hitung", type="primary"):
            luas = panjang * lebar
            keliling = 2 * (panjang + lebar)
            st.success(f"luas persegi panjang adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            st.balloons()
    case "Lingkaran":
        st.title("Lingkaran")
        st.markdown("Menghitung `luas` dan `keliling` lingkaran")
        jarijari = st.number_input("Masukkan jari-jari")
        if st.button("Hitung", type="primary"):
            luas = 3.14 * jarijari * jarijari
            keliling = 2 * 3.14 * jarijari
            st.success(f"luas lingkaran adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            st.balloons()
    case "Segitiga":
        st.title("Segitiga")
        st.markdown("Menghitung `luas` dan `keliling` segitiga")
        alas = st.number_input("Masukkan alas")
        tinggi = st.number_input("Masukkan tinggi")
        sisi_a = st.number_input("Masukkan sisi A (alas)")
        sisi_b = st.number_input("Masukkan sisi B")
        sisi_c = st.number_input("Masukkan sisi C")
        if st.button("Hitung", type="primary"):
            luas = 0.5 * alas * tinggi
            keliling = sisi_a + sisi_b + sisi_c
            st.success(f"luas segitiga adalah {luas:.2f} kelilingnya adalah {keliling:.2f}")
            st.snow()
    case "Jajar Genjang":
        st.title("Jajar Genjang")
        st.markdown("Menghitung `luas` dan `keliling` Jajar Genjang")
        alas = st.number_input("Masukkan alas")
        tinggi = st.number_input("Masukkan tinggi")
        miring = st.number_input("Masukkan miring")
        if st.button("Hitung", type="primary"):
            luas = alas * tinggi
            keliling = 0.5 * (alas + miring)
            st.success(f"luas jajar genjang adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            st.snow()
    case _ :
        st.error("Terjadi Kesalahan")