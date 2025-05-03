# 🧠 LLM Agent System

멀티 에이전트 기반의 시장 분석 시스템으로, 뉴스와 차트 데이터를 수집하고 상승/하락 시나리오를 판단한 후 실제 결과와 비교하여 피드백을 생성합니다.  
LangGraph, MCP, Ollama를 기반으로 구현되며, 논리 평가 및 복기 루프까지 포함한 폐루프형 시스템입니다.

---

## 🧠 구조 다이어그램

```mermaid
graph TD
    subgraph Input_Collection
        A1["User Request"] --> A2["Input Validator"]
        A2 --> B1["News Agent"]
        A2 --> B2["Stock Agent"]
    end

    subgraph Interpretation_Layer
        B1 --> C1["Optimistic Agent - Trend Focus"]
        B2 --> C1

        B1 --> C2["Pessimistic Agent - Risk Focus"]
        B2 --> C2
    end

    subgraph Evaluation_Layer
        C1 --> D1["Logic Evaluator"]
        C2 --> D1
        D1 --> D2["Confidence Scorer"]
        D2 --> D3["Judge Agent - Buy / Hold / Sell"]
    end

    D3 --> E1["Final Verdict Output"]

    subgraph Retrospective_Feedback_T+1
        F1["Actual Market Movement"] --> F2["Review Agent"]
        D3 --> F2
        F2 --> F3["Chain-of-Thought Review"]
        F3 --> G["Prompt or Weight Adjustment"]
        G --> D3
    end
