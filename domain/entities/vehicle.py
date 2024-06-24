from datetime import date
from uuid import UUID
from domain.interfaces.entities.vehicle import VehicleInterface

from domain.value_objects.vehicle import VehicleCategory, VehicleStatus


class Vehicle(VehicleInterface):
    def __init__(
        self,
        brand: str,
        category: VehicleCategory,
        price: float,
        model: str,
        manufacture_year: str,
        sale_date: date,
        status: VehicleStatus,
        uuid: UUID,
    ):
        self._brand = brand
        self._category = category
        self._price = price
        self._model = model
        self._manufacture_year = manufacture_year
        self._sale_date = sale_date
        self._status = status
        self._uuid = uuid

    @property
    def brand(self) -> str:
        return self._brand

    @brand.setter
    def brand(self, value: str):
        self._brand = value

    @property
    def category(self) -> VehicleCategory:
        return self._category

    @category.setter
    def category(self, value: VehicleCategory):
        self._category = value

    @property
    def status(self) -> VehicleStatus:
        return self._status

    @status.setter
    def status(self, value: VehicleStatus):
        self._status = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        self._price = value

    @property
    def model(self) -> str:
        return self._model

    @model.setter
    def model(self, value: str):
        self._model = value

    @property
    def manufacture_year(self) -> int:
        return self._manufacture_year

    @manufacture_year.setter
    def manufacture_year(self, value: int):
        self._manufacture_year = value

    @property
    def uuid(self) -> str:
        return self._uuid

    @property
    def sale_date(self) -> date:
        return self._sale_date

    @sale_date.setter
    def sale_date(self, value: date):
        self._sale_date = value

    def sell(self, sale_date: date) -> None:
        self.status = VehicleStatus.SOLD
        self.sale_date = sale_date

    def reserve(self) -> None:
        self.status = VehicleStatus.RESERVED

    def cancel_reservation(self) -> None:
        self.status = VehicleStatus.TO_SELL