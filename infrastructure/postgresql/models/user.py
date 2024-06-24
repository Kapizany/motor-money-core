import uuid

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.dialects.postgresql import UUID

from infrastructure.flask.db import Base
from infrastructure.postgresql.repositories.mixin import CRUDMixin



class UserModel(Base, CRUDMixin):
    __tablename__ = "user"

    email = Column(String, index=True, unique=True)
    name = Column(String)
    password = Column(String)
    is_admin = Column(Boolean, default=False, nullable=False)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, index=True, unique=True)
    id = Column(Integer, primary_key=True)

