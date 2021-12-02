import random
from typing import Tuple

from models import PaymentMethod, Sellable
from pos import PointOfSales, XReport, ZReport
from product_factory import ProductFactory


class Simulation:
    def __init__(self) -> None:
        self.product_factory = ProductFactory()
        self.pos = PointOfSales(MAXIMUM_SHIFTS=3)
        x_report = XReport(self.pos)
        z_report = ZReport(self.pos)
        self.pos.attach(x_report)
        self.pos.attach(z_report)

    def _create_random_customer(self) -> Tuple[list[Sellable], PaymentMethod]:
        return [
            self.product_factory.create_random_item()
            for _ in range(random.randint(1, 5))
        ], random.choice([PaymentMethod.CASH, PaymentMethod.CARD])

    def start(self) -> None:
        stop_simulation = False

        while not stop_simulation:
            customer = self._create_random_customer()
            stop_simulation = not self.pos.serve_customer(*customer)


Simulation().start()
