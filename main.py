from product_factory import ProductFactory

factory = ProductFactory()

items = [factory.create_random_item() for _ in range(5)]

for item in items:
    print(f'{item.get_name()} - {item.get_price()}')
