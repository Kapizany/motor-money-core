from abc import abstractmethod
from dataclasses import dataclass

from domain.interfaces.repositories.repository import RepositoryInterface
from interface_adapters.dtos.vehicle import CreateVehicleOutputDto, UpdateVehicleOutputDto, VehicleRepositoryDto

class VehicleRepositoryInterface(RepositoryInterface):
    @abstractmethod
    def create(self, new_vehicle_dto: CreateVehicleOutputDto) -> None:
        pass

    @abstractmethod
    def find(self, uuid: str) -> VehicleRepositoryDto | None:
        pass

    @abstractmethod
    def list(self, filters: dict, ordering: dict) -> list[VehicleRepositoryDto]:
        pass

    @abstractmethod
    def update(self, updated_vehicle_dto: UpdateVehicleOutputDto) -> None:
        pass

    @abstractmethod
    def delete(self, uuid: str) -> None:
        pass