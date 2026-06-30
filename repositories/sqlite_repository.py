# هنا هنحط الكود اللي كان ف storage.py

import sqlite3
from pathlib import Path
from langchain_core.messages import HumanMessage, AIMessage

from repositories.conversation_repository import ConversationRepository

DB_PATH = Path("memory/chat_history.db")


class SQLiteRepository(ConversationRepository):

    def __init__(self):
        # self.conn = sqlite3.connect(DB_PATH)
        self.create_table()

    def _get_connection(self):
        return sqlite3.connect(DB_PATH)

    def create_table(self):
        with self._get_connection() as conn:

            conn.execute("""
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                thread_id TEXT NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)
            conn.commit()

    def save_message(
        self,
        thread_id,
        role,
        content,
    ):

        with self._get_connection() as conn:

            conn.execute(
                """
                INSERT INTO conversations(
                    thread_id,
                    role,
                    content
                )

                VALUES(?,?,?)
                """,
                (
                    thread_id,
                    role,
                    content,
                ),
            )

            conn.commit()

    def load_messages(
        self,
        thread_id,
    ):

        with self._get_connection() as conn:

            cursor = conn.execute(
                """
                SELECT role,content

                FROM conversations

                WHERE thread_id=?

                ORDER BY id
                """,
                (thread_id,),
            )

            return cursor.fetchall()

    def load_conversation(
        self,
        thread_id,
    ):

        rows = self.load_messages(thread_id)

        messages = []

        for role, content in rows:

            if role == "human":
                messages.append(HumanMessage(content=content))

            elif role == "ai":
                messages.append(AIMessage(content=content))

        return {"messages": messages}

    def delete_conversation(
        self,
        thread_id,
    ):

        with self._get_connection() as conn:

            conn.execute(
                """
                DELETE FROM conversations

                WHERE thread_id=?
                """,
                (thread_id,),
            )

        conn.commit()

    def close(self):
        self.conn.close()

    def get_all_sessions(self):

        cursor = self._get_connection().execute("""
            SELECT DISTINCT thread_id
            FROM conversations
            ORDER BY id DESC
            """)

        return [row[0] for row in cursor.fetchall()]

    def get_conversation(self, thread_id: str):

        cursor = self._get_connection().execute(
            """
            SELECT role, content, created_at
            FROM conversations
            WHERE thread_id = ?
            ORDER BY id
            """,
            (thread_id,),
        )

        return cursor.fetchall()
