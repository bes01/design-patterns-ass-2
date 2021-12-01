from abc import ABC, abstractmethod
from typing import List

from models import Receipt, Sellable, PaymentMethod


class Subject(ABC):

    @abstractmethod
    def attach(self, observer: "Observer") -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class Observer(ABC):

    @abstractmethod
    def update(self) -> None:
        pass


class Report(Observer):

    def __init__(self):
        self._served_customer_count: int = 0
        self._CUSTOMER_AMOUNT_FOR_REPORT: int = 0  # Child class should specify this field

    def update(self) -> None:
        if self._CUSTOMER_AMOUNT_FOR_REPORT == 0:
            raise RuntimeError('Child class should have specified CUSTOMER_AMOUNT_FOR_REPORT')
        self._served_customer_count += 1
        if self._served_customer_count % self._CUSTOMER_AMOUNT_FOR_REPORT == 0:
            self.report_logic()

    @abstractmethod
    def report_logic(self) -> None:
        pass


class XReport(Report):

    def __init__(self, pos: "PointOfSales"):
        super().__init__()
        self.pos: "PointOfSales" = pos
        self._CUSTOMER_AMOUNT_FOR_REPORT: int = 20

    def report_logic(self) -> None:
        print('\n#######################################################')
        print('Starting X Report...')
        receipts = self.pos.get_receipts()
        summary_receipt = Receipt(True)
        for receipt in receipts:
            for product in receipt.get_products():
                for _ in range(product.get_quantity()):
                    summary_receipt.add_product(product.get_product())
        summary_receipt.close_receipt()
        print('X Report ended successfully')


class ZReport(Report):

    def __init__(self, pos: "PointOfSales"):
        super().__init__()
        self.pos: "PointOfSales" = pos
        self._CUSTOMER_AMOUNT_FOR_REPORT: int = 100

    def report_logic(self) -> None:
        print('\n#######################################################')
        print('Starting Z Report...')
        print('Clearing cash registers...')
        self.pos.end_shift()
        print('Z Report ended successfully')


class PointOfSales(Subject):

    def __init__(self, *, MAXIMUM_SHIFTS: int):
        self._observers: List[Observer] = []
        self._receipts: List[Receipt] = []
        self._shift_count: int = 0
        self.MAXIMUM_SHIFTS: int = MAXIMUM_SHIFTS

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update()

    def end_shift(self) -> None:
        self._receipts.clear()
        self._shift_count += 1

    def get_receipts(self) -> List[Receipt]:
        return self._receipts

    def serve_customer(self, cart: List[Sellable], payment_method: PaymentMethod) -> bool:
        if self._shift_count < self.MAXIMUM_SHIFTS:
            print('\n*******************************************************')
            print('Serving customer...')
            print(f'Payment method: {payment_method.value}')
            new_receipt = Receipt()
            for product in cart:
                new_receipt.add_product(product)
            new_receipt.close_receipt()
            self._receipts.append(new_receipt)
            self.notify()
            return True

        print(f'\nMaximum shifts count exceeded - {self.MAXIMUM_SHIFTS}')
        return False
