from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base


class A1(Base):
    __tablename__ = "A1_TABLE"

    a1 = Column(Integer, primary_key=True, index=True, autoincrement=True)
    a2 = Column(String(100), nullable=False)

class A2(Base):
    __tablename__ = "A2_TABLE"

    a1 = Column(Integer, primary_key=True, index=True, autoincrement=True)
    a2 = Column(Integer, ForeignKey("A1.a1"), nullable=False)
