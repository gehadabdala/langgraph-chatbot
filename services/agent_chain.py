from prompts.chat_prompt import chat_prompt
from services.llm_service import llm_with_tools

agent_chain = chat_prompt | llm_with_tools
