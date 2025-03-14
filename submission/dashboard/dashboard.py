import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
@st.cache_data
def load_data():
    data = pd.read_csv(r"hour.csv")
    data['dteday'] = pd.to_datetime(data['dteday'])  # Konversi ke datetime
    return data

data = load_data()

# Mapping musim
season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}

# Sidebar untuk memilih musim
selected_season = st.sidebar.selectbox("Pilih Musim", ["Semua"] + list(season_mapping.values()))

# Filter data berdasarkan musim yang dipilih
if selected_season != "Semua":
    season_key = [k for k, v in season_mapping.items() if v == selected_season][0]
    filtered_data = data[data['season'] == season_key]
else:
    filtered_data = data  # Jika "Semua", tampilkan semua data

# Tampilkan hasil setelah filter
st.write("### Data setelah difilter berdasarkan musim:")
st.write(filtered_data)

# Contoh visualisasi setelah filter
st.write("### Histogram Pengguna Terdaftar Berdasarkan Musim")
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.hist(filtered_data['registered'], bins=20, color='green', edgecolor='black')
ax.set_xlabel("Jumlah Pengguna Terdaftar")
ax.set_ylabel("Frekuensi")
ax.set_title("Distribusi Pengguna Terdaftar Berdasarkan Musim")
st.pyplot(fig)
# Main Dashboard
st.title("Dashboard Analisis Data")
st.write("### Ringkasan Data")
st.write(data.describe())

# Visualisasi Data
def plot_histogram(column, title, xlabel, color):
    fig, ax = plt.subplots()
    ax.hist(data[column], bins=20, color=color, edgecolor='black')
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Frekuensi")
    ax.set_title(title)
    st.pyplot(fig)

# Histogram Kecepatan Angin
st.write("### Histogram Kecepatan Angin")
plot_histogram('windspeed', "Distribusi Kecepatan Angin", "Kecepatan Angin", 'skyblue')

# Scatter Plot Pengguna Terdaftar
st.write("### Scatter Plot Pengguna Terdaftar")
fig, ax = plt.subplots()
ax.scatter(range(len(data['registered'])), data['registered'], color='blue', alpha=0.5)
ax.set_xlabel("Indeks Data")
ax.set_ylabel("Jumlah Pengguna Terdaftar")
ax.set_title("Variasi Pengguna Terdaftar")
st.pyplot(fig)

# Line Chart Jumlah 'cnt' berdasarkan 'instant'
st.write("### Line Chart Jumlah 'cnt' berdasarkan 'instant'")
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(data['instant'], data['cnt'], color='b')
ax.set_title("Line Chart Jumlah 'cnt' berdasarkan 'instant'")
ax.set_xlabel("Instant")
ax.set_ylabel("Count (cnt)")
st.pyplot(fig)

# Bar Chart Berdasarkan Musim dan Tahun
st.write("### Jumlah Rental Sepeda Berdasarkan Musim dan Tahun")
season_rentals = data.groupby(['season', 'yr'])['cnt'].sum().unstack()
x = np.arange(len(season_rentals.index))
width = 0.4
fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, season_rentals[0], width, label="2011", color='royalblue')
rects2 = ax.bar(x + width/2, season_rentals[1], width, label="2012", color='orange')
ax.set_xticks(x)
ax.set_xticklabels([season_mapping[i] for i in season_rentals.index])
ax.set_title('Jumlah Rental Sepeda Berdasarkan Musim dan Tahun')
ax.set_xlabel('Musim')
ax.set_ylabel('Total Rental Sepeda')
ax.legend()
st.pyplot(fig)

# Menampilkan Data Sample
st.write("### Data Sample")
st.write(data.head())
