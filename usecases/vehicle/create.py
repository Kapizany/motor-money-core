

from uuid import uuid4
from domain.entities.vehicle import Vehicle
from domain.exceptions.user import UnauthorizedException
from domain.interfaces.repositories.user import UserRepositoryInterface
from domain.interfaces.repositories.vehicle import VehicleRepositoryInterface
from domain.value_objects.vehicle import VehicleStatus
from interface_adapters.dtos.vehicle import CreateVehicleInputDto, CreateVehicleOutputDto


class CreateVehicleUseCase:
    def __init__(
        self,
        repository: VehicleRepositoryInterface,
        user_repository: UserRepositoryInterface,
    ):
        self._repository = repository
        self._user_repository = user_repository

    def execute(
        self, input_data: CreateVehicleInputDto, actor_uuid: str | None
    ) -> CreateVehicleOutputDto:
        actor = self._user_repository.find(actor_uuid)
        if actor is None or not actor.is_admin:
            raise UnauthorizedException("User not Allowed!")

        new_vehicle = Vehicle(
            brand=input_data.brand,
            category=input_data.category,
            price=input_data.price,
            model=input_data.model,
            manufacture_year=input_data.manufacture_year,
            sale_date=None,
            status=VehicleStatus.TO_SELL.value,
            uuid=uuid4(),
        )

        new_vehicle_dto = CreateVehicleOutputDto(
            brand=new_vehicle.brand,
            category=new_vehicle.category,
            price=new_vehicle.price,
            model=new_vehicle.model,
            manufacture_year=new_vehicle.manufacture_year,
            sale_date=new_vehicle.sale_date,
            status=new_vehicle.status,
            uuid=new_vehicle.uuid,
        )

        self._repository.create(new_vehicle_dto)

        return new_vehicle_dto