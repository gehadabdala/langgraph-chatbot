from langchain_groq import ChatGroq
from config.settings import (
    GROQ_API_KEY,
    MODEL_NAME,
    TEMPERATURE,
    TIMEOUT,
)
from tools.registry import LLM_TOOLS

llm = ChatGroq(
    model=MODEL_NAME,
    api_key=GROQ_API_KEY,
    temperature=TEMPERATURE,
    timeout=TIMEOUT,
)

llm_with_tools = llm.bind_tools(LLM_TOOLS)


def invoke_llm(messages):
    return llm_with_tools.invoke(messages)
