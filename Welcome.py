import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

file_name_list = []
for i in os.listdir():
  if i.endswith('csv'): 
    file_name_list.append(i)
  
st.write(file_name_list)

st.write('Hello World!')

df = pd.read_csv('Bastar Craton.csv')
st.dataframe(df)

el_list = df.columns.tolist()[27:80]
x_axis = st.selectbox('select element', el_list)
y_axis = st.selectbox('select element', el_list)

location = st.multiselect('select location', file_name_list,file_name_list[0])  #to be able to select multiple files


plt.scatter(df[x_axis]/10000, df[y_axis]/10000) # /10000 wechslt von wt-ppm to wt-%
plt.xlabel(x_axis +  'wt%')
plt.ylabel(y_axis +  'wt%')
plt.show()

