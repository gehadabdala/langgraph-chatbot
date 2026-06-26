from langchain_core.tools import tool


@tool
def add(a: int, b: int):
    """Add two numbers."""
    return a + b


@tool
def subtract(a: int, b: int):
    """Subtract the second number from the first."""
    return a - b


@tool
def multiply(a: int, b: int):
    """Multiply two numbers."""
    return a * b


@tool
def divide(a: int, b: int):
    """Divide the first number by the second."""
    return a / b
