from pydantic import BaseModel


class MessageResponse(BaseModel):
    role: str
    content: str
    created_at: str


class ConversationResponse(BaseModel):
    thread_id: str
    messages: list[MessageResponse]
