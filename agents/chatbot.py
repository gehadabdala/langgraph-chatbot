from langchain_groq import ChatGroq
import os
from langchain_core.messages import SystemMessage
from dotenv import load_dotenv
from prompts.system_prompt import SYSTEM_PROMPT
from tools.tools import add, divide, multiply, subtract
from memory.conversation import trim_messages

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0,
)
llm_with_tools = llm.bind_tools([add, subtract, multiply, divide])


def chatbot(state):
    messages = trim_messages(state["messages"])
    print(f"Messages sent to LLM: {len(messages)}")

    system_msg = SystemMessage(content=SYSTEM_PROMPT)

    response = llm_with_tools.invoke([system_msg] + messages)

    return {"messages": [response]}
