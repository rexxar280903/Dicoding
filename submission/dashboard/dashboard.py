import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
def load_data():
    return pd.read_csv("hour.csv")

data = load_data()

# Sidebar inputs
st.sidebar.title("Filter Data")
selected_variable = st.sidebar.selectbox("Pilih Variabel untuk Visualisasi:", ["windspeed", "registered", "cnt"])

time_range = st.sidebar.slider("Pilih Rentang Instant:", int(data["instant"].min()), int(data["instant"].max()), (int(data["instant"].min()), int(data["instant"].max())))

selected_weather = st.sidebar.multiselect("Filter Kondisi Cuaca:", options=data["weathersit"].unique(), default=data["weathersit"].unique())

# Apply filters
filtered_data = data[(data["instant"] >= time_range[0]) & (data["instant"] <= time_range[1]) & (data["weathersit"].isin(selected_weather))]

# Main dashboard
st.title("Dashboard Visualisasi Data")
st.write("Data yang Ditampilkan:", filtered_data.head())

# Plot Histogram
fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(filtered_data[selected_variable], kde=True, bins=30, ax=ax)
ax.set_title(f"Distribusi {selected_variable}")
st.pyplot(fig)

# Analisis Penyewaan Sepeda berdasarkan Musim
st.subheader("Pola Penyewaan Sepeda Berdasarkan Musim")
st.sidebar.subheader("Filter Musim")
selected_season = st.sidebar.multiselect("Pilih Musim:", options=data["season"].unique(), default=data["season"].unique())
season_data = data[data["season"].isin(selected_season)]

fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(x="season", y="cnt", data=season_data, ax=ax)
ax.set_title("Penyewaan Sepeda Berdasarkan Musim")
st.pyplot(fig)

# Analisis Penyewaan Sepeda pada Hari Libur vs Hari Kerja
st.subheader("Perbandingan Penyewaan Sepeda antara Hari Libur dan Hari Kerja")
st.sidebar.subheader("Filter Hari Libur")
selected_holiday = st.sidebar.radio("Pilih Tipe Hari:", [0, 1], format_func=lambda x: "Hari Kerja" if x == 0 else "Hari Libur")
holiday_data = data[data["holiday"] == selected_holiday]

fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(holiday_data["cnt"], kde=True, bins=30, ax=ax)
ax.set_title(f"Distribusi Penyewaan Sepeda pada {'Hari Kerja' if selected_holiday == 0 else 'Hari Libur'}")
st.pyplot(fig)