from .state import GraphState
from langchain.schema import HumanMessage
from models.ollama import model

PROMPT_TEMPLATE = """\
다음은 {query} 에 대한 관련 뉴스 기사들의 내용입니다.
각 뉴스의 핵심 내용을 간결하게 요약해줘. 중복된 내용은 묶어서 정리해도 좋아.

뉴스 목록:
{news}
"""


async def summarize_news(news_list: list[str], query: str) -> str:
    if not news_list:
        return "요약할 뉴스가 없습니다."

    news_text = "\n\n".join(news_list)
    prompt = PROMPT_TEMPLATE.format(query=query, news=news_text)

    response = await model.ainvoke([HumanMessage(content=prompt)])
    return response.content


async def summarize_node(state: GraphState) -> GraphState:
    summary = await summarize_news(state["articles"], query=state["query"])
    return {**state, "summary": summary}
