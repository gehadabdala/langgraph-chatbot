from langgraph.graph import StateGraph, START
from langgraph.checkpoint.memory import MemorySaver

from graph.state import ChatState
from graph.routes import route_after_chatbot

from agents.chatbot import chatbot
from tools.tool_executor import tool_executor

memory = MemorySaver()

graph_builder = StateGraph(ChatState)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tool_executor", tool_executor)

graph_builder.add_edge(START, "chatbot")

graph_builder.add_conditional_edges(
    "chatbot", route_after_chatbot, {"tool_executor": "tool_executor", "end": "end"}
)

graph_builder.add_edge("tool_executor", "chatbot")

graph = graph_builder.compile(checkpointer=memory)
