import sys
sys.path.append('.')

from backend.controller.log_controller import create_log

class Basecontroller:
    def __init__(self, dao):
        self.__dao=dao

    def create_base(self,obj:object)->None:
        self.__dao.create_dao(obj)
        create_log(f'Saved Seller {obj.name_seller} with phone {obj.tel} and email {obj.email}' )

    def read_by_id_base(self,id:int)->object:
        create_log(f'The ID = {id} was found in seller table.')
        return self.__dao.read_by_id(id)

    def read_all_base(self)->list:
        create_log(f'Read sellers in seller table')
        return self.__dao.read_all_dao()

    def delete_base(self,id:int)->None:
        self.__dao.delete_dao(id)
        create_log(f'ID {id} deleted of the seller table.')

    def update_base(self,obj:object)->None:
        self.__dao.update_dao(obj)
        create_log(f'ID {obj.id} in marketplace table updated with name {obj.name_seller}, phone {obj.tel} and email {obj.email}.')