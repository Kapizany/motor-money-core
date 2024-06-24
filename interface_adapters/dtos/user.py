from dataclasses import dataclass


@dataclass
class UserRepositoryDto:
    email: str
    name: str
    password: str | None
    is_admin: bool
    uuid: str

@dataclass
class CreateUserInputDto:
    email: str
    name: str
    password: str


@dataclass
class CreateUserOutputDto:
    email: str
    name: str
    is_admin: bool
    uuid: str


@dataclass
class UpdateUserInputDto:
    email: str
    name: str
    uuid: str


@dataclass
class UpdateUserOutputDto:
    email: str
    name: str
    is_admin: bool
    uuid: str

@dataclass
class ListUserOutputDto:
    email: str
    name: str
    is_admin: bool
    uuid: str


@dataclass
class FindUserInputDto:
    uuid: str


@dataclass
class FindUserOutputDto:
    email: str
    name: str
    is_admin: bool
    uuid: str



