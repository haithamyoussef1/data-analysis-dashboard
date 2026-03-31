import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px #draw visuals
import streamlit as st  # web App
 
#page size
 
st.set_page_config(layout="wide")
#data load
df = pd.read_csv("ds_salaries.csv")
 
#title
st.title("Data Science Salaries Dashboard")
#clean 
df.columns = df.columns.str.strip()
#sidebar filter
st.sidebar.header("Filters")
 
#filter 
experience = st.sidebar.selectbox("Select Experience Level" , df['experience_level'].unique())
year = st.sidebar.selectbox ("Select Year" , df['work_year'].unique())
 
filtered = df[ (df["experience_level"] == experience) & (df["work_year"] == year) ]
 
#KPI
col1, col2, col3, col4 = st.columns(4)
 
col1.metric("Average Salary (USD)", f"{filtered['salary_in_usd'].mean():,.0f}")
col2.metric("Max Salary (USD)", f"{filtered['salary_in_usd'].max():,.0f}")
col3.metric("Min Salary (USD)", f"{filtered['salary_in_usd'].min():,.0f}")
col4.metric("Total Salary (USD)", f"{filtered['salary_in_usd'].sum():,.0f}")
 
 
 
#figures 
fig1 = px.bar (filtered, x= 'job_title' , y='salary_in_usd',
        title = "Salary by Job Title")
st.plotly_chart(fig1)