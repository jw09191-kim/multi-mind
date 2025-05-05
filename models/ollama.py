from langchain_ollama import ChatOllama

# 모든 agent가 공유할 모델 (필요 시 다중 모델도 정의 가능)
model = ChatOllama(model="qwen3:4b", temperature=0.7)