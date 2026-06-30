# هستخدمه لو بعمل ai assistant لموقع وعايزه الاجابه متكونش مجرد نص لا تكون منظمه ومفصله
from langchain_core.messages import AIMessage

from services.structured_llm import structured_llm
from exceptions.handlers import handle_llm_error
from prompts.chat_prompt import chat_prompt
from memory.conversation import trim_messages

structured_chain = chat_prompt | structured_llm


def structured_agent(state):
    messages = trim_messages(state["messages"])

    try:
        response = structured_chain.invoke({"messages": messages})

        return {"messages": [AIMessage(content=response.answer)]}

    except Exception as e:
        return {"messages": [AIMessage(content=handle_llm_error(e))]}
