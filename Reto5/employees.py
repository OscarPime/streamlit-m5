
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import codecs


# # load a limit number of rows
# @st.cache
# def load_dataframe(num_rows):
#     df = pd.read_csv("source/Employees.csv", nrows=num_rows)
#     return df

# # Function with cache that load all employees
# @st.cache
# def load_alldata():
#     df = pd.read_csv("source/Employees.csv")
#     return df

# dfEmp = load_dataframe(500)
# dfEmpAll = load_alldata()

# crear title de la app web.
st.title("Employee analysis")

sidebar = st.sidebar
sidebar.title("Filters")

df = pd.read_csv("source/Employees.csv")
st.dataframe(df)


# show_df = sidebar.checkbox("Show Data Frame?", value=True )


# # Graph Age
# st.markdown("___")
# fig, ax = plt.subplots()
# ax.hist(dfEmpAll["Age"])
# ax.set_xlabel("Age")
# st.header("Age Histogram")
# st.pyplot(fig)

# # Graph Unit
# st.markdown("___")
# fig2, ax2 = plt.subplots()
# ax2.hist(dfEmpAll["Unit"])
# ax2.set_xlabel("Unit")
# ax2.set_xticklabels(ax2.get_xticklabels(), rotation=90)
# st.header("Unit Frecuency")
# st.pyplot(fig2)

# # Graph Hometown 
# st.markdown("___")
# #Create new dataframe
# df_empl_homtown = dfEmpAll[['Hometown','Attrition_rate']].groupby('Hometown').sum()
# #st.dataframe(df_empl_homtown)
# fig3, ax3 = plt.subplots()
# y_pos = df_empl_homtown.index
# x_pos = df_empl_homtown['Attrition_rate']
# ax3.barh(y_pos, x_pos)
# ax3.set_ylabel("Hometown")
# ax3.set_xlabel("Attrition rate")
# st.header('Hometowns with more Attrition Rate')
# st.pyplot(fig3)

# # Graph Age vs Attrition Rate 
# st.markdown("___")
# #Create new dataframe
# df_empl_Age = dfEmpAll[['Age','Attrition_rate']].groupby('Age').sum()
# #st.dataframe(df_empl_Age)
# fig4, ax4 = plt.subplots()
# y_pos2 = df_empl_Age.index
# x_pos2 = df_empl_Age['Attrition_rate']
# ax4.barh(y_pos2, x_pos2)
# ax4.set_ylabel("Age")
# ax4.set_xlabel("Attrition rate")
# st.header('Ages with more Attrition Rate')
# st.pyplot(fig4)


# # Graph dispersion between Time of service and Attriton Rate
# st.markdown("___")
# fig3, ax3 = plt.subplots()
# ax3.scatter(dfEmpAll["Time_of_service"], dfEmpAll["Attrition_rate"])
# ax3.set_xlabel("Time of service")
# ax3.set_ylabel("Attrition rate")
# st.header("Relation between Time of service and Atrrition Rate")
# st.pyplot(fig3)