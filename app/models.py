from sqlalchemy import Column, Integer, String, Float
from .database import Base


class ItemDB(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    price = Column(Float, nullable=False)
    brand = Column(String, nullable=True)
