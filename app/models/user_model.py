from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(16), unique=True)
    full_name = Column(String(255), nullable=True)
    email= Column(String(255), unique=True, nullable=True)
    phone= Column(String(20), unique=True, nullable=True)
    hashed_password = Column(String(255), nullable=True)
    salt = Column(String(255))
    activated = Column(Boolean)
    role_id = Column(Integer, ForeignKey('roles.id'))
    created_at = Column(DateTime)
    updated_at = Column(DateTime, nullable=True)
