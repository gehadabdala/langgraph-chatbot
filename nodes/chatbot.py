from dotenv import load_dotenv
from langchain_nvidia_ai_endpoints import ChatNVIDIA
import os

load_dotenv()
os.environ["NVIDIA_API_KEY"] = os.getenv("NVIDIA_API_KEY")

llm = ChatNVIDIA(model="meta/llama-3.1-70b-instruct")


def chatbot(state):

    response = llm.invoke(state["messages"])

    return {"messages": [response]}
