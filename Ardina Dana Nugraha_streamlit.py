import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv("hour_processed.csv", delimiter=",")

st.title('Dashboard Bike Sharing')
import streamlit as st


st.write(
    """
    Oleh: Ardina Dana Nugraha
    """
)

st.subheader('Total Pelanggan')
 
col1, col2 = st.columns(2)
 
with col1:
    user_casual = dataset['casual'].sum()
    st.metric("Casual user", value=user_casual)

with col2:
    user_reg = dataset['registered'].sum()
    st.metric("Registered user", value=user_reg)

    width = 0.35  # width of the bars

st.subheader('Total Pelanggan Berdasarkan Musim')
col1, col2, col3 = st.columns(3)
seas = dataset.groupby('season')['cnt'].sum().reset_index()
seas_cas = dataset.groupby('season')['casual'].sum().reset_index()
seas_reg = dataset.groupby('season')['registered'].sum().reset_index()

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(5, 5))
labels = ['Spring', 'Summer', 'Autumn', 'Winter']
sizes = seas['cnt']
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['red', 'orange', 'green', 'yellow'])

plt.title('Total Pelanggan Keseluruhan')

plt.show()

with col1:
    st.pyplot(fig)

fig, ax = plt.subplots(figsize=(5, 5))
labels = ['Spring', 'Summer', 'Autumn', 'Winter']
sizes = seas_cas['casual']
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['red', 'orange', 'green', 'yellow'])

plt.title('Total Pelanggan Casual')

plt.show()

with col2:
    st.pyplot(fig)

fig, ax = plt.subplots(figsize=(5, 5))
labels = ['Spring', 'Summer', 'Autumn', 'Winter']
sizes = seas_reg['registered']
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['red', 'orange', 'green', 'yellow'])

plt.title('Total Pelanggan Registered')

plt.show()

with col3:
    st.pyplot(fig)

st.subheader('Total Pelanggan Berdasarkan Bulan')

week_cas = dataset.groupby('weekday')['casual'].sum().reset_index()
week_reg = dataset.groupby('weekday')['registered'].sum().reset_index()

width = 0.35

fig, ax = plt.subplots(figsize=(10, 10))

c = ['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu']
ax.bar(c, week_cas['casual'], width, label='Casual User', color='blue')

ax.bar(c, week_reg['registered'], width, label='Registered User', color='red', bottom=week_cas['casual'])

ax.set_title('Stacked Bar Chart dari Pelanggan Casual dan Registered Berdasarkan Hari')
ax.set_xlabel('Hari')
ax.set_ylabel('Banyak Pelanggan')

ax.legend()

for i, value in enumerate(week_cas['casual']):
    plt.text(i - width / 2, value + 1, str(value), ha='center', va='bottom')

for i, value in enumerate(week_reg['registered']):
    plt.text(i + width / 2, week_cas['casual'][i] + value + 1, str(value), ha='center', va='bottom')

st.pyplot(fig)

st.subheader('Total Pelanggan Berdasarkan Tahun')
 
col1, col2 = st.columns(2)

yr0 = dataset[dataset['yr'] == 0]
yr1 = dataset[dataset['yr'] == 1]
a = yr0.groupby(['yr','mnth'])['cnt'].sum().reset_index()
a.sort_values(by='cnt', ascending=False)

b = yr1.groupby(['yr','mnth'])['cnt'].sum().reset_index()
b.sort_values(by='cnt', ascending=False)

c = a['cnt']
d = b['cnt']

persen = ((b['cnt']-a['cnt'])*100/a['cnt'])

with col1:
    persen_tertinggi = persen.max()
    percentage = persen_tertinggi
    persen_tertinggi = "{:.2f}%".format(percentage)
    persen_terendah = persen.min()
    percentage = persen_terendah
    persen_terendah = "{:.2f}%".format(percentage)
    st.metric("Kenaikan tertinggi", value=persen_tertinggi)

with col2:
    st.metric("Kenaikan terendah", value=persen_terendah)

    barWidth = 0.25
fig, ax = plt.subplots(figsize =(12, 8)) 
br1 = np.arange(len(c)) 
br2 = [x + barWidth for x in br1] 
br3 = [x + barWidth for x in br2] 
 
plt.bar(br1, c, color ='r', width = barWidth, 
        edgecolor ='grey', label ='2011') 
plt.bar(br2, d, color ='g', width = barWidth, 
        edgecolor ='grey', label ='2012') 
 
ax.set_title('Clustered Bar Chart Total Pelanggan berdasarkan Tahun')

plt.xlabel('Bulan', fontweight ='bold', fontsize = 15) 
plt.ylabel('Jumlah Pelanggan', fontweight ='bold', fontsize = 15) 
plt.xticks([r + barWidth for r in range(len(c))],['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember'])
#plt.xticks(a['mnth'])
 
plt.legend()
plt.show()
st.pyplot(fig)