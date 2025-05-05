from .graph import news_agent
from common.logger import get_logger
import asyncio

logger = get_logger("news_agent")


async def main():
    query = "이더리움 뉴스 최신 동향 알려줘"
    result = await news_agent.ainvoke({"query": query})

    logger.info(f"🔎 {len(result['articles'])}개 뉴스 검색 완료")
    logger.info("📝 뉴스 요약 완료")


if __name__ == "__main__":
    asyncio.run(main())
