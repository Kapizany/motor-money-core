from uuid import UUID

from domain.interfaces.entities.user import UserInterface




class User(UserInterface):
    def __init__(
        self,
        email: str,
        name: str,
        password: str,
        uuid: UUID,
        is_admin: bool = False,
    ):
        self.email = email
        self.name = name
        self.password = password
        self._uuid = uuid
        self._is_admin = is_admin

    @property
    def email(self):
        return self._email.value

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def password(self):
        return self._password.value

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def is_admin(self):
        return self._is_admin

    @property
    def uuid(self):
        return str(self._uuid)

    @property
    def validator(self):
        return self._validator