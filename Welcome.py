import streamlit as st
import pandas as pd
import os
from bokeh.plotting import figure
import numpy as np

# find files
file_name_list = []
for i in os.listdir():
  if i.endswith('csv'): 
    file_name_list.append(i)
  
st.write(file_name_list)

#st.write('Hello World!')

# choose location and read data of it in
location = st.multiselect('select location', file_name_list)  #to be able to select multiple files (multiselect)
for i in location:
  df = pd.read_csv(i)

  # extract the elements and choose the ones for the x and y-axis
  el_list = df.columns.tolist()[27:80]
  x_axis = st.selectbox('select element for x', el_list)
  y_axis = st.selectbox('select element for y', el_list)

  
  
  #calculations
  
  ##calculate the mean
  mean = np.mean(df[y_axis]/10000)
  
  ##calculate the std
  std = np.std(df[y_axis]/10000)
  
  
  # plot 
  ## the x vs. y data
  p = figure(title=i + x_axis + ' vs. ' + y_axis, x_axis_label=x_axis + ' wt%', y_axis_label=y_axis + ' wt%')
  p.circle(df[x_axis]/10000, df[y_axis]/10000, size=5, color='red')
  
  ## the mean line of y
  p.line(df[x_axis]/10000, mean, line_width=1.5, color="orange")


  # choose the std you want  
  std_choice = st.radio("What ±standard deviation do you want?", ('1', '2', '3'))
  
  ## the std of y
  if std_choice == '1':
    p.line(df[x_axis]/10000, mean-std, line_width=0.5, color="navy")
    p.line(df[x_axis]/10000, mean+std, line_width=0.5, color="navy")
  elif std_choice == '2':
    p.line(df[x_axis]/10000, mean-(2*std), line_width=0.5, color="navy")
    p.line(df[x_axis]/10000, mean+(2*std), line_width=0.5, color="navy")
  elif std_choice == '3':
    p.line(df[x_axis]/10000, mean-(3*std), line_width=0.5, color="navy")
    p.line(df[x_axis]/10000, mean+(3*std), line_width=0.5, color="navy")
    
  
  st.bokeh_chart(p, use_container_width=True)

