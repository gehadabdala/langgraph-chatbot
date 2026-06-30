from fastapi import FastAPI

from api.endpoints.chat import router as chat_router
from api.endpoints.sessions import router as session_router

app = FastAPI(
    title="LangGraph Agent",
    version="1.0.0",
)

app.include_router(chat_router)
app.include_router(session_router)
