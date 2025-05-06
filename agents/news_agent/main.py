import asyncio
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryMemory
from models.ollama import model
from .graph import news_agent
from .nodes.state import GraphState
from common.logger import get_logger

import re


def remove_think_blocks(text: str) -> str:
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()


logger = get_logger("interactive_news_agent")

memory = ConversationSummaryMemory(llm=model)
conversation = ConversationChain(llm=model, memory=memory, verbose=False)


async def run_news_agent(query: str):
    try:
        result = await news_agent.ainvoke({"query": query})
        return result
    except Exception as e:
        logger.error(f"[❌ ERROR] Failed to run news agent: {e}")
        return None


async def main():
    print("🗞️  Interactive News Agent. Type 'bye', 'exit' or 'quit' to quit.")
    while True:
        print("🗣️  Question: ")
        user_input = input().strip()

        if user_input.lower() in ("bye", "exit", "quit"):
            print("👋  Goodbye!")
            break

        result = await run_news_agent(user_input)
        # memory 업데이트
        memory.chat_memory.add_user_message(user_input)
        memory.chat_memory.add_ai_message(result)

        followup = conversation.predict(input=f"{user_input}")
        clean_followup = remove_think_blocks(followup)

        print(f"🤖  Follow-up: {clean_followup}")


if __name__ == "__main__":
    asyncio.run(main())
