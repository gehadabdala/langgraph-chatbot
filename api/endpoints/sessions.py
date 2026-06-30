from fastapi import APIRouter
from services.session_service import session_service
from schemas.session import (
    ConversationResponse,
    MessageResponse,
)

router = APIRouter(
    prefix="/sessions",
    tags=["Sessions"],
)


@router.post("/")
def create_session():

    thread_id = session_service.create_session()

    return {"thread_id": thread_id}


@router.get("/")
def get_sessions():

    return {"sessions": session_service.get_sessions()}


@router.get(
    "/{thread_id}",
    response_model=ConversationResponse,
)
def get_conversation(thread_id: str):

    conversation = session_service.get_conversation(thread_id)

    messages = [
        MessageResponse(
            role=role,
            content=content,
            created_at=created_at,
        )
        for role, content, created_at in conversation
    ]

    return ConversationResponse(
        thread_id=thread_id,
        messages=messages,
    )
