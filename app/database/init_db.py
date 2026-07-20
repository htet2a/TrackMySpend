from app.database.connection import get_connection
from app.utils.logger import get_logger


def initialize_database():
    """
    Initialize SQLite database and create tables.
    """

    logger = get_logger()

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS receipts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            receipt_date TEXT,
            store_name TEXT,
            receipt_number TEXT,
            currency TEXT,
            subtotal REAL,
            tax REAL,
            discount REAL,
            total_amount REAL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    connection.commit()
    connection.close()

    logger.info("Database initialized")