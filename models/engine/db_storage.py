#!/usr/bin/python3
"""New engine DBStorage"""
from os import getenv
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from os import getenv


class DBStorage():
    """DBStorage class"""
    __engine = None
    __session = None
    def __init__(self):
        """Initialization of engine"""
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                user, passwd, host, db), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
