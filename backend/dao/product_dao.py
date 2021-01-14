from backend.dao.conexao_bd import Conexao
from backend.models.product import Product


def save_product(product: Product) -> None:
    with Conexao() as conn:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO product (name, description, price) VALUES ('{product.name}', '{product.description}', '{product.price}')")
        conn.commit()


def read_products() -> list:
    products = []
    with Conexao() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM product')
        result = cursor.fetchall()
        for p in result:
            product = Product(p[1], p[2], p[3], p[0])
            products.append(product)
    return products


def delete_products(id:int) -> None:
    with Conexao() as conn:
        cursor = conn.cursor()
        cursor.execute(f"delete from product where id = {id};")
        conn.commit()    
        
        
def update_products(product: Product) -> None:    
    with Conexao() as conn:
        cursor = conn.cursor()
        cursor.execute(f"""UPDATE product SET name = '{product.name}', description = '{product.description}',
                       price  = {product.price} WHERE id={product.id};""")
        conn.commit()                
    