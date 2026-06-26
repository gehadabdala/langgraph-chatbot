from tools.tools import add, subtract, multiply, divide

available_tools = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}


def tool_executor(state):
    messages = state["messages"]
    last_message = messages[-1]

    tool_calls = last_message.tool_calls

    results = []

    for call in tool_calls:
        tool_name = call["name"]
        tool_args = call["args"]

        tool = available_tools.get(tool_name)

        if tool:
            result = tool.invoke(tool_args)
            results.append(result)

    return {"messages": messages + results}
