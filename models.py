from abc import abstractmethod, ABC
from typing import List


class Sellable(ABC):

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


class QuantitativeSellable(Sellable):

    def __init__(self, sellable: Sellable):
        self.sellable = sellable
        self.quantity = 1

    def get_name(self) -> str:
        return self.sellable.get_name()

    def get_price(self) -> float:
        return self.sellable.get_price() * self.quantity

    def get_single_item_price(self) -> float:
        return self.sellable.get_price()

    def get_quantity(self) -> int:
        return self.quantity

    def increment_quantity(self):
        self.quantity += 1


class Receipt:
    _products: dict[str, QuantitativeSellable] = {}

    def __init__(self):
        print("\nOpening new receipt...")

    def add_item(self, product: Sellable) -> None:
        if product.get_name() in self._products:
            self._products[product.get_name()].increment_quantity()
        else:
            self._products[product.get_name()] = QuantitativeSellable(product)

        print(f"Added: {product.get_name()}")

    def close_receipt(self) -> None:
        print("Closing receipt...")
        print("|--------------------|----------|----------|----------|")
        print("|        Name        |   Units  |   Price  |   Total  |")
        print("|--------------------|----------|----------|----------|")
        for product_name in self._products.keys():
            product = self._products[product_name]
            name = self._fill_with_whitespaces(product.get_name(), 20)
            units = self._fill_with_whitespaces(str(product.get_quantity()), 10)
            price = self._fill_with_whitespaces(str(product.get_single_item_price()), 10)
            total = self._fill_with_whitespaces(str(product.get_price()), 10)
            print(f'|{name}|{units}|{price}|{total}|')
            print("|--------------------|----------|----------|----------|")

    def _fill_with_whitespaces(self, word: str, length: int) -> str:
        fill_len = int((length - len(word)) / 2)
        fill_str = fill_len * ' '
        result = f'{fill_str}{word}{fill_str}'
        if len(result) > length:
            result = result[:length]
        elif len(result) < length:
            result += ' ' * (length - len(result))
        return result
