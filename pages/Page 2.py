import streamlit as st

st.markdown("# Page 2 : Correlation Matrix")
st.sidebar.markdown("# Page 2 ")

import streamlit as st
import pandas as pd
import plotly.express as px

# Assuming result_df is your DataFrame
# If not, replace result_df with your actual DataFrame
result_df = pd.read_excel('final_dataset.xlsx')
# Selecting the tonality features for correlation calculation
tonality_features = ['CLEAR', 'ASSERTIVE', 'CAUTIOUS', 'OPTIMISTIC', 'SPECIFIC', 'RELEVANT']

# Creating a DataFrame containing only the tonality features
tonality_df = result_df[tonality_features]

# Calculating the correlation matrix
correlation_matrix = tonality_df.corr()

# Create annotations with correlation values
annotations = [
    dict(
        x=i,
        y=j,
        text=str(round(correlation_matrix.iloc[i, j], 2)),
        showarrow=False,
        font=dict(color='black'),
    )
    for i in range(len(tonality_features))
    for j in range(len(tonality_features))
]

# Streamlit app
st.title("Interactive Correlation Matrix")

# Create an interactive heatmap using Plotly
fig = px.imshow(correlation_matrix,
                labels=dict(color="Correlation"), 
                x=tonality_features, 
                y=tonality_features,
                color_continuous_scale='RdBu', 
                zmin=-1, 
                zmax=1)

# Set title
fig.update_layout(title_text='Correlation Matrix of Tonality Features')

# Add correlation values as annotations
fig.update_layout(annotations=annotations)

# Display the plot using Streamlit
st.plotly_chart(fig)
