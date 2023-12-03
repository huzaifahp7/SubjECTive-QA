import streamlit as st
import pandas as pd
import plotly.express as px

# Streamlit page configuration
st.set_page_config(page_title='Interactive Tonality Feature Visualization', layout='wide')

# Title for the app
st.title('Interactive Visualization of Tonality Features')

# Loading the data
@st.cache_data
def load_data():
    return pd.read_excel('final_dataset.xlsx')

df = load_data()

# Select the tonality features for probability calculation
tonality_features = ['CLEAR', 'ASSERTIVE', 'CAUTIOUS', 'OPTIMISTIC', 'SPECIFIC', 'RELEVANT']

# Calculate probabilities for each tonality feature
def calculate_probabilities(value):
    prob_df = pd.DataFrame(index=tonality_features, columns=df.index)
    for feature in tonality_features:
        prob_df.loc[feature] = (df[feature] == value).astype(int)
    return prob_df.mean(axis=1)

# Interactive feature to select probability
selected_prob = st.selectbox("Select Probability Value", options=[0, 1, 2], index=0)

# Calculate the probabilities based on selection
prob_df = calculate_probabilities(selected_prob)

# Plotting function using Plotly
def create_interactive_bar_plot(data, title):
    fig = px.bar(
        x=tonality_features, y=data,
        labels={'y': 'Probability', 'x': 'Tonality Feature'},
        title=f'Probability of Tonality Features Being {selected_prob}'
    )
    fig.update_traces(marker_color=px.colors.sequential.Viridis, 
                      marker_line_width=1.5, 
                      width=0.4)  # Thinner bars
    fig.update_layout(font=dict(family="Arial, sans-serif", size=12, color='black'),
        title_font=dict(size=16, color='black'),
        xaxis=dict(title='Tonality Feature', title_font=dict(color='black'), tickfont=dict(color='black')),
        yaxis=dict(title='Probability', title_font=dict(color='black'), tickfont=dict(color='black')),
        hovermode='x unified',
                      plot_bgcolor='white',  # Set plot background to white
                      paper_bgcolor='white')  # Unified hover mode
    fig.update_layout(transition_duration=500)  # Animation effect
    return fig

# Visualize the selected probability
fig = create_interactive_bar_plot(prob_df, f'Probability of Tonality Features Being {selected_prob}')
st.plotly_chart(fig, use_container_width=True)
