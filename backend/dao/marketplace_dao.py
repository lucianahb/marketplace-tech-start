import psycopg2
from backend.models.marketplace import *
from backend.dao.conexao_bd import *

def save_mkp(marketplace:Marketplace):
    with psycopg2.connect(conexao()) as conn: 
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO marketplace (name, description) VALUES ('{marketplace.name_mkt}', '{marketplace.description}')")
        conn.commit()
            

def read_marketplace() -> list:
    list_marketplace = []

    with psycopg2.connect(conexao()) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM marketplace')
        marketplaces = cursor.fetchall()
        for m in marketplaces:
            obj_mkt = Marketplace(m[1],m[2])
            list_marketplace.append(obj_mkt)
    return list_marketplace