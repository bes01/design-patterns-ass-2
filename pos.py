from abc import ABC, abstractmethod
from typing import List


class Subject(ABC):

    @abstractmethod
    def attach(self, observer: "Observer") -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class Observer(ABC):

    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class Report(Observer):
    _served_customer_count: int = 0
    _CUSTOMER_AMOUNT_FOR_REPORT: int = -1  # Child class should specify this field

    def update(self, subject: Subject) -> None:
        self._served_customer_count += 1
        if self._served_customer_count % self._CUSTOMER_AMOUNT_FOR_REPORT == 0:
            self.report_logic()

    @abstractmethod
    def report_logic(self) -> None:
        pass


class XReport(Report):

    def __init__(self):
        self._CUSTOMER_AMOUNT_FOR_REPORT = 20

    def report_logic(self) -> None:
        print('X Report')


class ZReport(Report):

    def __init__(self):
        self._CUSTOMER_AMOUNT_FOR_REPORT = 100

    def report_logic(self) -> None:
        print('Z Report')


class PointOfSales(Subject):
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def notify(self) -> None:
        map(lambda observer: observer.update(), self._observers)
