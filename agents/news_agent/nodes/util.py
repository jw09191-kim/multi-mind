from dataclasses import dataclass
import re
from typing import List


@dataclass
class NewsArticle:
    title: str
    body: str
    url: str


def parse_articles(raw: str) -> List[NewsArticle]:
    if not raw.strip():
        return []

    articles = []

    # 각 뉴스 블록은 'Title:'로 시작하므로 이를 기준으로 분리
    blocks = raw.split("Title:")
    for block in blocks:
        if not block.strip():
            continue

        # 제목: 첫 줄
        title_match = re.search(r"^(.*?)\n", block)
        # 본문(Description)은 줄바꿈 포함 가능 (DOTALL 사용)
        body_match = re.search(r"Description:\s*(.*?)\nURL:", block, re.DOTALL)
        # URL은 줄 끝까지
        url_match = re.search(r"URL:\s*(https?://[^\s]+)", block)

        title = title_match.group(1).strip() if title_match else ""
        body = body_match.group(1).strip() if body_match else ""
        url = url_match.group(1).strip() if url_match else ""

        # 최소한 제목이나 본문이 있을 때만 추가
        if title or body:
            articles.append(NewsArticle(title=title, body=body, url=url))

    return articles
