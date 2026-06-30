from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph.message import add_messages
from langgraph.graph import MessagesState


class ChatState(MessagesState):
    pass
