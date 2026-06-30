# دا مجرد interface
from abc import ABC, abstractmethod


class ConversationRepository(ABC):

    @abstractmethod
    def save_message(
        self,
        thread_id: str,
        role: str,
        content: str,
    ):
        pass

    @abstractmethod
    def load_conversation(
        self,
        thread_id: str,
    ):
        pass

    @abstractmethod
    def delete_conversation(
        self,
        thread_id: str,
    ):
        pass
