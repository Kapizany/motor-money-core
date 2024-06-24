

from uuid import UUID
from domain.entities.vehicle import Vehicle
from domain.exceptions.user import UnauthorizedException
from domain.exceptions.vehicle import UnavailableVehicleException
from domain.interfaces.repositories.user import UserRepositoryInterface
from domain.interfaces.repositories.vehicle import VehicleRepositoryInterface
from interface_adapters.dtos.vehicle import UpdateVehicleInputDto, UpdateVehicleOutputDto


class UpdateVehicleUseCase:
    def __init__(
        self,
        repository: VehicleRepositoryInterface,
        user_repository: UserRepositoryInterface,
    ):
        self._repository = repository
        self._user_repository = user_repository


    def execute(
        self, input_data: UpdateVehicleInputDto, actor_uuid: str | None
    ) -> UpdateVehicleOutputDto:
        actor = self._user_repository.find(actor_uuid)
        if actor is None or not actor.is_admin:
            raise UnauthorizedException("User not Allowed!")

        vehicle = self._repository.find(input_data.uuid)

        if vehicle is None:
            raise UnavailableVehicleException("Vehicle Not Found!")

        updated_vehicle = Vehicle(
            brand=input_data.brand,
            category=input_data.category,
            price=input_data.price,
            model=input_data.model,
            manufacture_year=input_data.manufacture_year,
            sale_date=vehicle.sale_date,
            status=vehicle.status,
            uuid=UUID(input_data.uuid),
        )

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

        self._repository.update(updated_vehicle_dto)

        return updated_vehicle_dto