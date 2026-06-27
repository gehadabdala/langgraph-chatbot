from graph.builder import graph
from langchain_core.messages import HumanMessage

config = {"configurable": {"thread_id": "user-1"}}

state = {"messages": []}

while True:

    user_input = input("You: ")

    state["messages"].append(HumanMessage(content=user_input))

    state = graph.invoke(state, config=config)

    print(state["messages"][-1].content)
