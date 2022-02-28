import sqlite3
from typing import Callable
from pathlib import Path


class IDB:
    def __init__(self, dbPath: Path):
        self._host = str(dbPath)

    def executer(self, func: Callable, params: dict = None):
        with DatabaseConnection(self._host) as connection:
            cursor = connection.cursor()
            if params is None:
                return func(cursor)
            else:
                return func(cursor, **params)


class DatabaseConnection:
    def __init__(self, host: str):
        self.connection = None
        self.host = host

    def __enter__(self) -> sqlite3.Connection:
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
