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
