import psycopg2
from backend.controller.log_controller import create_log

_host='pgsql08-farm15.uni5.net'
_user='topskills7'
_password='olist21'
_database='topskills7'
_connection_string = f"host={_host} user={_user} dbname={_database} password={_password}"

def save_mkp(marketplace: str, description: str):
    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO marketplace (name, description) VALUES ('{marketplace}', '{description}')")
    conn.commit()
    cursor.close()
    conn.close()
    create_log(
        f'Saved Marketplace {marketplace} with description {description}'
    )

def read_marketplace() -> list:
    list_marketplace = []

    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM marketplace')
    marketplaces = cursor.fetchall()
    for m in marketplaces:
        marketplace = {'name': m[1], 'description': m[2]}
        list_marketplace.append(marketplace)
    cursor.close()
    conn.close()
    create_log(f'Read marketplaces in marketplace table')
    return list_marketplace