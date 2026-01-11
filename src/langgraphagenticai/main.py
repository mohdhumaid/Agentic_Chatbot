import streamlit as st

# MUST be first Streamlit call
st.set_page_config(page_title="Agentic AI Chatbot", page_icon="🤖", layout="wide")

from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMs.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit


@st.cache_resource
def get_llm_model(user_input):
    llm_config = GroqLLM(user_controls_input=user_input)
    return llm_config.get_llm_model()


@st.cache_resource
def get_graph(model, usecase, tavily_api_key):
    builder = GraphBuilder(
        model=model,
        tavily_api_key=tavily_api_key
    )
    return builder.setup_graph(usecase)


def load_langgraph_agenticai_app():

    # -------- SESSION STATE --------
    if "IsFetchButtonClicked" not in st.session_state:
        st.session_state.IsFetchButtonClicked = False

    if "timeframe" not in st.session_state:
        st.session_state.timeframe = ""

    if "TAVILY_API_KEY" not in st.session_state:
        st.session_state.TAVILY_API_KEY = None

    # -------- UI --------
    st.title("🤖 Agentic AI Chatbot")
    st.markdown("---")

    st.markdown(
        "<div style='text-align:center; font-size:14px; color:#6b7280;'>"
        "🧠 <b>LangGraph</b> &nbsp;•&nbsp; "
        "⚡ <b>Groq</b> &nbsp;•&nbsp; "
        "🤖 <b>Agentic Workflows</b>"
        "</div>",
        unsafe_allow_html=True
    )

    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui() or {}

    # ✅ CAPTURE Tavily API key from UI
    tavily_key = user_input.get("tavily_api_key")

    if tavily_key:
        st.session_state.TAVILY_API_KEY = tavily_key

    if st.session_state.get("IsFetchButtonClicked"):
        user_message = st.session_state.get("timeframe", "")
    else:
        user_message = st.chat_input("💬 Ask the Agentic AI anything…")

    if not user_message:
        st.info("👋 Enter a message to start chatting.")
        st.stop()

    # -------- EXECUTION --------
    try:
        model = get_llm_model(user_input)
        if not model:
            st.error("❌ LLM initialization failed")
            st.stop()

        usecase = user_input.get("selected_usecase")
        if not usecase:
            st.error("❌ Select a use case from sidebar")
            st.stop()

        # 🚨 AI News requires Tavily
        if usecase == "ai_news" and not st.session_state.TAVILY_API_KEY:
            st.error("❌ Tavily API key is required for AI News use case")
            st.stop()

        graph = get_graph(
            model=model,
            usecase=usecase,
            tavily_api_key=st.session_state.TAVILY_API_KEY
        )

        DisplayResultStreamlit(
            usecase=usecase,
            graph=graph,
            user_message=user_message
        ).display_result_on_ui()

    except Exception as e:
        st.exception(e)
