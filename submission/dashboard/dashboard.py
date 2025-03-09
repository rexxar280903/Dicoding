import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
@st.cache_data
def load_data():
    data = pd.read_csv(r"hour.csv")
    return data

data = load_data()

# Main Dashboard
st.title("Dashboard Analisis Data")
st.write("### Ringkasan Data")
st.write(data.describe())

# Visualisasi Data
st.write("### Boxplot Kecepatan Angin")
fig1, ax1 = plt.subplots()
ax1.boxplot(data['windspeed'], whis=3)
st.pyplot(fig1)


st.title("Visualisasi Histogram Kecepatan Angin")

# Membuat histogram
fig, ax = plt.subplots()
ax.hist(data['windspeed'], bins=20, color='skyblue', edgecolor='black')
ax.set_xlabel("Kecepatan Angin")
ax.set_ylabel("Frekuensi")
ax.set_title("Distribusi Kecepatan Angin")
st.pyplot(fig)


st.title("Scatter Plot Kecepatan Angin")
# Membuat scatter plot
fig, ax = plt.subplots()
ax.scatter(range(len(data['windspeed'])), data['windspeed'], color='red', alpha=0.5)
ax.set_xlabel("Indeks Data")
ax.set_ylabel("Kecepatan Angin")
ax.set_title("Variasi Kecepatan Angin")
st.pyplot(fig)


# Sidebar
st.sidebar.title("Dashboard Filter")
date_filter = st.sidebar.date_input("Pilih Tanggal", pd.to_datetime("2011-01-01"))

# Main Dashboard
st.title("Dashboard Analisis Data")
st.write("### Ringkasan Data")
st.write(data.describe())

# Visualisasi Boxplot
st.write("### Boxplot Pengguna Terdaftar")
fig1, ax1 = plt.subplots()
ax1.boxplot(data['registered'])
st.pyplot(fig1)

# Visualisasi Histogram
st.write("### Histogram Pengguna Terdaftar")
fig2, ax2 = plt.subplots()
ax2.hist(data['registered'], bins=20, color='green', edgecolor='black')
st.pyplot(fig2)

# Visualisasi Scatter Plot
st.write("### Scatter Plot Pengguna Terdaftar")
fig3, ax3 = plt.subplots()
ax3.scatter(range(len(data['registered'])), data['registered'], color='blue', alpha=0.5)
st.pyplot(fig3)

# Visualisasi Line Chart
st.write("### Line Chart Jumlah 'cnt' berdasarkan 'instant'")
fig4, ax4 = plt.subplots(figsize=(18, 8))
ax4.plot(data['instant'], data['cnt'], color='b')
ax4.set_title("Line Chart Jumlah 'cnt' berdasarkan 'instant'")
ax4.set_xlabel("Instant")
ax4.set_ylabel("Count (cnt)")
st.pyplot(fig4)

# Visualisasi Bar Chart Berdasarkan Musim dan Tahun
st.write("### Jumlah Rental Sepeda Berdasarkan Musim dan Tahun")
season_rentals = data.groupby(['season', 'yr'])['cnt'].sum().unstack()
x = np.arange(len(season_rentals.index))
width = 0.4
fig5, ax5 = plt.subplots(figsize=(10, 8))
rects1 = ax5.bar(x - width/2, season_rentals[0], width, label="2011", color='royalblue')
rects2 = ax5.bar(x + width/2, season_rentals[1], width, label="2012", color='orange')
ax5.set_xticks(x)
ax5.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'], fontsize=12)
ax5.set_title('Jumlah Rental Sepeda Berdasarkan Musim dan Tahun')
ax5.set_xlabel('Musim')
ax5.set_ylabel('Total Rental Sepeda')
ax5.legend()
st.pyplot(fig5)

# Visualisasi Bar Chart Berdasarkan Cuaca dan Tahun
st.write("### Jumlah Rental Sepeda Berdasarkan Kondisi Cuaca dan Tahun")
weathershit_rentals = data.groupby(['weathersit','yr'])['cnt'].sum().unstack()
x = np.arange(len(weathershit_rentals.index))
fig6, ax6 = plt.subplots(figsize=(10, 8))
rects1 = ax6.bar(x - width/2, weathershit_rentals[0], width, label="2011", color='royalblue')
rects2 = ax6.bar(x + width/2, weathershit_rentals[1], width, label="2012", color='orange')
ax6.set_xticks(x)
ax6.set_xticklabels(['Clear', 'Mist', 'Light Snow', 'Heavy Rain'], fontsize=12)
ax6.set_title('Jumlah Rental Sepeda Berdasarkan Kondisi Cuaca dan Tahun')
ax6.set_xlabel('Kondisi Cuaca')
ax6.set_ylabel('Total Rental Sepeda')
ax6.legend()
st.pyplot(fig6)

# Visualisasi Bar Chart Berdasarkan Hari Kerja, Musim, dan Tahun
st.write("### Jumlah Rental Sepeda Berdasarkan Musim, Hari Kerja, dan Tahun")
grouped_data = data.groupby(["workingday", "season", "yr"])['cnt'].sum().unstack()
x = np.arange(len(grouped_data))
fig7, ax7 = plt.subplots(figsize=(12, 8))
rects1 = ax7.bar(x - width/2, grouped_data.loc[:, 0], width, label="2011", color='royalblue')
rects2 = ax7.bar(x + width/2, grouped_data.loc[:, 1], width, label="2012", color='orange')
season_labels = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
labels = [f"Workday {wd} - {season_labels[s]}" for wd, s in grouped_data.index]
ax7.set_xticks(x)
ax7.set_xticklabels(labels, rotation=45, ha="right", fontsize=12)
ax7.set_title('Jumlah Rental Sepeda Berdasarkan Musim, Hari Kerja, dan Tahun')
ax7.set_xlabel('Kombinasi Hari Kerja dan Musim')
ax7.set_ylabel('Total Rental Sepeda')
ax7.legend()
st.pyplot(fig7)

# Menampilkan Data Sample
st.write("### Data Sample")
st.write(data.head())
