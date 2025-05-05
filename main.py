import asyncio
from agents.news_agent.search import search_news

async def main():
    result = await search_news()
    for i, msg in enumerate(result, start=1):
        print(f"\n📄 뉴스 {i}:\n{msg}")

if __name__ == "__main__":
    asyncio.run(main())