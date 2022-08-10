from sqlalchemy import Column, Integer, Text, VARCHAR, BINARY, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, create_session

from config import config_db

Base = declarative_base()

# Модель, которая будет соответсвовать как алгоритмам в БД, так и структурам данных
class Alg(Base):
    __tablename__ = 'alg'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    data_id = Column(VARCHAR(255), unique=True)
    type = Column(Integer, ForeignKey('type.id'))
    title = Column(VARCHAR(255), unique=True)
    description = Column(Text)
    code = Column(Text)


# Модель, которая будет соответствовать типу записи в таблице alg
class Type(Base):
    __tablename__= 'type'

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(VARCHAR(255), unique=True)
    description = Column(Text)


engine = create_engine(f'postgresql+psycopg2://{config_db["username"]}:{config_db["password"]}@{config_db["server"]}:{config_db["port"]}/{config_db["db_name"]}')
session = create_session(bind=engine)