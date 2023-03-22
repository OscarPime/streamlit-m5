import pandas as pd
import streamlit as st

name = 'dataset.csv'

dataSet = pd.read_csv(name)

st.title("Dataset con streamlit")
st.dataframe(dataSet)