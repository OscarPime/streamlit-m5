import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import codecs
import matplotlib.pyplot as plt


df_employees = load_data(500)
df_employeescomplete = load_dataAll()

# crear title de la app web.
st.title("Employees App (By Leonardo Gonzalez)")

sidebar = st.sidebar
sidebar.title("Filters")