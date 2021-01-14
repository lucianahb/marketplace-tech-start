from backend.models.marketplace import *
from backend.dao.conexao_bd import Conexao


def save_mkp(marketplace:Marketplace):
    with Conexao() as conn: 
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO marketplace (name, description) VALUES ('{marketplace.name_mkt}', '{marketplace.description}')")
        conn.commit()
            

def read_marketplace() -> list:
    list_marketplace = []

    with Conexao() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id,name,description FROM marketplace')
        marketplaces = cursor.fetchall()
        for m in marketplaces:
            obj_mkt = Marketplace(m[1],m[2],m[0])
            list_marketplace.append(obj_mkt)
    return list_marketplace


def delete_marketplace(id:int):
    with Conexao() as conn:
        cursor = conn.cursor()
        cursor.execute(f'delete from marketplace where id = {id};')
        conn.commit()


def update_marketplace(m:Marketplace):
    with Conexao() as conn:
        cursor = conn.cursor()
        cursor.execute(f"update marketplace set name='{m.name_mkt}',description='{m.description}' where id = {m.id};")
        conn.commit()

       