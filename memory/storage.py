# دلوقتي بقي مجرد wrapper
from repositories.factory import get_repository

storage = get_repository()


def save_message(
    thread_id: str,
    role: str,
    content: str,
):
    storage.save_message(
        thread_id=thread_id,
        role=role,
        content=content,
    )


def load_conversation(
    thread_id: str,
):
    return storage.load_conversation(thread_id)


def delete_conversation(
    thread_id: str,
):
    storage.delete_conversation(thread_id)
