


from domain.exceptions.vehicle import VehicleNotFoundException
from domain.interfaces.repositories.vehicle import VehicleRepositoryInterface
from infrastructure.postgresql.models.vehicle import VehicleModel
from interface_adapters.dtos.vehicle import VehicleRepositoryDto


class VehicleRepository(VehicleRepositoryInterface):
    def create(self, new_vehicle_dto):
        new_vehicle = VehicleModel(
            name=new_vehicle_dto.name,
            category=new_vehicle_dto.category,
            price=new_vehicle_dto.price,
            description=new_vehicle_dto.description,
            image=new_vehicle_dto.image,
            is_active=new_vehicle_dto.is_active,
            uuid=new_vehicle_dto.uuid,
        )
        new_vehicle.create()

    def find(self, uuid):
        vehicle = VehicleModel.retrieve(uuid)
        if vehicle is None:
            return None
        return VehicleRepositoryDto(
            name=vehicle.name,
            category=vehicle.category,
            price=vehicle.price,
            description=vehicle.description,
            image=vehicle.image,
            is_active=vehicle.is_active,
            uuid=str(vehicle.uuid),
        )

    def list(self, filters):
        vehicles = VehicleModel.list_filtering_by_column(filters)

        if vehicles is None:
            return []

        return [
            VehicleRepositoryDto(
                name=vehicle[0].name,
                category=vehicle[0].category,
                price=vehicle[0].price,
                description=vehicle[0].description,
                image=vehicle[0].image,
                is_active=vehicle[0].is_active,
                uuid=str(vehicle[0].uuid),
            )
            for vehicle in vehicles
        ]

    def update(self, updated_vehicle_dto):
        vehicle = VehicleModel.retrieve(updated_vehicle_dto.uuid)
        if vehicle is None:
            raise VehicleNotFoundException()
        VehicleModel.update(
            {
                "name": updated_vehicle_dto.name,
                "category": updated_vehicle_dto.category,
                "price": updated_vehicle_dto.price,
                "description": updated_vehicle_dto.description,
                "image": updated_vehicle_dto.image,
                "uuid": updated_vehicle_dto.uuid,
                "is_active": updated_vehicle_dto.is_active,
                "id": vehicle.id,
            }
        )

    def delete(self, uuid):
        vehicle = VehicleModel.retrieve(uuid)
        if vehicle is None:
            raise VehicleNotFoundException()
        VehicleModel.destroy(str(vehicle.uuid))