from langchain_core.messages import AIMessage

from exceptions.handlers import handle_llm_error
from prompts.chat_prompt import chat_prompt
from memory.conversation import trim_messages
from services.agent_chain import agent_chain
from utils.logger import logger


def chatbot(state):
    messages = trim_messages(state["messages"])

    logger.info(f"Messages sent to LLM: {len(messages)}")

    try:
        response = agent_chain.invoke({"messages": messages})

    except Exception as e:
        return {"messages": [AIMessage(content=handle_llm_error(e))]}

    return {"messages": [response]}
