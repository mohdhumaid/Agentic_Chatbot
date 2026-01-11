import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage


class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message

        # ---------------- BASIC CHATBOT ----------------
        if usecase == "Basic Chatbot":
            with st.chat_message("user"):
                st.write(user_message)

            for event in graph.stream(
                {"messages": [HumanMessage(content=user_message)]}
            ):
                for value in event.values():
                    if "messages" in value and value["messages"].content:
                        with st.chat_message("assistant"):
                            st.write(value["messages"].content)

        # ---------------- CHATBOT WITH WEB ----------------
        elif usecase == "Chatbot With Web":
            initial_state = {
                "messages": [HumanMessage(content=user_message)]
            }

            res = graph.invoke(initial_state)

            for message in res["messages"]:
                if isinstance(message, HumanMessage):
                    with st.chat_message("user"):
                        st.write(message.content)

                elif isinstance(message, ToolMessage):
                    with st.chat_message("assistant"):
                        st.write("🔧 Tool Call")
                        st.write(message.content)

                elif isinstance(message, AIMessage) and message.content:
                    with st.chat_message("assistant"):
                        st.write(message.content)

        # ---------------- AI NEWS ----------------
        elif usecase == "AI News":
            frequency = user_message.lower()

            with st.spinner("Fetching and summarizing news... ⏳"):
                graph.invoke(
                    {
                        "messages": [
                            HumanMessage(content=frequency)
                        ]
                    }
                )

                try:
                    AI_NEWS_PATH = f"./AINews/{frequency}_summary.md"
                    with open(AI_NEWS_PATH, "r", encoding="utf-8") as file:
                        markdown_content = file.read()

                    st.markdown(markdown_content, unsafe_allow_html=True)

                except FileNotFoundError:
                    st.error(f"❌ News not generated. File not found: {AI_NEWS_PATH}")

                except Exception as e:
                    st.error(f"❌ Error occurred: {str(e)}")
