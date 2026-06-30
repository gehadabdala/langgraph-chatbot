import uuid  # generate unique session IDs
from repositories.sqlite_repository import SQLiteRepository
from memory.storage import storage


class SessionService:

    def __init__(self, repository):
        self.repository = repository

    def create_session(self):
        return str(uuid.uuid4())

    def get_sessions(self):
        return self.repository.get_all_sessions()

    def get_conversation(self, thread_id: str):
        return self.repository.get_conversation(thread_id)


session_service = SessionService(SQLiteRepository())
