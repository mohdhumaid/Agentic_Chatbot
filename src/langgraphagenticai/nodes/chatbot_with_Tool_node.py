from langchain_core.messages import HumanMessage, AIMessage
from src.langgraphagenticai.state.state import State


class ChatbotWithToolNode:
    """
    Chatbot logic enhanced with tool integration
    """

    def __init__(self, model):
        self.llm = model

    def process(self, state: State) -> dict:
        """
        Processes input state and generates a response.
        (Not used in graph directly, but kept safe)
        """

        messages = state.get("messages", [])

        response = self.llm.invoke(messages)

        return {
            "messages": messages + [response]
        }

    def create_chatbot(self, tools):
        """
        Returns a chatbot node function with tool binding.
        """

        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            """
            Chatbot logic for processing the input state and returning a response.
            """

            messages = state.get("messages", [])

            # Invoke LLM with full conversation history
            response = llm_with_tools.invoke(messages)

            return {
                "messages": messages + [response]
            }

        return chatbot_node
