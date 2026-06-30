from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    thread_id: str = "user-1"


class ChatResponse(BaseModel):
    response: str
