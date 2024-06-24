

from uuid import UUID
from domain.entities.vehicle import Vehicle
from domain.exceptions.vehicle import UnavailableVehicleException
from domain.interfaces.repositories.vehicle import VehicleRepositoryInterface
from domain.value_objects.vehicle import VehicleStatus
from interface_adapters.dtos.vehicle import SellVehicleInputDto, SellVehicleOutputDto, UpdateVehicleOutputDto


class SellVehicleUseCase:
    def __init__(
        self,
        repository: VehicleRepositoryInterface,
    ):
        self._repository = repository

    def execute(
        self, input_data: SellVehicleInputDto,
    ) -> SellVehicleOutputDto:

        vehicle = self._repository.find(input_data.uuid)

        if vehicle is None:
            return UnavailableVehicleException("Vehicle Not Found!")

        updated_vehicle = Vehicle(
            brand=vehicle.brand,
            category=vehicle.category,
            price=vehicle.price,
            model=vehicle.model,
            manufacture_year=vehicle.manufacture_year,
            sale_date=vehicle.sale_date,
            status=vehicle.status,
            uuid=UUID(input_data.uuid),
        )

        updated_vehicle.sell(input_data.sale_date)

        updated_vehicle_dto = UpdateVehicleOutputDto(
            brand=updated_vehicle.brand,
            category=updated_vehicle.category,
            price=updated_vehicle.price,
            model=updated_vehicle.model,
            manufacture_year=updated_vehicle.manufacture_year,
            sale_date=updated_vehicle.sale_date,
            status=updated_vehicle.status,
            uuid=updated_vehicle.uuid,
        )

        self._repository.update(updated_vehicle_dto=updated_vehicle_dto)

        return SellVehicleOutputDto(
            brand=updated_vehicle_dto.brand,
            category=updated_vehicle_dto.category,
            price=updated_vehicle_dto.price,
            model=updated_vehicle_dto.model,
            manufacture_year=updated_vehicle_dto.manufacture_year,
            sale_date=updated_vehicle_dto.sale_date,
            status=updated_vehicle_dto.status,
            uuid=updated_vehicle_dto.uuid,
        )
