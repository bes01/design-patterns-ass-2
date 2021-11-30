from abc import abstractmethod
from typing import List


class Sellable:

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_price(self) -> float:
        pass


# Single Product
class Item(Sellable):
    def __init__(self, *, name: str, price: float, discount: float):
        self.name = name
        self.price = price
        self.discount = discount

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price * (1 - self.discount)


# Pack or any combo with discount
class ItemGroup(Sellable):
    def __init__(self, *, name: str, discount: float, items: List[Sellable]):
        self.name = name
        self.discount = discount
        self.items = items

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return sum([item.get_price() for item in self.items]) * (1 - self.discount)
