import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import codecs
import matplotlib.pyplot as plt


# # load a limit number of rows
# def load_dataframe(nrows):
#     df = pd.read_csv("employees.csv", nrows=nrows)
#     return df



# # Function with cache that load all employees
# @st.cache
# def load_alldata():
#     df = pd.read_csv("employees.csv")
#     return df

# dfEmp = load_dataframe(500)
# dfEmpAll = load_dataAll()

# crear title de la app web.
st.title("Employee analysis")

sidebar = st.sidebar
sidebar.title("Filters")