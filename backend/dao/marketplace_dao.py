import psycopg2
from backend.models.marketplace import *

_host='pgsql08-farm15.uni5.net'
_user='topskills7'
_password='olist21'
_database='topskills7'
_connection_string = f"host={_host} user={_user} dbname={_database} password={_password}"

def save_mkp(marketplace:Marketplace):
    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()
    
    cursor.execute(f"INSERT INTO marketplace (name, description) VALUES ('{marketplace.name_mkt}', '{marketplace.description}')")
    
    conn.commit()
    cursor.close()
    conn.close()
    

def read_marketplace() -> list:
    list_marketplace = []

    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM marketplace')

    marketplaces = cursor.fetchall()

    for m in marketplaces:
        
        obj_mkt = Marketplace(m[1],m[2])
        list_marketplace.append(obj_mkt)

    cursor.close()
    conn.close()

    return list_marketplace