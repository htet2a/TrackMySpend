from app.database.receipt_repository import add_receipt
from app.receipt.models import Receipt


receipt = Receipt(
    receipt_date="2026-07-20",
    store_name="Model Test Store",
    receipt_number="MODEL001",
    currency="CAD",
    subtotal=20.00,
    tax=2.60,
    discount=0,
    total_amount=22.60
)


add_receipt(receipt)

print("Receipt model saved successfully")