from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.base.pg_db import Base

class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    device_id = Column(Integer, ForeignKey('devices.id'))
    message = Column(String, nullable=False)

    user = relationship('User', back_populates="requests")
    device = relationship('Device', back_populates="requests")
