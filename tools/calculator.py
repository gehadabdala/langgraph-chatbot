from langchain_core.tools import tool


@tool
def calculator(expression: str) -> str:
    """
    Evaluate a mathematical expression.
    Example:
    2+2
    15*7
    100/5
    """

    return str(eval(expression))
