import psycopg2
from backend.models.seller import *
from backend.dao.conexao_bd import *

def save_seller(seller:Seller) -> None:
    with psycopg2.connect(conexao()) as conn:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO seller (name, phone, email) VALUES ('{seller.name_seller}', '{seller.tel}', '{seller.email}')")
        conn.commit()
   
def read_sellers() -> list:
    list_seller = []

    with psycopg2.connect(conexao()) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM seller')
        result = cursor.fetchall()
        l_sellers=[]
        for s in result:
            seller=Seller(s[1],s[2],s[3])
            l_sellers.append(seller)
    return l_sellers