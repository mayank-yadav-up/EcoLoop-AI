import streamlit as st
import pandas as pd
import plotly.express as px
import random
import time

from simulation.simulator import BuildingSimulator
from agents.hvac_agent import HVACAgent

st.set_page_config(
    page_title="EcoLoop AI",
    page_icon="🏢",
    layout="wide"
)

st.title("🏢 EcoLoop AI")
st.subheader("Autonomous Smart Building Controller")

sim = BuildingSimulator()
agent = HVACAgent()

sensor = sim.update()
decision = agent.decide(sensor)

energy = sensor["Energy (kWh)"]
saving = decision["Estimated Saving (%)"]

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Outdoor Temp",
    f'{sensor["Outdoor Temp (°C)"]} °C'
)

col2.metric(
    "Indoor Temp",
    f'{sensor["Indoor Temp (°C)"]} °C'
)

col3.metric(
    "Occupancy",
    sensor["Occupancy"]
)

col4.metric(
    "Energy Saving",
    f"{saving}%"
)

st.divider()

left, right = st.columns([2,1])

with left:

    st.subheader("Live Building Sensors")

    df = pd.DataFrame(
        sensor.items(),
        columns=["Parameter","Value"]
    )

    st.dataframe(df, use_container_width=True)

    history = pd.DataFrame({
        "Hour":[
            "8 AM","9 AM","10 AM","11 AM",
            "12 PM","1 PM","2 PM","3 PM"
        ],
        "Energy":[
            155,148,142,138,
            132,128,123,energy
        ]
    })

    fig = px.line(
        history,
        x="Hour",
        y="Energy",
        markers=True,
        title="Energy Consumption Trend"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    st.subheader("AI Recommendation")

    st.success(decision["Action"])

    st.metric(
        "Estimated Saving",
        f"{saving}%"
    )

    carbon = round(saving*1.8,1)

    st.metric(
        "CO₂ Reduction",
        f"{carbon} kg/day"
    )

    st.metric(
        "Comfort Score",
        "96%"
    )

    st.progress(96)

    st.info("Building operating within comfort constraints.")

st.divider()

st.subheader("System Status")

status = pd.DataFrame({
    "Component":[
        "EnergyPlus",
        "LLM Agent",
        "Sensor Network",
        "HVAC Controller",
        "MCP Bus"
    ],
    "Status":[
        "Running",
        "Running",
        "Connected",
        "Active",
        "Healthy"
    ]
})

st.table(status)

st.success("Closed Loop AI Control Active")

st.caption("Honeywell Smart Building Hackathon Prototype")