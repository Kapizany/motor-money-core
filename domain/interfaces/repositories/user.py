from abc import abstractmethod

from domain.interfaces.repositories.repository import RepositoryInterface
from interface_adapters.dtos.user import CreateUserOutputDto, UpdateUserOutputDto, UserRepositoryDto



class UserRepositoryInterface(RepositoryInterface):
    @abstractmethod
    def create(self, new_user_dto: CreateUserOutputDto) -> None:
        pass

    @abstractmethod
    def find(self, uuid: str | None) -> UserRepositoryDto | None:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> UserRepositoryDto | None:
        pass

    @abstractmethod
    def list(self) -> list[UserRepositoryDto]:
        pass

    @abstractmethod
    def update(self, updated_user_dto: UpdateUserOutputDto, password: str) -> None:
        pass