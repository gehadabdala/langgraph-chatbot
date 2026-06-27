from langchain_groq import ChatGroq
import os
from langchain_core.messages import SystemMessage
from dotenv import load_dotenv
from tools.tools import add, divide, multiply, subtract
from tools.calculator import calculator

load_dotenv()

api_key = os.getenv("NVIDIA_API_KEY")
print("API KEY LOADED:", api_key is not None)

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0,
)
llm_with_tools = llm.bind_tools([add, subtract, multiply, divide])

tools = {"add": add, "multiply": multiply, "subtract": subtract, "divide": divide}


import json
from langchain_core.messages import SystemMessage


def chatbot(state):
    messages = state["messages"]

    system_msg = SystemMessage(content="""
You are a helpful assistant with access to tools.

Use tools when needed to solve math problems.
Return natural answers.
""")

    response = llm_with_tools.invoke([system_msg] + messages)

    return {"messages": messages + [response]}
