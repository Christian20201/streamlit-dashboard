import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Title of the Dashboard
st.title("📊 AI-Powered Media Monitoring Dashboard")

# Dropdown to select destination
st.subheader("📍 Select a Tourist Destination")
destinations = ["All", "Quintana Roo", "Cancún", "Riviera Nayarit", "Tulum", "Los Cabos"]
selected_destination = st.selectbox("Choose a destination:", destinations)

# Simulated Data: Mentions by Destination
mentions = np.random.randint(500, 1500, size=len(destinations)-1)
df_mentions = pd.DataFrame({"Destination": destinations[1:], "Mentions": mentions})

# Filter data if user selects a specific destination
if selected_destination != "All":
    df_mentions = df_mentions[df_mentions["Destination"] == selected_destination]

# Create a bar chart
fig_mentions = px.bar(df_mentions, x="Destination", y="Mentions", title="Mentions by Destination")
st.plotly_chart(fig_mentions)

# Interactive slider to select date range
st.subheader("📅 Select Date Range for Sentiment Analysis")
date_range = st.slider("Pick a date range:", 1, 30, (5, 25))

# Simulated Sentiment Analysis Data
dates = pd.date_range(start="2024-02-01", periods=30, freq="D")
sentiment_data = np.random.randint(10, 500, size=(30, 3))
df_sentiment = pd.DataFrame(sentiment_data, columns=["Positive", "Negative", "Neutral"], index=dates)

# Filter sentiment data by user-selected range
df_sentiment_filtered = df_sentiment.iloc[date_range[0]:date_range[1]]

# Display line chart for sentiment analysis
st.line_chart(df_sentiment_filtered)

# Word Cloud for Emerging Trends
st.subheader("☁️ Emerging Trends in Tourism")
trend_words = "sustainable luxury gastronomy experiences beach adventure eco-tourism family-friendly nightlife resorts relaxation"
wordcloud = WordCloud(width=400, height=200, background_color="white").generate(trend_words)

# Display word cloud
fig, ax = plt.subplots(figsize=(6, 3))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)
