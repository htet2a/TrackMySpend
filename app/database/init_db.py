from app.database.connection import get_connection
from app.utils.logger import get_logger


def initialize_database():
    """
    Initialize SQLite database.
    """

    logger = get_logger()

    connection = get_connection()

    connection.close()

    logger.info("Database initialized")