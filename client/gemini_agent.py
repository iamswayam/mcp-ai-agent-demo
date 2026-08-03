import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

MODEL = "gemini-3.1-flash-lite"

SERVER_SCRIPT = (
    Path(__file__).parent.parent
    / "mcp_server"
    / "server.py"
)

session: ClientSession | None = None


async def get_total_cases() -> str:
    """
    Returns the total number of cases.
    """
    result = await session.call_tool(
        "get_total_cases",
        {}
    )

    return result.content[0].text


async def get_cases_by_status(status: str) -> str:
    """
    Returns all cases for a given status.
    """

    result = await session.call_tool(
        "get_cases_by_status",
        {
            "status": status
        }
    )

    return result.content[0].text


async def main():

    global session

    gemini = genai.Client(
        api_key=os.environ["GEMINI_API_KEY"]
    )

    server_params = StdioServerParameters(
        command="python",
        args=[str(SERVER_SCRIPT)],
    )

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as s:

            session = s

            await session.initialize()

            chat = gemini.aio.chats.create(
                model=MODEL,
                config=types.GenerateContentConfig(
                    temperature=0,
                    tools=[
                        get_total_cases,
                        get_cases_by_status,
                        get_case_status_summary
                    ],
                ),
            )

            print("\nEZAuto Agent Ready\n")

            while True:

                question = input("You : ")

                if question.lower() == "exit":
                    break

                response = await chat.send_message(question)

                print("\nAssistant:")
                print(response.text)
                print()



async def get_case_status_summary() -> str:
    """
    Returns the number of cases for every status.
    """

    result = await session.call_tool(
        "get_case_status_summary",
        {}
    )

    return result.content[0].text


if __name__ == "__main__":
    asyncio.run(main())