# AI Math Agent

An AI-powered mathematical assistant built with LangChain and Google Gemini.

---

## Description

AI Math Agent is an intelligent chatbot that uses Google Gemini and LangChain to solve mathematical expressions accurately.

Instead of relying on the LLM's own calculations, the agent uses a custom calculator tool powered by SymPy for accurate mathematical operations.

The project also implements a custom conversation memory system that allows the AI to remember previous messages during the conversation.

---

## Features

* 🤖 AI Agent powered by Google Gemini
* 🔧 Custom tool calling using LangChain
* 🧮 Accurate mathematical calculations using SymPy
* 🧠 Custom conversation memory system
* 💬 Maintains chat history during runtime
* 🏗️ Clean modular architecture
* 🔐 Secure API key management using environment variables

---

## How It Works

```
User Input
     |
     v
Human Message
     |
     v
AI Agent (Gemini)
     |
     v
Tool Required?
     |
  +--+--+
  |     |
 No    Yes
  |     |
  v     v
Answer  Calculator Tool
             |
             v
        Tool Response
             |
             v
        Final AI Response
```

---

## Project Structure

```
AI-Math-Agent/
│
├── agent.py              # Agent workflow and tool handling
├── tools.py              # Calculator tool implementation
├── memory.py             # Custom conversation memory
├── config.py             # Configuration management
├── main.py               # Application entry point
├── requirements.txt      # Project dependencies
├── .env.example          # Environment variable template
├── .gitignore            # Git ignored files
└── README.md             # Documentation
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/ridazahra-ai/AI-Math-Agent.git
```

### Navigate to Project Folder

```bash
cd AI-Math-Agent
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Setup

Create a `.env` file in the project directory.

Add your Google Gemini API key:

```env
GOOGLE_API_KEY=your_api_key_here
MODEL_NAME=gemini-2.5-flash
```

---

## Usage

Run the application:

```bash
python main.py
```

Example:

```
You: What is 25 * 17?

AI: The answer is 425.
```

Example with memory:

```
You: My name is Rida.

AI: Nice to meet you, Rida.

You: What is my name?

AI: Your name is Rida.
```

---

## Technologies Used

* Python
* LangChain
* Google Gemini API
* LangChain Google GenAI
* SymPy
* python-dotenv

---

## Concepts Implemented

* Large Language Model (LLM) Integration
* AI Agent Workflow
* Tool Calling
* Custom Conversation Memory
* Message-Based Conversation Handling
* Environment Configuration
* Modular Software Architecture

---

## Future Improvements

* Implement LangGraph agent workflow
* Add persistent database memory
* Support multiple tools
* Improve error handling
* Build FastAPI backend
* Add frontend interface
* Deploy as a cloud-based AI service

---

## License

MIT License
