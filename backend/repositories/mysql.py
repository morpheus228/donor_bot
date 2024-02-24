from sqlalchemy import create_engine, BigInteger, String, Column, DateTime, ForeignKey, Boolean, Integer, Text, Float, Enum, JSON
from sqlalchemy.orm import declarative_base
from datetime import datetime

from config import Config
from schemas.user import UserCondition


def get_mysql():
    config = Config.mysql
    uri = f"mysql+pymysql://{config.user}:{config.password}@{config.host}:{config.port}/{config.database}"
    return create_engine(uri)


Base = declarative_base()


class User(Base):
    __tablename__ = 'Users'

    id = Column(BigInteger, primary_key=True)
    login = Column(String(100))
    password = Column(String(100))
    username = Column(String(100))
    email = Column(String(100))



