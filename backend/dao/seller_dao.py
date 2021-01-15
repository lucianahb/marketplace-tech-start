import sys
sys.path.append('.')

from backend.models.seller import *
from backend.dao.base_dao import Basedao

class Sellerdao(Basedao):
    def save(self,seller:Seller) -> None:
        query=f"INSERT INTO seller (name, phone, email) VALUES ('{seller.name}', '{seller.tel}', '{seller.email}');"
        super().execute(query)  
       
    def read_by_id(self,id:int)->Seller:
        query="SELECT id,name,phone,email FROM seller WHERE {id};"
        result=super().read(query)[0]
        seller=Seller(result[0],result[1],result[2],result[3])
        return seller

    def read(self)->list:
        list_seller = []
        query='SELECT id,name,phone,email FROM seller;'
        result=super().read(query)
        for s in result:
            seller=Seller(s[1],s[2],s[3],s[0])
            list_seller.append(seller)
        return list_seller

    def delete(self,id:int)->None:
        query=f'delete from seller where id = {id};'
        super().execute(query)

    def update(self,s:Seller)->None:
        query=f"update seller set name='{s.name}',phone='{s.tel}',email='{s.email}' where id = {s.id};"
        super().execute(query)
 