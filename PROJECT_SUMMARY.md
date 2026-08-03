# EZAuto MCP Learning Project Summary

## Goal

Build a simple database-backed MCP project to understand SQLite, MCP
Server, MCP Client, Gemini Function Calling, and Agentic AI
fundamentals.

## Original Plan

User -\> Gemini -\> MCP -\> SQLite

## Project Structure

-   database/
-   mcp_server/
-   client/
-   requirements.txt
-   .gitignore

## Completed

-   SQLite schema and seed data (\~300 cases)
-   FastMCP server
-   MCP tools:
    -   get_total_cases
    -   get_cases_by_status
    -   get_case_status_summary
-   MCP client
-   Tool discovery
-   Tool execution

## Problems Encountered

### 1. Wrong MCP Version

Started with mcp 2.x while following examples written for the older API.
Resolved by using: - mcp==1.29.0 - fastmcp==3.4.5

### 2. Gemini + FastMCP Client

Tried: Gemini -\> FastMCP Client -\> MCP Server

Error: TypeError: cannot pickle '\_asyncio.Future' object

### 3. Gemini + Official ClientSession

Replaced FastMCP Client with official mcp.ClientSession. The identical
error occurred.

### 4. Root Cause

The traceback showed google-genai performing
config.model_copy(deep=True), which attempts to deepcopy a live
ClientSession containing asyncio state.

### 5. Revised Design

Instead of passing ClientSession directly into Gemini, use async Python
wrapper functions.

Final architecture:

User -\> Gemini Function Calling -\> Python Wrapper -\> MCP
ClientSession -\> FastMCP Server -\> SQLite

## Working Features

-   Total cases
-   Cases by status
-   Status summary
-   Natural language queries such as:
    -   How many cases are there?
    -   How many CREATED cases are there?
    -   List all CLOSED cases.
    -   How many cases are not escalated?

## What Was Learned

### MCP

-   Server
-   Client
-   Tool registration
-   Tool discovery
-   Tool execution

### Gemini

-   Automatic function calling
-   Async wrapper functions

### Agentic AI

Current stage: User -\> Gemini -\> Tool Selection -\> MCP -\> Database

Next: - More tools - Multi-step reasoning - Planning - Memory - RAG -
Vector databases

## Key Lesson

The LLM is not replacing SQL. Its value is understanding natural
language, selecting the correct tools, reasoning over tool outputs, and
presenting the answer naturally.

## Current Status

MCP learning phase completed. Project now moves into Agentic AI concepts
built on top of MCP.
