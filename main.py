from langgraph.graph import StateGraph
from langgraph.graph import START, END

from state import ChatState
from chatbot import chatbot

graph_builder = StateGraph(ChatState)

graph_builder.add_node("chatbot", chatbot)

graph_builder.add_edge(START, "chatbot")

graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()

from langchain_core.messages import HumanMessage

while True:

    user_input = input("You: ")

    result = graph.invoke({"messages": [HumanMessage(content=user_input)]})

    print(result["messages"][-1].content)
