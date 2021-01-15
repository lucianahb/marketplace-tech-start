
class BaseController:
    def __init__(self, dao) -> None:
        self.__dao = dao
    
    def create(self,obj: object) -> None:
        self.__dao.save(obj)


    def listall(self) -> list:
        list = self.__dao.read()
        return list


    def delete(self, id:int) -> None:
        self.__dao.delete(id)
        
        
    def update(self, obj: object) -> None:
        self.__dao.update(obj)