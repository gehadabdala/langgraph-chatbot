from langchain_core.messages import HumanMessage

from graph.builder import graph
from memory.storage import (
    load_conversation,
    save_message,
)


class ChatService:

    def chat(
        self,
        message: str,
        thread_id: str,
    ) -> str:

        state = load_conversation(thread_id)

        save_message(
            thread_id=thread_id,
            role="human",
            content=message,
        )

        state["messages"].append(HumanMessage(content=message))

        state = graph.invoke(
            state,
            config={"configurable": {"thread_id": thread_id}},
        )

        answer = state["messages"][-1].content

        save_message(
            thread_id=thread_id,
            role="ai",
            content=answer,
        )

        return answer


chat_service = ChatService()
