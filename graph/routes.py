from langgraph.graph import END


def route_after_chatbot(state):
    last = state["messages"][-1]

    if hasattr(last, "tool_calls") and last.tool_calls:
        return "tool_executor"

    return END
