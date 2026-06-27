from langchain_groq import ChatGroq
import os
from langchain_core.messages import SystemMessage
from dotenv import load_dotenv
from config.settings import TIMEOUT
from prompts.system_prompt import SYSTEM_PROMPT
from tools.tools import add, divide, multiply, subtract
from memory.conversation import trim_messages

load_dotenv()
from config.settings import (
    GROQ_API_KEY,
    MODEL_NAME,
    TEMPERATURE,
    TIMEOUT,
)

llm = ChatGroq(
    model=MODEL_NAME,
    api_key=GROQ_API_KEY,
    temperature=TEMPERATURE,
    timeout=TIMEOUT,
)

llm_with_tools = llm.bind_tools([add, subtract, multiply, divide])


def chatbot(state):
    messages = trim_messages(state["messages"])
    print(f"Messages sent to LLM: {len(messages)}")

    system_msg = SystemMessage(content=SYSTEM_PROMPT)

    response = llm_with_tools.invoke([system_msg] + messages)

    return {"messages": [response]}
