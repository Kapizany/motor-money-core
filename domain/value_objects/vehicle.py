from enum import Enum


class VehicleCategory(Enum):
    MOTORCYCLE = "motocicleta"
    CAR = "carro"
    VAN = "van"
    TRUCK = "caminhão"

class VehicleStatus(Enum):
    TO_SELL = "to_sell"
    RESERVED = "reserved"
    SOLD = "sold"