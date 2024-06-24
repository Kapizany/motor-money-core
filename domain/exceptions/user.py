from domain.exceptions.base import DomainException


class InvalidEmailException(DomainException):
    def __init__(self, message="Invalid email."):
        super().__init__(message)


class InvalidPasswordException(DomainException):
    def __init__(self, message="Invalid password."):
        super().__init__(message)


class UserNotFoundException(DomainException):
    def __init__(self, message="User not found."):
        super().__init__(message)


class UnauthorizedException(DomainException):
    def __init__(self, message="User unauthorized."):
        super().__init__(message)