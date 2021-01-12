import psycopg2
from backend.models.category import Category
from backend.dao.conexao_bd import *


def save_categories(category: Category) -> None:
    conn = psycopg2.connect(conexao())
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO category (name, description) VALUES ('{category.name}', '{category.description}')")
    conn.commit()
    cursor.close()
    conn.close()


def read_categories() -> list:
    categories = []
    conn = psycopg2.connect(conexao())
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM category')
    result = cursor.fetchall()
    for c in result:
        category = Category(c[1], c[2], c[0])
        categories.append(category)
    cursor.close()
    conn.close()
    return categories