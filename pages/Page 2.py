import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

# Assuming you have a DataFrame named Final_dataset with columns 'YEAR', 'CLEAR', 'ASSERTIVE', 'CAUTIOUS', 'OPTIMISTIC', 'SPECIFIC', 'RELEVANT'
# Replace 'CLEAR', 'ASSERTIVE', 'CAUTIOUS', 'OPTIMISTIC', 'SPECIFIC', 'RELEVANT' with your actual column names for the six features

# Load your existing dataset
# final_dataset = pd.read_csv('your_dataset.csv')  # Replace 'your_dataset.csv' with the actual file name or path

st.markdown("# Page 2 : Time-Series ")
st.sidebar.markdown("# Page 2 ")

final_dataset = pd.read_excel('final_dataset.xlsx')

# Convert 'YEAR' to datetime format
final_dataset['YEAR'] = pd.to_datetime(final_dataset['YEAR'], format='%Y')

# Create a color scale for Altair
color_scale = alt.Scale(domain=['CLEAR', 'ASSERTIVE', 'CAUTIOUS', 'OPTIMISTIC', 'SPECIFIC', 'RELEVANT'],
                        range=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'])

# Initialize an empty DataFrame for storing sampled data
sampled_data = pd.DataFrame(columns=final_dataset.columns)

# Iterate through each year and randomly sample 30 data points
for year in final_dataset['YEAR'].unique():
    sampled_data = pd.concat([sampled_data, final_dataset[final_dataset['YEAR'] == year].sample(n=42, replace=True)])

# Melt the DataFrame to long format for Altair
melted_df = sampled_data.melt(id_vars=['YEAR'], var_name='Feature', value_name='Probability')

# Create separate charts for probability of 0, 1, and 2
chart_0 = alt.Chart(melted_df).transform_calculate(
    Probability_0='datum.Probability == 0 ? 1 : 0'
).mark_line().encode(
    x=alt.X('YEAR:T', title='Year', axis=alt.Axis(format='%Y', tickCount=15)),
    y=alt.Y('mean(Probability_0):Q', title='Probability', axis=alt.Axis(format='%')),
    color=alt.Color('Feature:N', title='Feature', scale=color_scale)
).properties(width=700, height=400, title='Probability of 0 Trends').interactive()

chart_1 = alt.Chart(melted_df).transform_calculate(
    Probability_1='datum.Probability == 1 ? 1 : 0'
).mark_line().encode(
    x=alt.X('YEAR:T', title='Year', axis=alt.Axis(format='%Y', tickCount=15)),
    y=alt.Y('mean(Probability_1):Q', title='Probability', axis=alt.Axis(format='%')),
    color=alt.Color('Feature:N', title='Feature', scale=color_scale)
).properties(width=700, height=400, title='Probability of 1 Trends').interactive()

chart_2 = alt.Chart(melted_df).transform_calculate(
    Probability_2='datum.Probability == 2 ? 1 : 0'
).mark_line().encode(
    x=alt.X('YEAR:T', title='Year', axis=alt.Axis(format='%Y', tickCount=15)),
    y=alt.Y('mean(Probability_2):Q', title='Probability', axis=alt.Axis(format='%')),
    color=alt.Color('Feature:N', title='Feature', scale=color_scale)
).properties(width=700, height=400, title='Probability of 2 Trends').interactive()

# Display the charts
st.altair_chart(chart_0, use_container_width=True)
st.altair_chart(chart_1, use_container_width=True)
st.altair_chart(chart_2, use_container_width=True)









