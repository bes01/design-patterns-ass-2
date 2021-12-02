from abc import ABC, abstractmethod
from enum import Enum
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
        self.name: str = name
        self.price: float = price
        self.discount: float = discount

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price * (1 - self.discount)


# Pack or any combo with discount
class ItemGroup(Sellable):
    def __init__(self, *, name: str, discount: float, items: List[Sellable]):
        self.name: str = name
        self.discount: float = discount
        self.items: List[Sellable] = items

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return sum([item.get_price() for item in self.items]) * (1 - self.discount)


class QuantitativeSellable(Sellable):
    def __init__(self, sellable: Sellable):
        self._sellable: Sellable = sellable
        self._quantity: int = 1

    def get_name(self) -> str:
        return self._sellable.get_name()

    def get_price(self) -> float:
        return self._sellable.get_price()

    def get_quantity(self) -> int:
        return self._quantity

    def increment_quantity(self) -> None:
        self._quantity += 1

    def get_product(self) -> Sellable:
        return self._sellable


class Receipt:
    def __init__(self, is_report: bool = False):
        self.is_report = is_report
        self._products: dict[str, QuantitativeSellable] = {}
        if not self.is_report:
            print("\nOpening receipt...")

    def add_product(self, product: Sellable) -> None:
        if product.get_name() in self._products:
            self._products[product.get_name()].increment_quantity()
        else:
            self._products[product.get_name()] = QuantitativeSellable(product)

        if not self.is_report:
            print(f"Added: {product.get_name()}")

    def get_products(self) -> List[QuantitativeSellable]:
        return [self._products[key] for key in self._products.keys()]

    def close_receipt(self) -> None:
        if not self.is_report:
            print("Closing receipt...")
        print("|--------------------|----------|----------|----------|")
        print("|        Name        |   Units  |   Price  |   Total  |")
        print("|--------------------|----------|----------|----------|")
        for product_name in self._products.keys():
            product = self._products[product_name]
            name = self._fill_with_whitespaces(product.get_name(), 20)
            units = self._fill_with_whitespaces(str(product.get_quantity()), 10)
            price = self._fill_with_whitespaces(str(product.get_price()), 10)
            total = self._fill_with_whitespaces(
                str(product.get_price() * product.get_quantity()), 10
            )
            print(f"|{name}|{units}|{price}|{total}|")
            print("|--------------------|----------|----------|----------|")

    def _fill_with_whitespaces(self, word: str, length: int) -> str:
        fill_len = int((length - len(word)) / 2)
        fill_str = fill_len * " "
        result = f"{fill_str}{word}{fill_str}"
        if len(result) > length:
            result = result[:length]
        elif len(result) < length:
            result += " " * (length - len(result))
        return result


class PaymentMethod(Enum):
    CASH = "cash"
    CARD = "card"
