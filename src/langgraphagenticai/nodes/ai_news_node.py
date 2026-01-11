from tavily import TavilyClient
from langchain_core.prompts import ChatPromptTemplate


class AINewsNode:
    def __init__(self, llm, tavily_api_key: str):
        """
        Initialize the AINewsNode with Tavily API key and LLM.
        """
        print("DEBUG Tavily key received:", repr(tavily_api_key))
        if not tavily_api_key:
            raise ValueError("Tavily API key is required for AI News use case")

        self.tavily = TavilyClient(api_key=tavily_api_key)
        self.llm = llm

        # used to capture steps for later display
        self.state = {}

    def fetch_news(self, state: dict) -> dict:
        """
        Fetch AI news based on the specified frequency.
        """

        frequency = state["messages"][0].content.lower()
        self.state["frequency"] = frequency

        time_range_map = {
            "daily": "d",
            "weekly": "w",
            "monthly": "m",
            "year": "y"
        }

        days_map = {
            "daily": 1,
            "weekly": 7,
            "monthly": 30,
            "year": 366
        }

        response = self.tavily.search(
            query="Top Artificial Intelligence (AI) technology news India and globally",
            topic="news",
            time_range=time_range_map.get(frequency, "d"),
            include_answer="advanced",
            max_results=20,
            days=days_map.get(frequency, 1),
        )

        state["news_data"] = response.get("results", [])
        self.state["news_data"] = state["news_data"]

        return state

    def summarize_news(self, state: dict) -> dict:
        """
        Summarize fetched news using LLM.
        """

        news_items = self.state.get("news_data", [])

        prompt_template = ChatPromptTemplate.from_messages([
            ("system", """Summarize AI news articles into markdown format.
For each item include:
- Date in **YYYY-MM-DD** format in IST timezone
- Concise summary from latest news
- Sort by date (latest first)
- Source URL as link

Use format:
### [Date]
- [Summary](URL)
"""),
            ("user", "Articles:\n{articles}")
        ])

        articles_str = "\n\n".join([
            f"Content: {item.get('content', '')}\n"
            f"URL: {item.get('url', '')}\n"
            f"Date: {item.get('published_date', '')}"
            for item in news_items
        ])

        response = self.llm.invoke(
            prompt_template.format(articles=articles_str)
        )

        state["summary"] = response.content
        self.state["summary"] = state["summary"]

        return state

    def save_result(self, state: dict) -> dict:
        """
        Save summarized news to markdown file.
        """

        frequency = self.state.get("frequency", "daily")
        summary = self.state.get("summary", "")

        filename = f"./AINews/{frequency}_summary.md"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# {frequency.capitalize()} AI News Summary\n\n")
            f.write(summary)

        self.state["filename"] = filename
        return self.state
