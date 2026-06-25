from langgraph.graph import StateGraph
from langgraph.graph import START, END

from nodes.math_node import math_node
from state import ChatState
from nodes.chatbot import chatbot

from nodes.router import route_question

graph_builder = StateGraph(ChatState)


graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("math", math_node)


graph_builder.add_conditional_edges(START, route_question)

graph_builder.add_edge("chatbot", END)
graph_builder.add_edge("math", END)

graph = graph_builder.compile()

conversation_history = []

from langchain_core.messages import HumanMessage

while True:

    user_input = input("You: ")

    conversation_history.append(HumanMessage(content=user_input))

    result = graph.invoke({"messages": conversation_history})

    conversation_history.append(result["messages"][-1])

    print(result["messages"][-1].content)
