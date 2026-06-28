from langchain_core.messages import AIMessage, SystemMessage

from exceptions.handlers import handle_llm_error
from prompts.system_prompt import SYSTEM_PROMPT
from memory.conversation import trim_messages
from services.llm_service import invoke_llm
from utils.logger import logger


def chatbot(state):
    messages = trim_messages(state["messages"])

    logger.info(f"Messages sent to LLM: {len(messages)}")

    system_msg = SystemMessage(content=SYSTEM_PROMPT)

    try:
        response = invoke_llm([system_msg] + messages)

    except Exception as e:
        return {"messages": [AIMessage(content=handle_llm_error(e))]}

    return {"messages": [response]}
