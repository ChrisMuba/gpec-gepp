import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Load the dataset
@st.cache
def load_data():
    data = pd.read_csv('turnover_data.csv', parse_dates=['Date_de_recrutement', 'Date_de_départ'])
    # Correcting gender labels if necessary (assuming 'Homme' is male and 'Femme' is female)
    data['Genre'] = data['Genre'].replace({'Homme': 'Male', 'Femme': 'Female'})
    return data

df = load_data()

# Calculate tenure in days
df['tenure'] = (df['Date_de_départ'] - df['Date_de_recrutement']).dt.days

# Calculate turnover rate
def calculate_turnover(df):
    # Assuming the dataset is for a specific period, e.g., one year
    total_employees = len(df)
    total_departures = df['Date_de_départ'].notna().sum()
    turnover_rate = (total_departures / total_employees) * 100
    return turnover_rate

turnover_rate = calculate_turnover(df)

# Title of the app
st.title('HR Turnover Analysis')

# Display turnover rate
st.write(f"Overall Turnover Rate: {turnover_rate:.2f}%")

# Turnover Trends Over Time
st.subheader('Turnover Trends Over Time')
turnover_trends = df.set_index('Date_de_départ').resample('M').size()
fig_turnover_trends = px.line(x=turnover_trends.index, y=turnover_trends.values, labels={'x': 'Month', 'y': 'Turnover Count'})
st.plotly_chart(fig_turnover_trends)

# Analysis of Turnover Rates by Department
st.subheader('Turnover Rates by Department')
turnover_by_dept = df.groupby('Service')['Matricule'].count().reset_index()
fig_turnover_by_dept = px.bar(turnover_by_dept, x='Service', y='Matricule', labels={'Matricule': 'Turnover Count'})
st.plotly_chart(fig_turnover_by_dept)

# Impact of Tenure on Turnover
st.subheader('Impact of Tenure on Turnover')
fig_tenure = px.histogram(df, x='tenure', nbins=30)
st.plotly_chart(fig_tenure)

# Gender-Based Turnover Analysis
st.subheader('Gender-Based Turnover Analysis')
turnover_by_gender = df.groupby('Genre')['Matricule'].count().reset_index()
fig_gender = px.bar(turnover_by_gender, x='Genre', y='Matricule', labels={'Matricule': 'Turnover Count'})
st.plotly_chart(fig_gender)

# Impact of Position Held on Turnover
st.subheader('Impact of Position Held on Turnover')
turnover_by_position = df.groupby('Poste_occupé')['Matricule'].count().reset_index()
fig_position = px.bar(turnover_by_position, x='Poste_occupé', y='Matricule', labels={'Matricule': 'Turnover Count'})
st.plotly_chart(fig_position)

# Reasons for Departure and Their Trends
st.subheader('Reasons for Departure and Their Trends')
reasons_trends = df.groupby([df['Date_de_départ'].dt.to_period('M'), 'Raison_du_départ']).size().unstack().fillna(0)
fig_reasons_trends = px.line(reasons_trends)
st.plotly_chart(fig_reasons_trends)

# Run the Streamlit app
if __name__ == '__main__':
    st.run()