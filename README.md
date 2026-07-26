# 🤖 Simple AI Agent with LangGraph & Ollama
This repository contains a lightweight, stateful AI Agent build using **LangGraph**, **LangChain**, and **Ollama**. The agent runs completely locally and maintains a conversation history with state management. It is designed as a foundational project to showcase advanced LLM orchestration for developer portfolios.


---

## 📊 Agent Architecture
The agent's workflow topology is designed as a directed graph using LangGraph, ensuring smooth state transitions between the user and the local model.

<p align="center">
    <img src="Agent Graph.png" alt="LangGraph Architecture Diagram" width="250">
</p>

- **`__start__`**: Initiates the execution flow when user input is captured.
- **`process`**: The core business logic node that invokes the local LLM (`qwen2.5:14b`) with the conversation state and processes the response.
- **`__end__`**: Safely terminates the execution loop after updating the shared state.

---

## ✨ Features

- **State Management**: Keeps track of message history efficiently across the session.
- **Local Execution**: Powered by Ollama (`qwen2.5`) for maximum privacy and zero API costs.
- **Session Loggin**: Automatically persists the conversation logs into a clean `logging.txt` file for debugging and validation.
- **Clean Architecture**: Built on top of core LangGraph semantic (Nodes and Workflow compilation).

---

##  📂 Project Structure

```text
|-- agent.py            # Main application logic and graph configuration
|-- requirements.txt    # Frozen list of core dependencies
|-- logging.txt         # Live demonstration logs of the agent's chats
|-- Agent Graph.pnd     # Visual workflow topology diagram
|-- README.md           # Documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have **Ollama** installed locally. Pull the optimized Qwen model before running the application:
```bash
ollama run qwen2.5:14b
```
*(Note: If you are constrained by VRAM under 12GB, switch to `qwen2.5:7b` inside `agent.py`)*

### 2. Installation
Clone the repository, create a virtual environment, and install the verified project dependencies:
```bash
# Clone repository
git clone <https://github.com/sourov-roy-ovi/simple-ai-agent.git>
cd <SIMPLE AI AGENT>

# Setup Virtual Environment
python -m venv myvenv
source myvenv/bin/scripts/activate  # On Windows: .\myvenv\Scripts\activate

# Install Dependencies
pip install -r requirements.txt
```

### 3. Run the Agent
Run the interactive command-line loop:
```bash
python agent.py
```

---

## 📝 Conversation Logs (Proof of Concept)
To check how the agent maintains context, handles query workflows, and responds in real-time, please inspect the [`logging.txt`](./logging.txt) file generated automatically in this repository.