import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
day_df = pd.read_csv("https://raw.githubusercontent.com/N421RMLU1315/Submission-Bike-Sharing-Dataset/main/day.csv")
hour_df = pd.read_csv("https://raw.githubusercontent.com/N421RMLU1315/Submission-Bike-Sharing-Dataset/main/hour.csv")

# Data Wrangling (Sesuaikan dengan proses cleaning data yang telah Anda lakukan)
day_df.season.replace((1, 2, 3, 4), ('Spring', 'Summer', 'Fall', 'Winter'), inplace=True)

# Sidebar
st.sidebar.title("Dashboard Menu")
selected_chart = st.sidebar.radio("Pilih Chart:", ["Pola Penggunaan Sepeda", "Korelasi Jam Puncak"])

# Main Content
st.title("Dashboard Analisis Data Sepeda")

# Chart 1: Pola Penggunaan Sepeda
if selected_chart == "Pola Penggunaan Sepeda":
    st.subheader("Pola Penggunaan Sepeda Selama Musim")
    
    # Visualisasi penggunaan sepeda berdasarkan bulan (point plot)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.pointplot(x='Month', y='cnt', data=day_df, ci=None, ax=ax)
    plt.title('Pola Penggunaan Sepeda Selama Musim')
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Peminjaman')
    st.pyplot(fig)

# Chart 2: Korelasi Jam Puncak
elif selected_chart == "Korelasi Jam Puncak":
    st.subheader("Korelasi Jam Puncak dan Jumlah Peminjaman Sepeda")
    
    # Visualisasi korelasi antara jam puncak dan jumlah peminjaman sepeda (bar chart)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='hr', y='cnt', data=hour_df, ci=None, ax=ax)
    plt.title('Korelasi Jam Puncak dan Jumlah Peminjaman Sepeda')
    plt.xlabel('Jam Puncak')
    plt.ylabel('Jumlah Peminjaman')
    st.pyplot(fig)
