"""
A basic module abstracting common access patterns to a SQLite3
database
"""

import abc


class Database(abc.ABC):
    @abc.abstractmethod
    @property
    def name(self) -> str:
        pass

    @abc.abstractmethod
    def tables(self):
        pass

    @abc.abstractmethod
    @property
    def cursor(self):
        pass

    @abc.abstractmethod
    def commit(self):
        pass


class Column:
    def __init__(self, name):
        self.name = name


class Query:
    def __init__(self, cursor, *query: tuple[str, ...]) -> None:
        self.query = query[0]
        self.multiple = False
        if len(query) > 1:
            self.vals = query[1]
            self.multiple = True
        self.cursor = cursor

    def execute(self):
        if not self.multiple:
            self.cursor.execute(self.query)
            rows = self.cursor.fetchall()
            return Results(rows)  # ty:ignore[unresolved-reference]  # noqa: F821

        else:
            self.execute_multiple(self.vals)

    def execute_multiple(self, vals):
        self.cursor.executemany(self.query, vals)
