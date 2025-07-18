from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy import text

from app.db.database import Base

class B1(Base):
    __tablename__ = "B1_TABLE"

    b1 = Column(Integer, primary_key=True, index=True, autoincrement=True)
    