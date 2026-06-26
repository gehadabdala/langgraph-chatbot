from langchain_nvidia_ai_endpoints import ChatNVIDIA
import os
from langchain_core.messages import SystemMessage
from dotenv import load_dotenv
from tools.tools import add, divide, multiply, subtract
from tools.calculator import calculator

load_dotenv()

api_key = os.getenv("NVIDIA_API_KEY")
print("API KEY LOADED:", api_key is not None)

llm = ChatNVIDIA(model="meta/llama-3.1-70b-instruct", api_key=api_key, timeout=180)
llm_with_tools = llm.bind_tools([calculator])

tools = {"add": add, "multiply": multiply, "subtract": subtract, "divide": divide}


import json
from langchain_core.messages import SystemMessage


def chatbot(state):
    messages = state["messages"]

    system_msg = SystemMessage(content="""
You are an AI agent with tools.

Available tools:
- add(a, b)
- multiply(a, b)

If user asks a math question, respond ONLY in this format:
{"tool": "add", "args": {"a": 2, "b": 3}}

Otherwise respond normally.
""")

    response = llm_with_tools.invoke([system_msg] + messages)

    return {"messages": messages + [response]}
