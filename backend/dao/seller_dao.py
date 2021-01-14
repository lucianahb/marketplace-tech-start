from backend.models.seller import *
from backend.dao.conexao_bd import Conexao


def save_seller(seller:Seller) -> None:
    with Conexao() as conn:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO seller (name, phone, email) VALUES ('{seller.name_seller}', '{seller.tel}', '{seller.email}')")
        conn.commit()
   
   
def read_sellers() -> list:
    list_seller = []

    with Conexao() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id,name,phone,email FROM seller')
        result = cursor.fetchall()
        l_sellers=[]
        for s in result:
            seller=Seller(s[1],s[2],s[3],s[0])
            l_sellers.append(seller)
    return l_sellers


def delete_seller(id:int):
    with Conexao() as conn:
        cursor = conn.cursor()
        cursor.execute(f'delete from seller where id = {id};')
        conn.commit()


def update_seller(s:Seller):
    with Conexao() as conn:
        cursor = conn.cursor()
        cursor.execute(f"update seller set name='{s.name_seller}',phone='{s.tel}',email='{s.email}' where id = {s.id};")
        conn.commit()