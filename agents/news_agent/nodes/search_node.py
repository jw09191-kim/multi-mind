import os
from .state import GraphState
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from models.ollama import model

load_dotenv()  # .env 로드
BRAVE_API_KEY = os.environ.get("BRAVE_API_KEY")


async def search_news(query: str = "비트코인 뉴스 최신 내용 검색해줘") -> list[str]:
    server_params = StdioServerParameters(
        command="docker",
        args=[
            "run",
            "-i",
            "--rm",
            "-e",
            f"BRAVE_API_KEY={BRAVE_API_KEY}",
            "mcp/brave-search:latest",
        ],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            agent = create_react_agent(model, tools)
            result = await agent.ainvoke(
                {"messages": [{"role": "user", "content": query}]}
            )
            return [msg.content for msg in result["messages"]]


async def search_node(state: GraphState) -> GraphState:
    news = await search_news(state["query"])
    return {**state, "articles": news}
