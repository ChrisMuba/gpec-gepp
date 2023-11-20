

# let's start by importing the necessary libraries and loading your dataset. We'll use pandas for data manipulation, numpy for numerical operations, and streamlit and plotly for data visualization.
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

# Next, let's load your dataset. We'll use pandas' read_csv function to load your CSV data into a DataFrame.
df = pd.read_csv('csv_files/turnover_data.csv')

# Before we proceed with the analysis, we should check the basic information about the dataset and handle any missing values. We can use the info and describe functions for this.
st.write(df.info())
st.write(df.describe())

# We can also check for missing values and handle them accordingly.
st.write(df.isnull().sum())

# Now, let's proceed with the EDA analysis.

# 1. Turnover Trends Over Time: We can use plotly to create a line graph showing turnover rates over time. We'll need to calculate the turnover rate first.

df['turnover_date'] = pd.to_datetime(df['departure_date'])
df['recruitment_date'] = pd.to_datetime(df['recruitment_date'])
df['tenure'] = (df['turnover_date'] - df['recruitment_date']).dt.days / 365
df['turnover'] = 1
df_turnover = df.groupby('turnover_date')['turnover'].sum()
fig = px.line(df_turnover, x=df_turnover.index, y='turnover', title='Turnover Trends Over Time')
st.plotly_chart(fig)

# 2. Analysis of Turnover Rates by Department: We can use a bar chart to compare turnover rates across different departments.
df_turnover_by_dept = df.groupby('department')['turnover'].sum()
fig = px.bar(df_turnover_by_dept, x=df_turnover_by_dept.index, y='turnover', title='Turnover Rates by Department')
st.plotly_chart(fig)

# 3. Impact of Tenure on Turnover: We can use a histogram to show the distribution of tenure at departure.
fig = px.histogram(df, x='tenure', title='Impact of Tenure on Turnover')
st.plotly_chart(fig)

# 4.Gender-Based Turnover Analysis: We can use a bar chart to compare turnover rates between genders.
df_turnover_by_gender = df.groupby('gender')['turnover'].sum()
fig = px.bar(df_turnover_by_gender, x=df_turnover_by_gender.index, y='turnover', title='Gender-Based Turnover Analysis')
st.plotly_chart(fig)

# 5. Impact of Position Held on Turnover: We can use a bar chart to compare turnover rates by position.
df_turnover_by_position = df.groupby('position_held')['turnover'].sum()
fig = px.bar(df_turnover_by_position, x=df_turnover_by_position.index, y='turnover', title='Impact of Position Held on Turnover')
st.plotly_chart(fig)

# 6. Reasons for Departure and Their Trends: We can use a stacked bar chart to show the trends of different reasons for departure over time.
df_departure_reasons = df.groupby('reason_for_departure')['turnover'].sum()
fig = px.bar(df_departure_reasons, x=df_departure_reasons.index, y='turnover', title='Reasons for Departure and Their Trends')
st.plotly_chart(fig)




