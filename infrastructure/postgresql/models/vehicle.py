import uuid

from sqlalchemy import Column, Integer, String, Enum, Float, DateTime
from sqlalchemy.dialects.postgresql import UUID
from domain.value_objects.vehicle import VehicleCategory, VehicleStatus

from infrastructure.flask.db import Base
from infrastructure.postgresql.repositories.mixin import CRUDMixin



class VehicleModel(Base, CRUDMixin):
    __tablename__ = "vehicle"

    brand = Column(String, nullable=False)
    category = Column(Enum(VehicleCategory), index=True, nullable=False)
    price = Column(Float, nullable=False)
    model = Column(String, nullable=False)
    manufacture_year = Column(String, nullable=False)
    sale_date = Column(DateTime)
    status = Column(Enum(VehicleStatus), index=True, nullable=False)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, index=True, unique=True)
    id = Column(Integer, primary_key=True)