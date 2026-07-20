from app.receipt.processor import inspect_receipt_file


result = inspect_receipt_file(
    "receipts/incoming/test_receipt.jpg"
)

print(result)