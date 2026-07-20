from app.database.connection import get_connection
from app.receipt.models import Receipt


def add_receipt(receipt: Receipt):
    """
    Insert a Receipt object into the database.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO receipts (
            receipt_date,
            store_name,
            receipt_number,
            currency,
            subtotal,
            tax,
            discount,
            total_amount
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            receipt.receipt_date,
            receipt.store_name,
            receipt.receipt_number,
            receipt.currency,
            receipt.subtotal,
            receipt.tax,
            receipt.discount,
            receipt.total_amount
        )
    )

    connection.commit()
    connection.close()