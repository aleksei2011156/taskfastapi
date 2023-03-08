from app.database import Base, engine
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    balance = Column(Integer)

    # relations
    history_usr = relationship("History", back_populates="usr")


class Type(Base):
    __tablename__ = "type"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    # relations
    history_type = relationship("History", back_populates="typ")


class History(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Integer, ForeignKey("user.id"))
    type = Column(Integer,  ForeignKey("type.id"))
    count = Column(Integer)
    status = Column(Boolean)

    #relations
    usr = relationship("User", back_populates="history_usr")
    typ = relationship("Type", back_populates="history_type")
