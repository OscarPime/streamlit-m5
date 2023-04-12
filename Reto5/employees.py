
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import codecs

DATA_URL = 'source/Employees.csv'

# Title of WebApp.
st.title("Employee analysis")
st.markdown("**By Oscar Pimentel Anguiano**")

sidebar = st.sidebar
sidebar.title("Filters")

# load a limit number of rows
@st.cache
def load_filterdata(num_rows):
    dataframe = pd.read_csv(DATA_URL, nrows=num_rows)
    return dataframe

# Function with cache that load all employees
@st.cache
def load_alldata():
    dataframe = pd.read_csv(DATA_URL)
    return dataframe

df_limitEmp = load_filterdata(500)
df_allemployees = load_alldata()
st.dataframe(df_allemployees)

bol_showinfo = sidebar.checkbox("Wants to show filter info?", value=True )
if bol_showinfo:
    # Show limit information
    st.write(f"Total Employees : {df_limitEmp.shape[0]}")
    st.dataframe(df_limitEmp)

st.markdown("___")

# Graph Age
fig_age, ax = plt.subplots()
ax.hist(df_allemployees["Age"])
ax.set_xlabel("Age")

st.header("Graph Age Histogram")
st.pyplot(fig_age)

# Graph of Unit
fig_unit, ax2 = plt.subplots()
ax2.hist(df_allemployees["Unit"])
ax2.set_xlabel("Unit")
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=90)

st.header("Unit Frecuency")
st.pyplot(fig_unit)

# Graph Hometown
df_homtown = df_allemployees[['Hometown','Attrition_rate']].groupby('Hometown').sum()
fig_homtown, ax3 = plt.subplots()
y_pos = df_homtown.index
x_pos = df_homtown['Attrition_rate']
ax3.barh(y_pos, x_pos)
ax3.set_ylabel("Hometown")
ax3.set_xlabel("Attrition rate")

st.header('Hometowns with more Attrition Rate')
st.pyplot(fig_homtown)

# Age vs Attrition Rate
df_Age = df_allemployees[['Age','Attrition_rate']].groupby('Age').sum()
fig_Attrit, ax4 = plt.subplots()
y_pos2 = df_Age.index
x_pos2 = df_Age['Attrition_rate']
ax4.barh(y_pos2, x_pos2)
ax4.set_ylabel("Age")
ax4.set_xlabel("Attrition rate")

st.header('Ages with more Attrition Rate')
st.pyplot(fig_Attrit)

# Dispersion (Time of service & Attriton Rate)
fig_time, ax3 = plt.subplots()
ax3.scatter(df_allemployees["Time_of_service"], df_allemployees["Attrition_rate"])
ax3.set_xlabel("Time of service")
ax3.set_ylabel("Attrition rate")


st.header("Dispersion (Time of service & Atrrition Rate)")
st.pyplot(fig_time)
