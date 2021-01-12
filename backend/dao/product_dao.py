from backend.dao.conexao_bd import conexao
import psycopg2
from backend.models.product import Product


def save_prod(product: Product) -> None:
    conn = psycopg2.connect(conexao())
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO product (name, description, price) VALUES ('{product.name}', '{product.description}', '{product.price}')")
    conn.commit()
    cursor.close()
    conn.close()


def read_products() -> list:
    products = []
    conn = psycopg2.connect(conexao())
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM product')
    result = cursor.fetchall()
    for p in result:
        product = Product(p[1], p[2], p[3], p[0])
        products.append(product)
    cursor.close()
    conn.close()
    return products