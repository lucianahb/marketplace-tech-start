import psycopg2
from backend.controller.log_controller import create_log

_host='pgsql08-farm15.uni5.net'
_user='topskills7'
_password='olist21'
_database='topskills7'
_connection_string = f"host={_host} user={_user} dbname={_database} password={_password}"

def save_prod(product: str, description: str, price: str) -> None:
    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO product (name, description, price) VALUES ('{product}', '{description}', '{price}')")
    conn.commit()
    cursor.close()
    conn.close()
    create_log(
        f'Saved Product {product} with description {description} and price {price}'
    )

def read_products() -> list:
    list_product = []

    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM product')
    products = cursor.fetchall()
    for p in products:
        product = {'name': p[1], 'description': p[2], 'price': p[3]}
        list_product.append(product)
    cursor.close()
    conn.close()
    create_log(f'Read products in product table')
    return list_product