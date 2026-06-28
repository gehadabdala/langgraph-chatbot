from exceptions.handlers import handle_tool_error
from tools.tools import add, subtract, multiply, divide
from langchain_core.messages import ToolMessage
from utils.logger import logger
from tools.registry import AVAILABLE_TOOLS


def tool_executor(state):
    messages = state["messages"]
    last_message = messages[-1]

    tool_calls = last_message.tool_calls

    results = []

    for call in tool_calls:
        tool_name = call["name"]
        tool_args = call["args"]

        tool = AVAILABLE_TOOLS.get(tool_name)

        if tool:
            logger.info(f"Calling tool: {tool_name}")
            logger.info(f"Arguments: {tool_args}")

            try:
                result = tool.invoke(tool_args)

            except Exception as e:
                result = handle_tool_error(tool_name, e)

            logger.info(f"Result: {result}")

            results.append(ToolMessage(content=str(result), tool_call_id=call["id"]))

    return {"messages": messages + results}
