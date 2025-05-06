from .state import GraphState
import os
import re
from pathlib import Path
from common.datetime import get_now_string


def parse_raw_articles(raw_text: str) -> list[dict]:
    """
    'Title: ...\nDescription: ...\nURL: ...' 형식의 뉴스 문자열 파싱
    """
    pattern = r"Title:\s*(.*?)\nDescription:\s*(.*?)\nURL:\s*(https?://[^\s]+)"
    matches = re.findall(pattern, raw_text, re.DOTALL)

    articles = []
    for title, description, url in matches:
        articles.append(
            {
                "title": title.strip(),
                "description": description.strip(),
                "url": url.strip(),
            }
        )

    return articles


def clean_summary(summary: str) -> str:
    """
    <think> 태그 제거
    """
    return re.sub(r"<think>.*?</think>", "", summary, flags=re.DOTALL).strip()


def save_to_markdown(articles: list[dict], summary: str, topic: str = "news"):
    """
    Markdown 형식으로 기사와 요약을 저장
    """
    timestamp = get_now_string()
    safe_topic = topic.replace(" ", "_").lower()

    dir_path = f"outputs/news/{safe_topic}"
    os.makedirs(dir_path, exist_ok=True)

    md = [f"# 📰 {topic} 뉴스 요약", ""]

    md.append("## 📌 뉴스 기사 목록")
    for article in articles:
        md.append(f"- **제목**: {article['title']}")
        md.append(f"  - **설명**: {article['description']}")
        md.append(f"  - **링크**: {article['url']}")
        md.append("")  # 줄바꿈

    md.append("\n---\n")
    md.append("## 🧾 전체 요약")
    md.append(clean_summary(summary))

    # 저장
    output_path = os.path.join(dir_path, f"news_{timestamp}.md")
    Path(output_path).write_text("\n".join(md), encoding="utf-8")


async def save_node(state: GraphState) -> GraphState:
    articles = parse_raw_articles("\n".join(state.get("articles", [])))
    summary = state.get("summary", "").strip()

    if articles and summary:
        save_to_markdown(
            articles=articles,
            summary=summary,
        )
    return state  # 상태 그대로 반환 (종단 노드로 사용 가능)
