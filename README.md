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
