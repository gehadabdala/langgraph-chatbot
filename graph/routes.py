from langgraph.graph import END


def route_after_chatbot(state):
    last_message = state["messages"][-1]

    if getattr(last_message, "tool_calls", None):
        return "tool_executor"

    return END
