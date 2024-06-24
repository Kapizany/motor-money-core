

from domain.exceptions.vehicle import InvalidVehicleCategoryException
from domain.interfaces.repositories.vehicle import VehicleRepositoryInterface
from domain.value_objects.vehicle import VehicleCategory
from interface_adapters.dtos.vehicle import ListVehicleOutputDto


class ListVehicleUseCase:
    def __init__(
        self,
        repository: VehicleRepositoryInterface,
    ):
        self._repository = repository

    def execute(
        self,  filters: dict = {}, ordering: dict = {}
    ) -> list[ListVehicleOutputDto]:

        if "category" in filters.keys():
            if filters["category"] not in [category.value for category in VehicleCategory]:
                raise InvalidVehicleCategoryException(f"Invalid category {filters['category']}")

        vehicle_list = self._repository.list(filters, ordering)

        if vehicle_list is None:
            return []

        return [
            ListVehicleOutputDto(
                brand=vehicle.brand,
                category=vehicle.category,
                price=vehicle.price,
                model=vehicle.model,
                manufacture_year=vehicle.manufacture_year,
                sale_date=vehicle.sale_date,
                status=vehicle.status,
                uuid=vehicle.uuid,
            )
            for vehicle in vehicle_list
        ]