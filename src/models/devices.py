from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, func, TIMESTAMP
from sqlalchemy.orm import relationship
from src.base.pg_db import Base

class Device(Base):
    __tablename__ = 'devices'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    name = Column(String, nullable=False)
    model = Column(String)
    serial_number = Column(String, nullable=False)
    status = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    user = relationship('User', back_populates='devices')
    category = relationship('Category', back_populates='devices')
    requests = relationship('Request', back_populates='device')
