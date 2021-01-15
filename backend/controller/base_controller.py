import sys
sys.path.append('.')

class Basecontroller:
    def __init__(self, dao):
        self.__dao=dao

    def create(self,obj:object)->None:
        self.__dao.save(obj)
        
    def read_by_id(self,id:int)->object:
        return self.__dao.read_by_id(id)

    def listall(self)->list:
        return self.__dao.read()

    def delete(self,id:int)->None:
        self.__dao.delete(id)        

    def update(self,obj:object)->None:
        self.__dao.update(obj)        
