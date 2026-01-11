from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode


def get_tools(tavily_api_key: str):
    """
    Return the list of tools to be used in the chatbot.
    """

    if not tavily_api_key:
        raise ValueError("Tavily API key is required for web search tools")

    tools = [
        TavilySearchResults(
            max_results=2,
            api_key=tavily_api_key
        )
    ]
    return tools


def create_tool_node(tools):
    """
    Creates and returns a tool node for the graph.
    """
    return ToolNode(tools=tools)
