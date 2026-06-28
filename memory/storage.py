import sqlite3
from pathlib import Path
from langchain_core.messages import HumanMessage, AIMessage

DB_PATH = Path("memory/chat_history.db")


class ConversationStorage:

    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.create_table()

    def create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            thread_id TEXT NOT NULL,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        self.conn.commit()

    def save_message(self, thread_id: str, role: str, content: str):
        self.conn.execute(
            """
            INSERT INTO conversations(thread_id, role, content)
            VALUES (?, ?, ?)
            """,
            (thread_id, role, content),
        )
        self.conn.commit()

    def load_messages(self, thread_id: str):
        cursor = self.conn.execute(
            """
            SELECT role, content
            FROM conversations
            WHERE thread_id = ?
            ORDER BY id
            """,
            (thread_id,),
        )

        return cursor.fetchall()

    def load_conversation(self, thread_id: str):
        rows = self.load_messages(thread_id)

        messages = []

        for role, content in rows:
            if role == "human":
                messages.append(HumanMessage(content=content))

            elif role == "assistant":
                messages.append(AIMessage(content=content))

        return {"messages": messages}

    def delete_conversation(self, thread_id: str):
        self.conn.execute(
            """
            DELETE FROM conversations
            WHERE thread_id = ?
            """,
            (thread_id,),
        )
        self.conn.commit()

    def close(self):
        self.conn.close()


storage = ConversationStorage()


def save_message(thread_id: str, role: str, content: str):
    storage.save_message(thread_id, role, content)


def load_conversation(thread_id: str):
    return storage.load_conversation(thread_id)


def delete_conversation(thread_id: str):
    storage.delete_conversation(thread_id)
