import streamlit as st
from src.langgraphagenticai.ui.uiconfigfile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):

        # ---------- SAFE SESSION STATE INIT ----------
        if "timeframe" not in st.session_state:
            st.session_state.timeframe = ""

        if "IsFetchButtonClicked" not in st.session_state:
            st.session_state.IsFetchButtonClicked = False

        if "TAVILY_API_KEY" not in st.session_state:
            st.session_state.TAVILY_API_KEY = None
        # --------------------------------------------

        st.header("🧠 " + self.config.get_page_title())

        with st.sidebar:
            # Options
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox(
                "Select LLM", llm_options
            )

            if self.user_controls["selected_llm"] == "Groq":
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox(
                    "Select Model", model_options
                )

                self.user_controls["GROQ_API_KEY"] = st.text_input(
                    "GROQ API Key", type="password"
                )

                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key")

            # Usecase
            self.user_controls["selected_usecase"] = st.selectbox(
                "Select Usecases", usecase_options
            )

            # Tavily cases
            if self.user_controls["selected_usecase"] in ["Chatbot With Web", "AI News"]:
                tavily_key = st.text_input(
                    "TAVILY API Key", type="password"
                )

                if not tavily_key:
                    st.warning("⚠️ Please enter your TAVILY API key")

                # ✅ SINGLE SOURCE OF TRUTH
                if tavily_key:
                    tavily_key = tavily_key.strip()
                    self.user_controls["tavily_api_key"] = tavily_key
                    st.session_state.TAVILY_API_KEY = tavily_key
                else:
                    self.user_controls["tavily_api_key"] = None

            # AI News controls
            if self.user_controls["selected_usecase"] == "AI News":
                st.subheader("📰 AI News Explorer")

                time_frame = st.selectbox(
                    "📅 Select Time Frame",
                    ["Daily", "Weekly", "Monthly"],
                    index=0
                )

                if st.button("🔍 Fetch Latest AI News", use_container_width=True):
                    st.session_state.IsFetchButtonClicked = True
                    st.session_state.timeframe = time_frame

        return self.user_controls
