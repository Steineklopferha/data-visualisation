import streamlit as st
import pandas as pd
import os
from bokeh.plotting import figure


file_name_list = []
for i in os.listdir():
  if i.endswith('csv'): 
    file_name_list.append(i)
  
st.write(file_name_list)

st.write('Hello World!')

df = pd.read_csv('Bastar Craton.csv')


el_list = df.columns.tolist()[27:80]
x_axis = st.selectbox('select element', el_list)
#y_axis = st.selectbox('select element', el_list)

location = st.selectbox('select location', file_name_list)  #to be able to select multiple files (multiselect)

df = pd.read_csv(location)
p = figure(x_axis_label='Mg wt%', y_axis_label='Si wt%')
p.star(df['Mg']/10000, df['Si']/10000, size=10, color='red')

st.bokeh_chart(p, use_container_width=True)
