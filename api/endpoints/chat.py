from fastapi import APIRouter

from schemas.chat import ChatRequest, ChatResponse
from fastapi import Depends

from dependencies.services import get_chat_service
from services.chat_service import ChatService

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(
    request: ChatRequest,
    chat_service: ChatService = Depends(get_chat_service),
):

    response = chat_service.chat(
        message=request.message,
        thread_id=request.thread_id,
    )

    return ChatResponse(response=response)
