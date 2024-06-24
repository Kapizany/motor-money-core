from abc import ABC, abstractmethod
from datetime import date
from uuid import UUID

from domain.value_objects.vehicle import VehicleCategory, VehicleStatus


class VehicleInterface(ABC):
    _brand: str
    _category: VehicleCategory
    _price: float
    _model: str
    _manufacture_year: str
    _sale_date: date
    _status: VehicleStatus
    _uuid: UUID

    @property
    @abstractmethod
    def brand(self) -> str:
        pass

    @brand.setter
    @abstractmethod
    def brand(self, value: str):
        pass

    @property
    @abstractmethod
    def category(self) -> VehicleCategory:
        pass

    @category.setter
    @abstractmethod
    def category(self, value: VehicleCategory):
        pass

    @property
    @abstractmethod
    def status(self) -> VehicleStatus:
        pass

    @status.setter
    @abstractmethod
    def status(self, value: VehicleStatus):
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float):
        pass

    @property
    @abstractmethod
    def model(self) -> str:
        pass

    @model.setter
    @abstractmethod
    def model(self, value: str):
        pass

    @property
    @abstractmethod
    def manufacture_year(self) -> int:
        pass

    @manufacture_year.setter
    @abstractmethod
    def manufacture_year(self, value: int):
        pass

    @property
    @abstractmethod
    def uuid(self) -> str:
        pass

    @property
    @abstractmethod
    def sale_date(self) -> date:
        pass

    @sale_date.setter
    @abstractmethod
    def sale_date(self, value: date):
        pass

    @abstractmethod
    def sell(self) -> None:
        pass

    @abstractmethod
    def reserve(self) -> None:
        pass

    @abstractmethod
    def cancel_reservation(self) -> None:
        pass

