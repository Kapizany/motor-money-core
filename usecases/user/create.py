

from uuid import uuid4
from domain.entities.user import User
from domain.exceptions.user import UnauthorizedException
from domain.interfaces.repositories.user import UserRepositoryInterface
from interface_adapters.dtos.user import CreateUserInputDto, CreateUserOutputDto


class CreateUserUseCase:
    def __init__(
        self,
        repository: UserRepositoryInterface,
    ):
        self._repository = repository

    def execute(self, input_data: CreateUserInputDto) -> CreateUserOutputDto:

        new_user = User(
            email=input_data.email,
            name=input_data.name,
            password=input_data.password,
            repository=self._repository,
            uuid=uuid4(),
        )
        new_user_dto = CreateUserOutputDto(
            email=new_user.email,
            name=new_user.name,
            is_admin=new_user.is_admin,
            uuid=new_user.uuid,
        )
        self._repository.create(new_user_dto=new_user_dto)
        return new_user_dto


class CreateAdminUserUseCase:
    def __init__(
        self,
        repository: UserRepositoryInterface,
    ):
        self._repository = repository

    def execute(
        self, input_data: CreateUserInputDto, creator_uuid: str
    ) -> CreateUserOutputDto:
        user = self._repository.find(creator_uuid)

        if user is None or not user.is_admin:
            raise UnauthorizedException("User not Allowed!")

        new_user = User(
            email=input_data.email,
            name=input_data.name,
            password=input_data.password,
            repository=self._repository,
            is_admin=True,
            uuid=uuid4(),
        )

        new_user_dto = CreateUserOutputDto(
            email=new_user.email,
            name=new_user.name,
            is_admin=new_user.is_admin,
            uuid=new_user.uuid,
        )

        self._repository.create(new_user_dto=new_user_dto)

        return new_user_dto