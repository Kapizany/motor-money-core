from domain.exceptions.base import DomainException


class InvalidVehiclePriceException(DomainException):
    def __init__(self, message="Invalid vehicle price."):
        super().__init__(message)


class UnavailableVehicleException(DomainException):
    def __init__(self, message="Unavailable vehicle."):
        super().__init__(message)


class InvalidVehicleCategoryException(DomainException):
    def __init__(self, message="Invalid vehicle category."):
        super().__init__(message)


class VehicleNotFoundException(DomainException):
    def __init__(self, message="Vehicle not found."):
        super().__init__(message)