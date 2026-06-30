from services.llm_service import llm
from schemas.agent_response import AgentResponse

structured_llm = llm.with_structured_output(AgentResponse)
