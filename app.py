import streamlit as st
import sys

sys.path.append(".")

from src.langgraphagenticai.main import load_langgraph_agenticai_app

st.set_page_config(page_title="Agentic Chatbot", page_icon="🤖", layout="wide")

# Start Streamlit UI
load_langgraph_agenticai_app()
