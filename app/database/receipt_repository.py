from app.database.connection import get_connection


def add_receipt(
    receipt_date,
    store_name,
    receipt_number,
    currency,
    subtotal,
    tax,
    discount,
    total_amount
):
    """
    Insert a receipt into the database.
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
            receipt_date,
            store_name,
            receipt_number,
            currency,
            subtotal,
            tax,
            discount,
            total_amount
        )
    )

    connection.commit()

    connection.close()