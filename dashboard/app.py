import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Smart Home Energy Monitoring",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Smart Home Energy Monitoring System")

df = pd.read_csv("data/energy_log.csv")

latest = df.iloc[-1]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Voltage (V)",
        round(latest["Voltage"], 2)
    )

with col2:
    st.metric(
        "Current (A)",
        round(latest["Current"], 2)
    )

with col3:
    st.metric(
        "Power (W)",
        round(latest["Power"], 2)
    )

col4, col5, col6 = st.columns(3)

with col4:
    st.metric(
        "Energy (kWh)",
        round(latest["Energy"], 4)
    )

with col5:
    st.metric(
        "Cost (₹)",
        round(latest["Cost"], 2)
    )

with col6:
    st.metric(
        "Alert",
        latest["Alert"]
    )

st.subheader("Power Consumption")

fig1 = px.line(
    df,
    y="Power",
    title="Power Usage Over Time"
)

st.plotly_chart(fig1, use_container_width=True)

st.subheader("Energy Consumption")

fig2 = px.line(
    df,
    y="Energy",
    title="Energy Usage Over Time"
)

st.plotly_chart(fig2, use_container_width=True)

st.subheader("Voltage Monitoring")

fig3 = px.line(
    df,
    y="Voltage",
    title="Voltage Trend"
)

st.plotly_chart(fig3, use_container_width=True)

st.subheader("Current Monitoring")

fig4 = px.line(
    df,
    y="Current",
    title="Current Trend"
)

st.plotly_chart(fig4, use_container_width=True)

st.subheader("Raw Data")

st.dataframe(df.tail(20))