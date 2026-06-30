from config.database import DATABASE_TYPE

from repositories.sqlite_repository import SQLiteRepository


def get_repository():

    if DATABASE_TYPE == "sqlite":
        return SQLiteRepository()

    raise ValueError(f"Unsupported database type: {DATABASE_TYPE}")
