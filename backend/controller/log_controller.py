from backend.dao.log_dao import *
from backend.models.log import Log


class LogController:
    def __init__(self) -> None:
        self.__dao = LogDao()
        
        
    def create(self, log: str) -> None:
        l = Log(log)
        return self.__dao.save(l)


    def listall(self) -> list:
        list = self.__dao.read()
        return list   