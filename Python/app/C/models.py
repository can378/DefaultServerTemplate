from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from app.db.database import Base

class C1(Base):
    __tablename__ = "C1_TABLE"

    c1 = Column(Integer, primary_key=True, index=True, autoincrement=True)
    c2 = Column(String(100), nullable=False)
