import streamlit as st

st.set_page_config(page_title="Analytics", layout="wide")

st.title("📊 PPE Analytics Dashboard")

st.markdown("### Power BI Live Dashboard")

POWERBI_URL ="https://app.powerbi.com/view?r=eyJrIjoiMGVhMTJkZDQtOTZjNC00M2Q5LTkxNjctZjdlYzg0MjQ4ZDE5IiwidCI6ImM3ZWU3YWFhLWQ5YWMtNDRjNy04ODQ5LWUzNjJlYTgyMGE5NSJ9"

st.components.v1.iframe(
    src=POWERBI_URL,
    width=1400,
    height=800,
    scrolling=True
)