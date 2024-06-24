

from domain.exceptions.vehicle import UnavailableVehicleException, VehicleNotFoundException
from domain.interfaces.repositories.vehicle import VehicleRepositoryInterface
from domain.value_objects.vehicle import VehicleStatus
from interface_adapters.dtos.vehicle import FindVehicleInputDto, FindVehicleOutputDto


class FindVehicleUseCase:
    def __init__(
        self,
        repository: VehicleRepositoryInterface,
    ):
        self._repository = repository

    def execute(
        self, input_data: FindVehicleInputDto
    ) -> FindVehicleOutputDto | None:

        vehicle = self._repository.find(uuid=input_data.uuid)

        if vehicle is None:
            raise VehicleNotFoundException()
        if vehicle.status != VehicleStatus.TO_SELL.value:
            raise UnavailableVehicleException()

        return FindVehicleOutputDto(
            brand=vehicle.brand,
            category=vehicle.category,
            price=vehicle.price,
            model=vehicle.model,
            manufacture_year=vehicle.manufacture_year,
            sale_date=vehicle.sale_date,
            status=vehicle.status,
            uuid=vehicle.uuid,
        )