import streamlit as st
import pandas as pd

st.write('Hello World!')

df = pd.read_csv('Bastar Craton.csv')
st.dataframe(df)
