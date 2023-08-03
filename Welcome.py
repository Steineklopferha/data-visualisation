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

ef my_plot(el_x, el_y, filename):
    dfe = pd.read_csv(filename)
    plt.scatter(dfe[el_x]/10000, dfe[el_y]/10000) # /10000 wechslt von wt-ppm to wt-%
    plt.xlabel(el_x +  'wt%')
    plt.ylabel(el_y +  'wt%')
    return plt.show()

my_plot(x_axis, y_axis, location)
