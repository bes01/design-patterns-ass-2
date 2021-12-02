import random

import in_memory_data
from models import Item, ItemGroup, Sellable


class ProductFactory:
    def __init__(self) -> None:
        self.items = in_memory_data.ITEMS
        self.discounted_combos = in_memory_data.DISCOUNTED_COMBOS
        self.items_by_batch = in_memory_data.ITEMS_BY_BATCH

    def create_random_item(self) -> Sellable:
        return random.choice(
            [
                self.create_cheese,
                self.create_beer,
                self.create_bread,
                self.create_6x_beer_pack,
                self.create_bread_and_cheese_combo,
            ]
        )()

    def create_bread(self) -> Sellable:
        return self._create_item(0, True)

    def create_cheese(self) -> Sellable:
        return self._create_item(1, True)

    def create_beer(self) -> Sellable:
        return self._create_item(2, True)

    def create_6x_beer_pack(self) -> Sellable:
        item_group = self.items_by_batch[0]
        item = self._create_item(2, False)
        return ItemGroup(
            name=item_group["name"],
            discount=item_group["discount"],
            items=[item for _ in range(item_group["quantity"])],
        )

    def create_bread_and_cheese_combo(self) -> Sellable:
        item_combo = self.discounted_combos[0]
        item_1 = self._create_item(0, False)
        item_2 = self._create_item(0, False)
        return ItemGroup(
            name=item_combo["name"],
            discount=item_combo["discount"],
            items=[item_1, item_2],
        )

    def _create_item(self, index: int, discount: bool) -> Sellable:
        item = self.items[index]
        discount_amount = 0
        if discount:
            discount_amount = item["discount"]
        return Item(name=item["name"], price=item["price"], discount=discount_amount)
