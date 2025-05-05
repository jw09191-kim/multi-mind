from langgraph.graph import StateGraph
from .nodes.search_node import search_node
from .nodes.summarize_node import summarize_node
from .nodes.save_node import save_node
from .nodes.state import GraphState

builder = StateGraph(GraphState)

builder.add_node("search_node", search_node)
builder.add_node("summarize_node", summarize_node)
builder.add_node("save_node", save_node)

builder.set_entry_point("search_node")
builder.add_edge("search_node", "summarize_node")
builder.add_edge("summarize_node", "save_node")

news_agent = builder.compile()
