from typing import TypedDict, Annotated, List


class GraphState(TypedDict):
    query: Annotated[str, "query"]
    articles: Annotated[List[str], "articles"]
    summary: Annotated[str, "summary"]
