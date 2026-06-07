# Twitter Reflection Agent

> Transform rough ideas into **viral-ready tweets** using an AI-powered reflection loop.

## 📖 Overview

**Twitter Reflection Agent** is an AI agent that takes a rough, unpolished idea and automatically refines it into a high-quality, engaging tweet — through an iterative **Generate → Reflect → Improve** loop.

Instead of getting one AI-generated tweet, the agent:
1. ✍️ **Generates** a tweet from your idea
2. 🔍 **Reflects** on it like a viral Twitter influencer would
3. 🔄 **Improves** it based on the critique
4. Repeats until the tweet is polished ✅

---

## 🧠 Architecture

The agent is built using a **LangGraph StateGraph** with two nodes that loop conditionally:

```
         ┌─────────────────────────────────┐
         │                                 │
  Input ──▶  [ GENERATE ]  ──────────────▶  END
                  ▲          (> 6 messages)
                  │
             [ REFLECT ]
                  │
         feedback as HumanMessage
```

| Node | Role |
|---|---|
| `GENERATE` | Writes or improves the tweet based on the conversation history |
| `REFLECT` | Critiques the tweet on virality, length, style, and tone |
| `should_continue` | Stops the loop after **3 reflection cycles** |

---

## 📂 Project Structure

```
twitter-reflection-agent/
│
├── main.py        # LangGraph graph definition and agent entry point
├── chains.py      # Prompt templates and LLM chain definitions
├── flow.png       # Auto-generated agent flow visualization
├── .env           # Environment variables (not committed)
├── .gitignore     # Ignores .env and other sensitive files
└── README.md      # Project documentation
```
