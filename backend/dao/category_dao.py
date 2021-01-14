from backend.models.category import Category
from backend.dao.conexao_bd import Conexao


def save_category(category: Category) -> None:
    with Conexao() as conn:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO category (name, description) VALUES ('{category.name}', '{category.description}')")
        conn.commit()


def read_categories() -> list:
    categories = []
    with Conexao() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM category')
        result = cursor.fetchall()
        for c in result:
            category = Category(c[1], c[2], c[0])
            categories.append(category)
    return categories


def delete_categories(id:int) -> None:
    with Conexao() as conn:
        cursor = conn.cursor()
        cursor.execute(f"delete from category where id = {id};")
        conn.commit()    
        
        
def update_categories(category: Category) -> None:    
    with Conexao() as conn:
        cursor = conn.cursor()
        cursor.execute(f"""UPDATE category SET name = '{category.name}', description = '{category.description}'
                    WHERE id={category.id};""")
        conn.commit() 