import psycopg2
from backend.controller.log_controller import create_log

_host='pgsql08-farm15.uni5.net'
_user='topskills7'
_password='olist21'
_database='topskills7'
_connection_string = f"host={_host} user={_user} dbname={_database} password={_password}"

def save_categories(category: str, description: str) -> None:
    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO category (name, description) VALUES ('{category}', '{description}')")
    conn.commit()
    cursor.close()
    conn.close()
    create_log(
        f'Saved category {category} with description {description}'
    )

def read_categories() -> list:
    list_category = []

    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM category')
    categories = cursor.fetchall()
    for c in categories:
        category = {'name': c[1], 'description': c[2]}
        list_category.append(category)
    cursor.close()
    conn.close()
    create_log(f'Read categories in category table')
    return list_category