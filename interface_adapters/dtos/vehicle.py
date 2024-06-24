from dataclasses import dataclass
from datetime import date

from domain.value_objects.vehicle import VehicleCategory, VehicleStatus




@dataclass
class VehicleRepositoryDto:
    brand: str
    category: VehicleCategory
    price: float
    model: str
    manufacture_year: str
    sale_date: date
    status: VehicleStatus
    uuid: str


@dataclass
class ReserveVehicleInputDto:
    uuid: str


@dataclass
class ReserveVehicleOutputDto:
    brand: str
    category: VehicleCategory
    price: float
    model: str
    manufacture_year: str
    sale_date: date
    status: VehicleStatus
    uuid: str


@dataclass
class CancelVechicleReservationInputDto:
    uuid: str


@dataclass
class CancelVechicleReservationOutputDto:
    brand: str
    category: VehicleCategory
    price: float
    model: str
    manufacture_year: str
    sale_date: date
    status: VehicleStatus
    uuid: str


@dataclass
class SellVehicleInputDto:
    uuid: str
    sale_date: date


@dataclass
class SellVehicleOutputDto:
    brand: str
    category: VehicleCategory
    price: float
    model: str
    manufacture_year: str
    sale_date: date
    status: VehicleStatus
    uuid: str


@dataclass
class CreateVehicleInputDto:
    brand: str
    category: VehicleCategory
    price: float
    model: str
    manufacture_year: str


@dataclass
class CreateVehicleOutputDto:
    brand: str
    category: VehicleCategory
    price: float
    model: str
    manufacture_year: str
    sale_date: date
    status: VehicleStatus
    uuid: str


@dataclass
class DeleteVehicleInputDto:
    uuid: str


@dataclass
class DeleteVehicleOutputDto:
    brand: str
    category: VehicleCategory
    price: float
    model: str
    manufacture_year: str
    sale_date: date
    status: VehicleStatus
    uuid: str


@dataclass
class FindVehicleInputDto:
    uuid: str


@dataclass
class FindVehicleOutputDto:
    brand: str
    category: VehicleCategory
    price: float
    model: str
    manufacture_year: str
    sale_date: date
    status: VehicleStatus
    uuid: str

@dataclass
class UpdateVehicleInputDto:
    brand: str
    category: VehicleCategory
    price: float
    model: str
    manufacture_year: str
    uuid: str


@dataclass
class UpdateVehicleOutputDto:
    brand: str
    category: VehicleCategory
    price: float
    model: str
    manufacture_year: str
    sale_date: date
    status: VehicleStatus
    uuid: str

@dataclass
class ListVehicleOutputDto:
    brand: str
    category: VehicleCategory
    price: float
    model: str
    manufacture_year: str
    sale_date: date
    status: VehicleStatus
    uuid: str
