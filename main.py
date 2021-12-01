from models import Receipt
from product_factory import ProductFactory

factory = ProductFactory()

items = [factory.create_random_item() for _ in range(5)]

receipt = Receipt()
for item in items:
    receipt.add_item(item)
receipt.close_receipt()
