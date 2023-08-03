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
x_axis = st.selectbox('select element for x', el_list)
y_axis = st.selectbox('select element for y', el_list)

location = st.selectbox('select location', file_name_list)  #to be able to select multiple files (multiselect)

df = pd.read_csv(location)
p = figure(title=location + x_axis + ' vs. ' + y_axis, x_axis_label=x_axis + ' wt%', y_axis_label=y_axis + ' wt%')
p.circle(df[x_axis]/10000, df[y_axis]/10000, size=5, color='red')


st.bokeh_chart(p, use_container_width=True)
