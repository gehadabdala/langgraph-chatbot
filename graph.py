from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

from nodes.chatbot import chatbot
from tools.tool_executor import tool_executor
from state import ChatState

memory = MemorySaver()

graph_builder = StateGraph(ChatState)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tool_executor", tool_executor)

# 1. start → chatbot
graph_builder.add_edge(START, "chatbot")


# 2. chatbot decides: tool or end
def route(state):
    last = state["messages"][-1]

    # لو فيه tool calls → نروح ننفذ tools
    if hasattr(last, "tool_calls") and last.tool_calls:
        return "tool_executor"

    return END


graph_builder.add_conditional_edges("chatbot", route)


# 3. tool execution returns to chatbot
graph_builder.add_edge("tool_executor", "chatbot")


graph = graph_builder.compile(checkpointer=memory)
