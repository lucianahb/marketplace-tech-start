from .log_controller import LogController

class BaseController:
    def __init__(self, dao, dominio) -> None:
        self.__dominio = dominio
        self.__dao = dao
        self.__log = LogController()
    
    
    def create(self,obj: object) -> None:
        self.__dao.save(obj)
        self.__log.create(f'Saved {self.__dominio}')


    def listall(self) -> list:
        list = self.__dao.read()
        self.__log.create(f'Listed {self.__dominio}')
        return list


    def delete(self, id:int) -> None:
        self.__dao.delete(id)
        self.__log.create(f'Deleted {self.__dominio} in ID {id}')
        
        
    def update(self, obj: object) -> None:
        self.__dao.update(obj)
        self.__log.create(f'Updated {self.__dominio}')