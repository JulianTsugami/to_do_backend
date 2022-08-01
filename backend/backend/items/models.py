from sqlalchemy import Column, Integer, String
from backend.database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    note = Column(String, nullable=False)
