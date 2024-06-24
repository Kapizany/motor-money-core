from abc import ABC, abstractmethod
from uuid import UUID


class UserInterface(ABC):
    _email: str
    _name: str
    _password: str
    _is_admin: bool
    _uuid: UUID


    @property
    @abstractmethod
    def email(self) -> str:
        pass

    @email.setter
    @abstractmethod
    def email(self, email: str):
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @name.setter
    @abstractmethod
    def name(self, value: str):
        pass

    @property
    @abstractmethod
    def password(self) -> str:
        pass

    @password.setter
    @abstractmethod
    def password(self, password: str):
        pass

    @property
    @abstractmethod
    def is_admin(self) -> bool:
        pass

    @property
    @abstractmethod
    def uuid(self) -> str:
        pass
