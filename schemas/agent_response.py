from pydantic import BaseModel, Field


class AgentResponse(BaseModel):
    answer: str = Field(description="Final response to the user.")

    confidence: float = Field(ge=0, le=1, description="Confidence score.")

    requires_followup: bool = Field(description="Whether another question is needed.")
