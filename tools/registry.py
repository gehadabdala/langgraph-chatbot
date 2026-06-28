from tools.tools import add, subtract, multiply, divide

AVAILABLE_TOOLS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}

LLM_TOOLS = list(AVAILABLE_TOOLS.values())
