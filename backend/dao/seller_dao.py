import psycopg2
from backend.controller.log_controller import create_log

_host='pgsql08-farm15.uni5.net'
_user='topskills7'
_password='olist21'
_database='topskills7'
_connection_string = f"host={_host} user={_user} dbname={_database} password={_password}"

def save_seller(name_seller: str, phone: str, email: str) -> None:
    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO seller (name, phone, email) VALUES ('{name_seller}', '{phone}', '{email}')")
    conn.commit()
    cursor.close()
    conn.close()
    create_log()
    create_log(
        f'Saved Seller {name_seller} with phone {phone} and email {email}'
    )

def read_sellers() -> list:
    list_seller = []

    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM seller')
    sellers = cursor.fetchall()
    for s in sellers:
        seller = {'name': s[1], 'phone': s[2], 'email': s[3]}
        list_seller.append(seller)
    cursor.close()
    conn.close()
    create_log(f'Read sellers in seller table')
    return list_seller