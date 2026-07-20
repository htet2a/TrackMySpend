import sqlite3

from app.utils.paths import get_project_path


def get_connection():
    """
    Create and return SQLite database connection.
    """

    database_path = get_project_path("data/trackmyspend.db")

    connection = sqlite3.connect(database_path)

    return connection