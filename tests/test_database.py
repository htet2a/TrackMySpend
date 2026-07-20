from app.database.receipt_repository import add_receipt


add_receipt(
    "2026-07-20",
    "Test Store",
    "TEST001",
    "CAD",
    10.00,
    1.30,
    0,
    11.30
)

print("Test receipt inserted")