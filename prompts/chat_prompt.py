from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from prompts.system_prompt import SYSTEM_PROMPT

chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),
        MessagesPlaceholder("messages"),
    ]
)
