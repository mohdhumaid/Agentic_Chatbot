import os
import streamlit as st
from langchain_groq import ChatGroq
from groq import AuthenticationError, BadRequestError, RateLimitError


class GroqLLM:
    def __init__(self, user_controls_input: dict):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        # ---- SAFE KEY ACCESS ----
        groq_api_key = self.user_controls_input.get("GROQ_API_KEY", "").strip()
        env_groq_key = os.getenv("GROQ_API_KEY", "").strip()
        api_key = groq_api_key or env_groq_key

        selected_groq_model = self.user_controls_input.get("selected_groq_model")

        # ---- VALIDATE KEY PRESENCE ----
        if not api_key:
            st.warning("🔑 To use this app, please enter your Groq API key in the sidebar.")
            st.stop()

        try:
            llm = ChatGroq(
                api_key=api_key,
                model=selected_groq_model
            )

            # 🔍 Lightweight validation call (forces Groq auth + model check)
            llm.invoke("ping")

            return llm

        except AuthenticationError:
            st.error("🔑 Invalid Groq API key. Please check the key in the sidebar.")
            st.stop()

        except BadRequestError:
            st.error(
                f"🚫 The model **{selected_groq_model}** is not available for your Groq API key."
            )
            st.stop()

        except RateLimitError:
            st.warning("⏳ Groq rate limit reached. Please try again later.")
            st.stop()

        except Exception as e:
            # ⚠️ Do NOT re-raise ValueError — show clean UI error instead
            st.error(f"⚠️ Unexpected Groq error: {e}")
            st.stop()
