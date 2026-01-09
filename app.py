import streamlit as st
import sys
sys.path.append(".")

from src.langgraphagenticai.main import load_langgraph_agenticai_app

# Streamlit must stay alive
load_langgraph_agenticai_app()

# Prevent exit (CRITICAL for HF)
st.empty()
while True:
    pass
