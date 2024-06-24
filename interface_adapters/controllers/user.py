

from domain.interfaces.repositories.user import UserRepositoryInterface
from interface_adapters.dtos.user import CreateUserInputDto, CreateUserOutputDto, UserRepositoryDto
from usecases.user.create import CreateAdminUserUseCase, CreateUserUseCase


class UserController:
    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def create_admin_user(
        self, input_data: CreateUserInputDto, current_user: UserRepositoryDto
    ) -> CreateUserOutputDto:
        create_use_case = CreateAdminUserUseCase(
            repository=self.repository
        )
        new_admin_user = create_use_case.execute(input_data, current_user.uuid)
        return new_admin_user

    def create_user(
        self, input_data: CreateUserInputDto,
    ) -> CreateUserOutputDto:
        create_use_case = CreateUserUseCase(
            repository=self.repository
        )
        new_admin_user = create_use_case.execute(input_data)
        return new_admin_user

