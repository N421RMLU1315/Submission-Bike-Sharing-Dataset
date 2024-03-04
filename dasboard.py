import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
day_df = pd.read_csv("https://raw.githubusercontent.com/N421RMLU1315/Submission-Bike-Sharing-Dataset/main/day.csv")
hour_df = pd.read_csv("https://raw.githubusercontent.com/N421RMLU1315/Submission-Bike-Sharing-Dataset/main/hour.csv")

# Sidebar
st.sidebar.title("Proyek Analisis Data - Bike Sharing")

# Adding Image from Google
image_url = "https://treelains.com/web/wp-content/uploads/2021/04/sepeda.jpg"
st.sidebar.image(image_url, caption="Gambar dari Google", use_column_width=True)

# Copyright Notice
st.sidebar.text("Copyright (c) Nazir M Lubis 2024")

# Page Selection
page = st.sidebar.radio("Pilih Halaman:", ["Visualisasi Penggunaan Sepeda", "Korelasi Jam Puncak", "Conclusion"])

# Main Content
st.title("Dashboard Analisis Data - Bike Sharing")

if page == "Visualisasi Penggunaan Sepeda":
    st.subheader("Pola Penggunaan Sepeda Berdasarkan Bulan")
    # Extract month from the 'dteday' column
    day_df['Month'] = pd.to_datetime(day_df['dteday']).dt.month
    chart = sns.pointplot(x='Month', y='cnt', data=day_df, ci=None)
    plt.title('Pola Penggunaan Sepeda Selama Musim')
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Peminjaman')
    st.pyplot(chart.figure)

    st.subheader("Pola Penggunaan Sepeda Berdasarkan Musim")
    # Stacked bar chart for bike usage based on season
    season_df = day_df.groupby(['Month', 'season'])['cnt'].sum().unstack()
    season_df.plot(kind='bar', stacked=True)
    plt.title('Pola Penggunaan Sepeda Berdasarkan Musim')
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Peminjaman')
    st.pyplot(plt.gcf())  # Get the current figure for Streamlit

elif page == "Korelasi Jam Puncak":
    st.subheader("Korelasi Jam Puncak dan Jumlah Peminjaman Sepeda")
    chart = sns.barplot(x='hr', y='cnt', data=hour_df, ci=None)
    plt.title('Korelasi Jam Puncak dan Jumlah Peminjaman Sepeda')
    plt.xlabel('Jam Puncak')
    plt.ylabel('Jumlah Peminjaman')
    st.pyplot(chart.figure)

elif page == "Conclusion":
    st.subheader("Kesimpulan Analisis Data Bike Sharing")
    st.markdown(
        """
        **Pertanyaan 1: Bagaimana Pola Penggunaan Sepeda Berubah Selama Musim Panas dan Musim Dingin?**

        Berdasarkan penjelasan pada diagram di atas, bisa disimpulkan bahwa peningkatan jumlah peminjaman terjadi pada musim panas yang dimulai dari 6 bulan pertama setiap tahunnya, dan penurunan jumlah peminjaman sepeda terjadi pada musim dingin yang terjadi di triwulan terakhir.

        **Pertanyaan 2: Apa Korelasi Antara Jam Puncak dan Jumlah Peminjaman Sepeda?**

        Berdasarkan pada diagram di atas, bisa disimpulkan bahwa terdapat korelasi antara jam puncak dan jumlah peminjaman sepeda. Korelasi ini bisa menjadi dasar untuk strategi peminjaman sepeda pada jam-jam tertentu. Jumlah peminjaman sepeda tertinggi terjadi di sore hari (jam 17-18) dan pagi hari (jam 8).
        """
    )
