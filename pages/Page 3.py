import streamlit as st

st.markdown("# Page 3 : Correlation Matrix")
st.sidebar.markdown("# Page 3 ")

import streamlit as st
import pandas as pd
import altair as alt

# Load your data from the Excel file into a Pandas DataFrame
df = pd.read_excel('final_dataset.xlsx')

# Select the tonality features for correlation calculation
tonality_features = ['CLEAR', 'ASSERTIVE', 'CAUTIOUS', 'OPTIMISTIC', 'SPECIFIC', 'RELEVANT']

# Create a DataFrame containing only the tonality features
tonality_df = df[tonality_features]

# Calculate the correlation matrix
correlation_matrix = tonality_df.corr()

# Set up Altair chart
chart = alt.Chart(correlation_matrix.unstack().reset_index(), title='Correlation Matrix of Tonality Features').mark_rect().encode(
    x='level_0:N',
    y='level_1:N',
    color='values:Q'
).properties(width=400, height=400)

# Create a Streamlit slider for adjusting the correlation matrix threshold
threshold = st.slider('Correlation Threshold', min_value=-1.0, max_value=1.0, value=0.0, step=0.1)

# Display the chart with the Matplotlib plot using st.altair_chart()
st.altair_chart(chart, use_container_width=True)

# Display only correlations above the threshold
correlation_pairs = st.checkbox('Display Pairs Above Threshold', value=False)
if correlation_pairs:
    st.write('Correlation pairs above the threshold:')
    high_correlation_pairs = (correlation_matrix.abs() > threshold) & (correlation_matrix < 1.0)
    st.write(high_correlation_pairs)


