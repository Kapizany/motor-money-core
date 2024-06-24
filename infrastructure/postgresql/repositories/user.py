

from domain.exceptions.user import UserNotFoundException
from domain.interfaces.repositories.user import UserRepositoryInterface
from infrastructure.postgresql.models.user import UserModel
from interface_adapters.dtos.user import UserRepositoryDto


class UserRepository(UserRepositoryInterface):
    def create(self, new_user_dto):
        new_user = UserModel(
            email=new_user_dto.email,
            name=new_user_dto.name,
            password=new_user_dto.password,
            uuid=new_user_dto.uuid,
        )
        new_user.create()

    def find(self, uuid):
        user = UserModel.retrieve(uuid)
        if user is None:
            return None
        return UserRepositoryDto(
            email=user.email,
            name=user.name,
            password=user.password,
            is_admin=user.is_admin,
            uuid=str(user.uuid),
        )

    def find_by_email(self, email):
        user = UserModel.retrieve_by_column("email", email)
        if user is None:
            return None
        return UserRepositoryDto(
            email=user.email,
            name=user.name,
            password=user.password,
            is_admin=user.is_admin,
            uuid=str(user.uuid),
        )

    def list(self):
        users = UserModel.list()

        if users is None:
            return []

        return [
            UserRepositoryDto(
                email=user[0].email,
                name=user[0].name,
                is_admin=user[0].is_admin,
                uuid=str(user[0].uuid),
            )
            for user in users
        ]

    def update(self, updated_user_dto, password):
        user = UserModel.retrieve(updated_user_dto.uuid)
        if user is None:
            raise UserNotFoundException()
        UserModel.update(
            {
                "email": updated_user_dto.email,
                "name": updated_user_dto.name,
                "password": password,
                "uuid": updated_user_dto.uuid,
                "id": user.id,
            }
        )