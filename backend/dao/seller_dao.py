import psycopg2
from backend.models.seller import *

_host='pgsql08-farm15.uni5.net'
_user='topskills7'
_password='olist21'
_database='topskills7'
_connection_string = f"host={_host} user={_user} dbname={_database} password={_password}"

def save_seller(seller:Seller) -> None:
    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()
    
    cursor.execute(f"INSERT INTO seller (name, phone, email) VALUES ('{seller.name_seller}', '{seller.tel}', '{seller.email}')")

    conn.commit()
    cursor.close()
    conn.close()

def read_sellers() -> list:
    list_seller = []

    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM seller')
    result = cursor.fetchall()
    l_sellers=[]


    for s in result:
        seller=Seller(s[1],s[2],s[3])
        l_sellers.append(seller)

    cursor.close()
    conn.close()
    
    return l_sellers