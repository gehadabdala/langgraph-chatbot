## Build my first graph built to understand the core concepts of workflow-based AI systems.

## Objective

Learn the fundamental building blocks of LangGraph before moving to:

- Memory
- Tool Calling
- Conditional Routing
- Multi-Agent Systems

## Workflow
START
  ↓
Chatbot Node
  ↓
END


## Project Structure

```text
langgraph-chatbot/
│
├── main.py
├── chatbot.py
├── state.py
└── .env
```

## state.py 
-All data in one notebook.

## what is the job of node?
اقرأ State
↓
اعمل حاجة
↓
حدث State
↓
رجعه

-pass the state as input -> def chatbot(state):
-شان أي Node في LangGraph لازم تعرف تتعامل مع الـ State كله.

## Graph
-أنا هبني Workflow بيتعامل مع State من نوع ChatState.
->>graph_builder = StateGraph(
    ChatState
)

## Node Registration
-add node using name "chatbot" and its code chatebot()

-graph_builder.add_node(
    "chatbot",
    chatbot
)

## Edge
-graph_builder.add_edge(
    START,
    "chatbot"
)
-ابدأ من هنا
↓
روح للـ chatbot
-بعدين
-graph_builder.add_edge(
    "chatbot",
    END
)
-بعد ما تخلص
انهي التنفيذ

## Compile
-before compile it just blueprint after compile real program.

## Invoke
-graph.invoke(...)
-هنا حصل التنفيذ الفعلي.

## Phase 2 -> Conditional Router
START
 ↓
route_question()
 ↓
يرجع:
math

أو

chatbot

## Phase 3 -> Memory + State Management
You: My name is Gehad

You: What is my name?

Bot: Your name is Gehad

-Stateless

كل Request لوحده.
-Request
↓
Response


-Stateful

فيه تاريخ.
-Request
↓
History
↓
Response

-->>manual memory is done.

## Phase 4 🚀 LangGraph Memory (Checkpointing)
-ا اللي بتخلي الـ chatbot “يفتكر بجد” مش مجرد list في بايثون.
-Persistent State Store ✅


## Phase 5 Advanced Tool-Calling Agent (LangGraph)
->> Workflow
User
 ↓
Router Node (optional)
 ↓
Agent Node (LLM decides)
 ↓
IF tool needed?
   ├── Tool Node (calculator / logic)
   ↓
Back to Agent
 ↓
Final Answer

## Phase 6 LLM-driven Tool Calling Workflow
ال LLM هيبدأ هنا يفكر وياخد قرار يستخدم Tool بنفسه بدل ما احنا نفرض عليه يروح لل Tool Executor.

-إحنا عايزين الـ LLM نفسه يقول:

أنا محتاج أستخدم Calculator.

وده بيكون في الـ Response.

يعني بدل ما يرجع:
The answer is 425
-هيرجع حاجه زي كده:
tool_call:
    name = calculator
    args = {
        "expression":"25*17"
    }
    ->دا  اسمه tool calling.

-بدل 
User
 │
 ▼
Router
 │
 ▼
Tool
-يكون ده 
User
 │
 ▼
LLM
 │
 │
 ├── لو مفيش Tool
 │        │
 │        ▼
 │      Answer
 │
 └── لو فيه Tool
          │
          ▼
     Tool Executor
          │
          ▼
        LLM
          │
          ▼
      Final Answer

->كده ال LLM هو اللي بقي Brain.


## Phase 7 Multi-Step Tool Reasoning Agent
-بدل ما نستخدم Tool واحده لا نقدر هنا نسخدم اكتر من واحده.
-هنحسن ففايل ال chatbot.py, tool_executor.py, graph.py

->tool = step في reasoning chain

## Phase 8 Agent Production
-Workflow:
User
 ↓
Chat Node (LLM + tool calling)
 ↓
Tool Router (decides execute or end)
 ↓
Tool Executor (runs tools safely)
 ↓
Chat Node (final answer synthesis)
 ↓
Memory (thread-aware)

->In this step Refactor graph structure into builder, routes, and state modules


## Phase 9 Memory Architecture
-التقسيمه كالتالي: 
User

      │
      ▼

Conversation

      │
      ▼

Short Memory
      │
      ▼

Summary Memory
      │
      ▼

Long Memory

## Phase 10 State Management
-To prevent:
Duplicate messages.
Bugs في الـ Memory.
Tool loops غريبة.
State غير متوقعة.


## Phase 11 Structured Output by Pydantic
إخراج منظم من الـ LLM (Pydantic Models) ✅.
-بدل The answer is 50.
-هيكون object منظم كده:
AgentResponse(
    answer="The answer is 50.",
    confidence=0.98,
    requires_followup=False,
)
-ودا هيكون هنا schemas/agent_response.py

## Phase 12 Structured output
-دي عملتها للمستقبل حاليا مش مستخدماها بس لو حبيت اطور المشروع يكون لموقع فيه AI assistant محتاج اجابه منظمه ومفصله مش مجرد string ساعتها هستخدمهز


## Phase 13 Streaming 
-دلوقتي ال agent شغال عندي كده:
User
   │
   ▼
LLM يفكر...
   │
   │ (3 ثواني)
   │
   ▼
يرجع الرد كله مرة واحدة

-بعد ما ال llm بيفكر بكام ثانيه بتطلع الاجابه كامله علي بعضها ودا بيحسس اليوزر ان ال agent ردوده بطيئه نوعا ما ف هنا جت فكره ال streaming وهي انه يبدأ يطلع الاجابه بالتدريج زي كده:
Ans
Answer
Answer is
Answer is ...
ودا بيحسس اليوزر ان ال agent اسرع حتي لو بياخد وقت عبال ما ال llm يجيب الاجابه.

## Phase 14 Async
-البرنامج يقف لحد ما الـ API ترد.
User
 │
 ▼
LLM
 │
 │
 │
 البرنامج واقف
 │
 │
 ▼
Response
-> ال async بقي بتخلي اليوزرز ينتظروا بس كلهم شغالين فنفس الوقت parallel


## Phase 15 FastAPI 
POST /chat
        │
        ▼
graph.invoke()
        │
        ▼
AI Response
        │
        ▼
JSON
->for running:
python -m uvicorn api.app:app --reload

## Phase 16 Dependency Injection
FastAPI
    │
Depends()
    │
ChatService
    │
Repository
    │
LLM

###
🔖 Latest
GLM-5.2

Claude-Opus-4-8

GPT-5.5

GPT-Image-2

DeepSeek-V4-Pro

Qwen3.7-Max

MiniMax-M3

Kimi-K2.7

OpenClaw

Hermes Agent
###