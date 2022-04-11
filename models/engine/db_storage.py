#!/usr/bin/python3
"""New engine DBStorage"""
from os import getenv
from requests import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from os import getenv
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


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

    def all(self, cls):
        """Shows the elements of a class"""
        c_list = [
            City,
            State
        ]
        rows = []
        if cls:
            rows = self.__session.query(cls)
        else:
            for cls in c_list:
                rows += self.__session.query(cls)
        return {type(v).__name__ + "." + v.id: v for v in rows}

    def new(self, obj):
        """Add object into database"""
        if not obj:
            return
        self.__session.add(obj)

    def save(self, obj):
        """Saves objet into database"""
        if not obj:
            return
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj in database"""
        if not obj:
            return
        else:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """Creates all tables in database"""
        sesion = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sesion)
        self.__session = Session()
