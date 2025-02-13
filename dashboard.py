import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Title of the Dashboard
st.title("📊 AI-Powered Media Monitoring Dashboard")

# ✅ SECTION 1: Comparación de Menciones por Destino
st.subheader("📍 Comparación de Menciones por Destino Turístico")

destinations = ["Quintana Roo", "Cancún", "Riviera Nayarit", "Tulum", "Los Cabos"]
mentions = np.random.randint(500, 1500, size=len(destinations))
df_mentions = pd.DataFrame({"Destino": destinations, "Menciones": mentions})

fig_mentions = px.bar(df_mentions, x="Destino", y="Menciones", title="Menciones por Destino")
st.plotly_chart(fig_mentions)

# ✅ SECTION 2: Análisis de Sentimiento con Filtros
st.subheader("📈 Análisis de Sentimiento en Medios y Redes Sociales")

dates = pd.date_range(start="2024-02-01", periods=30, freq="D")
sentiment_data = np.random.randint(10, 500, size=(30, 3))
df_sentiment = pd.DataFrame(sentiment_data, columns=["Positivo", "Negativo", "Neutral"], index=dates)

date_range = st.slider("Selecciona un rango de fechas:", 1, 30, (5, 25))
df_sentiment_filtered = df_sentiment.iloc[date_range[0]:date_range[1]]

st.line_chart(df_sentiment_filtered)

# ✅ SECTION 3: Tendencias Emergentes (Nube de Palabras)
st.subheader("☁️ Tendencias Emergentes en Turismo")

trend_words = "sostenible lujo gastronomía experiencias playa aventura ecoturismo familiar vida-nocturna resorts relajación"
wordcloud = WordCloud(width=400, height=200, background_color="white").generate(trend_words)

fig, ax = plt.subplots(figsize=(6, 3))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# ✅ SECTION 4: Detección de Fake News
st.subheader("🛑 Detección de Fake News en Medios y Redes")

fake_news_count = np.random.randint(0, 20, size=len(dates))
df_fake_news = pd.DataFrame({"Fecha": dates, "Fake News Detectadas": fake_news_count})

fig_fake_news = px.bar(df_fake_news, x="Fecha", y="Fake News Detectadas", title="Fake News Detectadas por Día")
st.plotly_chart(fig_fake_news)

# ✅ SECTION 5: Impacto de Campañas de PR
st.subheader("📊 Impacto de Campañas de Relaciones Públicas")

campaigns = ["Campaña A", "Campaña B", "Campaña C"]
engagement_before = np.random.randint(500, 1500, size=len(campaigns))
engagement_after = engagement_before + np.random.randint(200, 800, size=len(campaigns))

df_campaigns = pd.DataFrame({"Campaña": campaigns, "Antes": engagement_before, "Después": engagement_after})

fig_campaigns = px.bar(df_campaigns, x="Campaña", y=["Antes", "Después"], barmode="group",
                       title="Impacto de Campañas en Engagement")
st.plotly_chart(fig_campaigns)

# ✅ SECTION 6: Alertas de Crisis
st.subheader("🚨 Alertas de Crisis de Reputación")

alert_status = ["🚨 Alerta" if np.random.random() > 0.7 else "✅ Normal" for _ in range(30)]
df_alerts = pd.DataFrame({"Fecha": dates, "Estado de Alerta": alert_status})

alert_counts = df_alerts["Estado de Alerta"].value_counts()
fig_alerts = px.bar(x=alert_counts.index, y=alert_counts.values, title="Estado de Alertas de Crisis")

st.plotly_chart(fig_alerts)
