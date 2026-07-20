from app.receipt.models import Receipt


receipt = Receipt(
    receipt_date="2026-07-20",
    store_name="Test Store",
    receipt_number="TEST001",
    currency="CAD",
    subtotal=10.00,
    tax=1.30,
    discount=0,
    total_amount=11.30
)


print(receipt)