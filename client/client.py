import asyncio
from pathlib import Path

from fastmcp import Client
from fastmcp.client.transports import StdioTransport

SERVER_PATH = (
    Path(__file__).parent.parent
    / "mcp_server"
    / "server.py"
)

transport = StdioTransport(
    command="python",
    args=[str(SERVER_PATH)],
    cwd=str(Path(__file__).parent.parent),
)

client = Client(transport)


async def main():
    async with client:
        tools = await client.list_tools()

        print("\nAvailable Tools:\n")

        for tool in tools:
            print(f"\nTool: {tool.name}")
            print(f"Description: {tool.description}")
            print(f"Input Schema: {tool.inputSchema}")

        result = await client.call_tool(
            "get_cases_by_status",
            {
                "status": "ESCALATED"
            }
        )

        print("\nEscalated Cases:\n")

        for case in result.data:
            print(case)


asyncio.run(main())