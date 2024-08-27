from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, \
    Integer, String, Boolean, Enum, ForeignKey,\
    MetaData
# Pay attentions if you use another DB like Oracle, MySQL etc.
# This types implement for specific dialect
from sqlalchemy.dialects.postgresql import JSONB, FLOAT

from sqlalchemy.orm import relationship

from .utils import conventions


meta = MetaData(naming_convention=conventions)

Base = declarative_base(metadata=meta)


class ModerTgUser(Base):
    __tablename__ = "moder_tguser"

    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer)
    name = Column(String)
    lower_name = Column(String)
    password = Column(String)
    cart = Column(String)
    bonus = Column(Integer)


class Info(Base):
    __tablename__ = "moder_info"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    article = Column(String)


class Moder(Base):
    __tablename__ = "moder_moder"

    id = Column(Integer, primary_key=True)
    tg_id = Column(String)


class Message(Base):
    __tablename__ = "moder_message"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    message = Column(String)
