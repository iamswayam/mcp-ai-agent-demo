# EZAuto MCP Learning

> A minimal end-to-end project for learning the **Model Context Protocol (MCP)** by building an AI-powered roadside assistance case management system using **FastMCP**, **SQLite**, and **Google Gemini 3.1 Flash Lite**.

---

## 🎯 Project Goal

This project was built to understand **how AI Agents communicate with external systems using MCP**.

Instead of using frameworks like LangChain or CrewAI, this project focuses on learning the fundamentals by implementing everything from scratch.

---

# Architecture

```text
                    User
                      │
                      ▼
        Gemini 3.1 Flash Lite
        (Function Calling)
                      │
                      ▼
          Python Tool Wrappers
                      │
                      ▼
        Official MCP ClientSession
                      │
                      ▼
            FastMCP Server
                      │
                      ▼
              SQLite Database
```

---

# Features

- SQLite database with 300 sample roadside assistance cases
- FastMCP Server exposing business tools
- Official MCP Client
- Gemini Function Calling
- Natural language querying
- AI powered tool selection
- End-to-end MCP communication

---

# Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.12 | Programming Language |
| SQLite | Database |
| FastMCP | MCP Server |
| MCP SDK | Official MCP Client |
| Google Gemini 3.1 Flash Lite | LLM |
| google-genai | Gemini SDK |

---

# Project Structure

```text
ezauto-mcp-learning/
│
├── database/
│   ├── schema.sql
│   ├── seed.py
│   └── ezauto.db
│
├── mcp_server/
│   └── server.py
│
├── client/
│   └── gemini_agent.py
│
├── requirements.txt
├── .env
└── README.md
```

---

# MCP Tools

| Tool | Description |
|------|-------------|
| get_total_cases() | Returns total number of cases |
| get_cases_by_status(status) | Returns cases for a given status |
| get_case_status_summary() | Returns grouped case counts |

---

# Example Questions

```text
How many cases are there?

How many CREATED cases are there?

How many ASSIGNED cases are there?

How many PENDING_ASSIGNMENT cases are there?

Give me the case status summary.

List all CLOSED cases.

How many cases are not escalated?
```

---

# Example Flow

```text
User
 │
 ▼
"How many cases are not escalated?"
 │
 ▼
Gemini understands intent
 │
 ▼
Calls get_total_cases()

Calls get_cases_by_status("ESCALATED")
 │
 ▼
FastMCP Server
 │
 ▼
SQLite
 │
 ▼
Returns results
 │
 ▼
Gemini reasons:

300 - 60 = 240
 │
 ▼
"There are 240 non-escalated cases."
```

---

# Learning Outcomes

This project demonstrates:

- Building an MCP Server
- Registering MCP Tools
- MCP Tool Discovery
- MCP Tool Execution
- SQLite Integration
- Gemini Function Calling
- AI Tool Selection
- Agent-to-Tool Communication

---

# Future Improvements

- Search cases by customer name
- Search by city
- Get case by ID
- Date range filtering
- Multi-step reasoning
- Conversation memory
- RAG integration
- PostgreSQL backend
- Vector search

---

# Lessons Learned

One of the biggest takeaways from this project was understanding that:

- **MCP standardizes communication between AI agents and external tools.**
- **LLMs are valuable not because they replace SQL, but because they understand human intent, choose the appropriate tools, reason over the returned data, and generate natural-language responses.**

---

# Acknowledgements

This project was built as part of a hands-on journey to understand the Model Context Protocol (MCP), Function Calling, and Agentic AI from first principles.