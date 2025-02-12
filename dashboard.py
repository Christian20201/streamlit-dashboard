import streamlit as st
import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Title of the Dashboard
st.title("📊 AI-Powered Media Monitoring Dashboard")

# Simulated Data: Mentions by Destination
st.subheader("📍 Mentions by Tourist Destination")
destinations = ["Quintana Roo", "Cancún", "Riviera Nayarit", "Tulum", "Los Cabos"]
mentions = np.random.randint(500, 1500, size=len(destinations))
df_mentions = pd.DataFrame({"Destination": destinations, "Mentions": mentions})

# Create a bar chart
fig_mentions = px.bar(df_mentions, x="Destination", y="Mentions", title="Mentions by Destination")
st.plotly_chart(fig_mentions)

# Simulated Sentiment Analysis Data
st.subheader("📈 Sentiment Trend in Media and Social Networks")
dates = pd.date_range(start="2024-02-01", periods=30, freq="D")
sentiment_data = np.random.randint(10, 500, size=(30, 3))
df_sentiment = pd.DataFrame(sentiment_data, columns=["Positive", "Negative", "Neutral"], index=dates)

# Display line chart for sentiment analysis
st.line_chart(df_sentiment)

# Word Cloud for Emerging Trends
st.subheader("☁️ Emerging Trends in Tourism")
trend_words = "sustainable luxury gastronomy experiences beach adventure eco-tourism family-friendly nightlife resorts relaxation"
wordcloud = WordCloud(width=400, height=200, background_color="white").generate(trend_words)

# Display word cloud
fig, ax = plt.subplots(figsize=(6, 3))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)