import sys
sys.path.append('.')
from backend.models.marketplace import *
from backend.dao.base_dao import BaseDao

class Marketplacedao(BaseDao):

    def save(self,obj:Marketplace) -> None:
        query=f"INSERT INTO marketplace (name, description) VALUES ('{obj.name}', '{obj.description}');"
        super().execute(query)  
       
    def read_by_id(self,id:int)->Marketplace:
        query="SELECT id,name,description FROM marketplace WHERE {id};"
        result=super().read(query)[0]
        market=Marketplace(result[0],result[1],result[2])
        return market
    
    def read(self)->list:
        list_market = []
        query='SELECT id,name,description FROM marketplace'
        result=super().read(query)
        for s in result:
            market=Marketplace(s[1],s[2],s[0])
            list_market.append(market)
        return list_market

    def delete(self,id:int)->None:
        query=f'delete from marketplace where id = {id};'
        super().execute(query)

    def update(self,m:Marketplace)->None:
        query=f"update marketplace set name='{m.name}',description='{m.description}' where id = {m.id};"
        super().execute(query)