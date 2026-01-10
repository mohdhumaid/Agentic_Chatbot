# 🧠 Agentic AI Chatbot

An **Agentic AI-powered chatbot** built with **Streamlit**, **LangGraph**, and **Groq**, designed to run **autonomous workflows**, use **tools**, and provide an **AI News Summarizer** experience.

This application demonstrates how to build **production-ready agentic systems** with modular graphs, dynamic LLM selection, and real-time user interaction.

---

## 🚀 Features

### 🤖 Agentic Chatbot
- Multi-step reasoning using **LangGraph**
- Stateful conversations
- Modular agent nodes
- Safe reruns with Streamlit session state

### 🛠️ Tool-Enabled AI
- Tool calling support inside agent workflows
- Dynamic tool execution based on user intent
- Extensible design to add more tools easily

### 📰 AI News Summarizer
- Fetches latest AI-related news
- Supports **Daily / Weekly / Monthly** summaries
- Uses external search tools (e.g., Tavily)
- Summarizes content using LLMs

### ⚡ Multi-Model Support
- Groq-powered LLMs
- Supports:
  - `llama-3.1-8b-instant`
  - `llama-3.3-70b-versatile`
- Provider-aware model handling

### 🎨 Streamlit UI
- Clean, modern chat interface
- Sidebar-based configuration
- Chat-style input/output
- Logo, icons, and enhanced UI elements

---

## 🏗️ Tech Stack

- **Frontend**: Streamlit
- **Agent Framework**: LangGraph
- **LLM Provider**: Groq
- **Orchestration**: LangChain
- **Tools / Search**: Tavily API
- **Language**: Python 3.10+

---

## 📂 Project Structure

```

agentic_chatbot/
│
├── app.py
├── requirements.txt
├── README.md
│
├── src/
│   └── langgraphagenticai/
│       ├── main.py
│       ├── graph/
│       │   └── graph_builder.py
│       ├── nodes/
│       │   └── basic_chatbot_node.py
│       ├── LLMs/
│       │   └── groqllm.py
│       └── ui/
│           └── streamlitui/
│               ├── loadui.py
│               └── display_result.py

````

---

## 🔑 Environment Variables

Set the following environment variables or Streamlit secrets:

```bash
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
````

### Streamlit Cloud (`.streamlit/secrets.toml`)

```toml
GROQ_API_KEY="your_groq_api_key"
TAVILY_API_KEY="your_tavily_api_key"
```

---

## ▶️ Running Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/Agentic_Chatbot.git
cd Agentic_Chatbot
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the app

```bash
streamlit run app.py
```

---

## ☁️ Deployment

### ✅ Streamlit Cloud

* Push code to GitHub
* Connect repository on Streamlit Cloud
* Add secrets in **App Settings**
* Ensure `app.py` is the entry point

### ✅ Hugging Face Spaces

* Select **Streamlit** as SDK
* Add secrets in Space settings
* Ensure `requirements.txt` is present

---

## 🧠 Use Cases

* AI-powered chat assistants
* Agentic workflow demonstrations
* Tool-based reasoning systems
* AI news monitoring & summarization
* LLM experimentation playground

---

## ⚠️ Notes & Best Practices

* Avoid infinite loops in Streamlit apps
* Cache heavy LLM objects using `@st.cache_resource`
* Restrict model options per provider
* Never hardcode API keys
* Use session state for user interactions

---

## 🛣️ Future Enhancements

* Multi-agent collaboration
* Memory persistence (vector stores)
* More tool integrations
* User authentication
* Analytics dashboard

---

## 📜 License

This project is for **educational and experimental purposes**.
Feel free to fork and extend.

---

## 🙌 Author

**Mohd Humaid**
RPA Developer | Agentic AI & LLM Enthusiast

---

⭐ If you like this project, consider giving it a star!

```

---

If you want, I can also:
- shorten this for GitHub landing page
- add badges (Streamlit, Groq, Python)
- tailor it for recruiters / portfolio

Just tell me 👍
```
