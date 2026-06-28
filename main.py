from graph.builder import graph
from langchain_core.messages import HumanMessage
from memory.storage import load_conversation, save_message, storage

config = {"configurable": {"thread_id": "user-1"}}

# state = {"messages": []}
state = load_conversation(thread_id="user-1")

while True:

    user_input = input("You: ")
    save_message(
        thread_id="user-1",
        role="human",
        content=user_input,
    )

    state["messages"].append(HumanMessage(content=user_input))

    state = graph.invoke(state, config=config)

    assistant_reply = state["messages"][-1].content

    save_message(
        thread_id="user-1",
        role="assistant",
        content=assistant_reply,
    )

    print(assistant_reply)
