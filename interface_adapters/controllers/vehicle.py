
from typing import Literal
from interface_adapters.dtos.user import UserRepositoryDto
from interface_adapters.dtos.vehicle import CancelVechicleReservationInputDto, CancelVechicleReservationOutputDto, CreateVehicleInputDto, CreateVehicleOutputDto, DeleteVehicleInputDto, DeleteVehicleOutputDto, FindVehicleInputDto, FindVehicleOutputDto, ListVehicleOutputDto, ReserveVehicleInputDto, ReserveVehicleOutputDto, SellVehicleInputDto, SellVehicleOutputDto, UpdateVehicleInputDto, UpdateVehicleOutputDto
from domain.interfaces.repositories.vehicle import VehicleRepositoryInterface
from domain.interfaces.repositories.user import UserRepositoryInterface
from domain.value_objects.vehicle import VehicleCategory
from usecases.vehicle.create import CreateVehicleUseCase
from usecases.vehicle.delete import DeleteVehicleUseCase
from usecases.vehicle.list import ListVehicleUseCase
from usecases.vehicle.find import FindVehicleUseCase
from usecases.vehicle.reservation import CancelVechicleReservationUseCase, ReserveVehicleUseCase
from usecases.vehicle.sell import  SellVehicleUseCase
from usecases.vehicle.update import UpdateVehicleUseCase


class VehicleController:
    def __init__(
        self,
        repository: VehicleRepositoryInterface,
        user_repository: UserRepositoryInterface,
        current_user: UserRepositoryDto,
    ):
        self.repository = repository
        self.user_repository = user_repository
        self.current_user = current_user

    def list_vehicles(
        self, category: str | None = None, order_key: str = None, order: Literal["asc"] | Literal["desc"] = "desc"
    ) -> list[ListVehicleOutputDto]:
        filters = {}
        ordering = {}

        if category is not None:
            filters["category"] = category

        if order_key:
            ordering[order_key] = order

        list_use_case = ListVehicleUseCase(
            repository=self.repository
        )

        return list_use_case.execute(self.current_user.uuid, filters)

    def retrieve_vehicle(self, vehicle_uuid: str) -> FindVehicleOutputDto | None:
        find_use_case = FindVehicleUseCase(
            repository=self.repository
        )
        return find_use_case.execute(
            FindVehicleInputDto(uuid=vehicle_uuid), self.current_user.uuid
        )

    def update_vehicle(
        self,
        brand: str,
        category: VehicleCategory,
        price: float,
        model: str,
        manufacture_year: str,
        uuid: str,
    ) -> UpdateVehicleOutputDto:
        input_data = UpdateVehicleInputDto(
            brand=brand,
            category=category,
            price=price,
            model=model,
            manufacture_year=manufacture_year,
            uuid=uuid,
        )
        update_use_case = UpdateVehicleUseCase(
            repository=self.repository, user_repository=self.user_repository
        )
        return update_use_case.execute(
            input_data=input_data, actor_uuid=self.current_user.uuid
        )

    def create_vehicle(
        self,
        brand: str,
        category: VehicleCategory,
        price: float,
        model: str,
        manufacture_year: str,
    ) -> CreateVehicleOutputDto:
        input_data = CreateVehicleInputDto(
            brand=brand,
            category=category,
            price=price,
            model=model,
            manufacture_year=manufacture_year,
        )
        create_use_case = CreateVehicleUseCase(
            repository=self.repository, user_repository=self.user_repository
        )
        return create_use_case.execute(input_data, self.current_user.uuid)

    def reserve_vehicle(
        self,
        input_data: ReserveVehicleInputDto,
    ) -> ReserveVehicleOutputDto:
        update_use_case = ReserveVehicleUseCase(
            repository=self.repository
        )
        return update_use_case.execute(
            input_data=input_data
        )

    def cancel_vehicle_reservation(
        self,
        input_data: CancelVechicleReservationInputDto,
    ) -> CancelVechicleReservationOutputDto:
        update_use_case = CancelVechicleReservationUseCase(
            repository=self.repository
        )
        return update_use_case.execute(
            input_data=input_data
        )

    def sell_vehicle(
        self,
        input_data: SellVehicleInputDto,
    ) -> SellVehicleOutputDto:
        update_use_case = SellVehicleUseCase(
            repository=self.repository
        )
        return update_use_case.execute(
            input_data=input_data
        )

    def delete_vehicle(
        self,
        vehicle_uuid: str,
    ) -> DeleteVehicleOutputDto | None:
        delete_use_case = DeleteVehicleUseCase(
            repository=self.repository, user_repository=self.user_repository
        )
        return delete_use_case.execute(
            DeleteVehicleInputDto(uuid=vehicle_uuid), self.current_user.uuid
        )