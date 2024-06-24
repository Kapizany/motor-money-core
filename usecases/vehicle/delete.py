

from domain.interfaces.repositories.user import UserRepositoryInterface
from domain.interfaces.repositories.vehicle import VehicleRepositoryInterface
from interface_adapters.dtos.vehicle import DeleteVehicleInputDto, DeleteVehicleOutputDto


class DeleteVehicleUseCase:
    def __init__(
        self,
        repository: VehicleRepositoryInterface,
        user_repository: UserRepositoryInterface,
    ):
        self._repository = repository
        self._user_repository = user_repository

    def execute(
        self, input_data: DeleteVehicleInputDto, actor_uuid: str | None
    ) -> DeleteVehicleOutputDto | None:
        actor = self._user_repository.find(actor_uuid)
        if actor is None or not actor.is_admin:
            return None

        vehicle = self._repository.find(uuid=input_data.uuid)

        if vehicle is None:
            return None

        self._repository.delete(uuid=input_data.uuid)

        return DeleteVehicleOutputDto(
            brand=vehicle.brand,
            category=vehicle.category,
            price=vehicle.price,
            model=vehicle.model,
            manufacture_year=vehicle.manufacture_year,
            sale_date=vehicle.sale_date,
            status=vehicle.status,
            uuid=vehicle.uuid,
        )