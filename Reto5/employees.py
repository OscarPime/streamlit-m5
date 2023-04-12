
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

# Function load all employees
@st.cache
def load_alldata():
    dataframe = pd.read_csv(DATA_URL)
    return dataframe

df_limitEmp = load_filterdata(500)
df_allemployees = load_alldata()

# Function offilter by Emloyee_ID
@st.cache
def getInfo_name(id_employe):
    filtered_data_byname = df_allemployees[df_allemployees['Employee_ID'].str.upper().str.contains(id_employe)]
    return filtered_data_byname

# Function filter HomeTown
@st.cache
def getInfo_hometown(filter):
    df_fltHometown = df_allemployees[df_allemployees['Hometown'].str.upper().str.contains(filter)]
    return df_fltHometown

# Function filter Unit
@st.cache
def getInfo_unit(filter):
    df_fltUnit = df_allemployees[df_allemployees['Unit'].str.upper().str.contains(filter)]
    return df_fltUnit

# Function filter Education_level
@st.cache
def getInfo_education_level(level):
    df_fltlevel = df_allemployees[df_allemployees['Education_Level'] == level ]
    return df_fltlevel

# Function filter HometownSELECT
@st.cache
def getInfo_hometownSelect(hometown_selec):
    df_fltHomeTownSelec = df_allemployees[df_allemployees['Hometown'] == hometown_selec ]
    return df_fltHomeTownSelec

# Function filter UnitSELECT
@st.cache
def getInfo_UnitSelect(unit_selec):
    df_fltUnitSelec = df_allemployees[df_allemployees['Unit'] == unit_selec ]
    return df_fltUnitSelec

bol_showinfo = sidebar.checkbox("Wants to show filter info?", value=True )
if bol_showinfo:
    # Filter input by Employee_ID
    id_employee = sidebar.text_input("Employee_ID:")
    if sidebar.button('Find Employee_ID'):
        if id_employee :            
            df_limitEmp = getInfo_name(id_employee.upper())

    # filter input by Hometown
    flt_hometown = sidebar.text_input("Hometown:")
    if (sidebar.button('Find Hometown')):
        if (flt_hometown):            
            df_limitemp = getInfo_hometown(flt_hometown.upper())

    # filter input by Unit
    flt_unit = sidebar.text_input("Unit:")
    if (sidebar.button('Find Unit')):
        if (flt_unit):            
            df_limitemp = getInfo_unit(flt_unit.upper())

    # filter selectedbox by education level
    flt_education_level  = sidebar.selectbox('Select Education Level', df_allemployees.sort_values(by='Education_Level')['Education_Level'].unique())
    btn_EducLevel = sidebar.button('Find Education Level')
    if (btn_EducLevel):
        df_limitEmp = getInfo_education_level(flt_education_level)
    
    # filter selectedbox by Hometown
    flt_selc_hometown  = sidebar.selectbox('Select Hometown', df_allemployees.sort_values(by='Hometown')['Hometown'].unique())
    btn_HomeTown= sidebar.button('Find Hometown (Select)')
    if (btn_HomeTown):
        df_limitEmp = getInfo_hometownSelect(flt_selc_hometown)

    # filter selectedbox by Unit
    flt_selc_unit = sidebar.selectbox('Select Unit', df_allemployees.sort_values(by='Unit')['Unit'].unique())
    btn_Unit= sidebar.button('Find Unit (Select)')
    if (btn_Unit):
        df_limitEmp = getInfo_UnitSelect(flt_selc_unit)

    # Show limit information
    st.write(f"Total Employees : {df_limitEmp.shape[0]}")
    st.dataframe(df_limitEmp)
else:
    st.write(f"Total Employees : {df_allemployees.shape[0]}")
    st.dataframe(df_allemployees)
    
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
