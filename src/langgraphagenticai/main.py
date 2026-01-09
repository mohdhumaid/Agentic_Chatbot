import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMs.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit


def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    """

    # MUST be first Streamlit call
    st.set_page_config(page_title="Agentic AI Chatbot", layout="wide")

    # -------- SAFE SESSION STATE INIT --------
    if "IsFetchButtonClicked" not in st.session_state:
        st.session_state.IsFetchButtonClicked = False

    if "timeframe" not in st.session_state:
        st.session_state.timeframe = ""

    # ----------------------------------------

    # Always render something (HF health check)
    st.title("🤖 Agentic AI Chatbot")
    st.write("App loaded successfully")
    st.caption("LangGraph • Groq • Agentic Workflows")

    # Load sidebar / controls
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui() or {}

    # Input handling
    if st.session_state.get("IsFetchButtonClicked"):
        user_message = st.session_state.get("timeframe", "")
    else:
        user_message = st.chat_input("Enter your message")

    # ✅ IMPORTANT: Do NOT stop the app
    if not user_message:
        st.info("👋 Enter a message to start chatting with the Agentic AI.")
        return

    try:
        # Configure LLM
        obj_llm_config = GroqLLM(user_controls_input=user_input)
        model = obj_llm_config.get_llm_model()

        if not model:
            st.error("❌ LLM model could not be initialized")
            return

        # Use case
        usecase = user_input.get("selected_usecase")
        if not usecase:
            st.error("❌ Please select a use case from the sidebar")
            return

        # Build graph
        graph_builder = GraphBuilder(model)
        graph = graph_builder.setup_graph(usecase)

        # Display result
        DisplayResultStreamlit(
            usecase=usecase,
            graph=graph,
            user_message=user_message
        ).display_result_on_ui()

    except Exception as e:
        st.error(f"❌ Runtime Error: {e}")