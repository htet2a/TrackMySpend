from dataclasses import dataclass


@dataclass
class Receipt:
    """
    Represents a processed receipt.
    """

    receipt_date: str
    store_name: str
    receipt_number: str
    currency: str

    subtotal: float
    tax: float
    discount: float
    total_amount: float