from backend.models.product import Product
from .base_dao import BaseDao


class ProductDao(BaseDao):
    def save(self, product: Product) -> None:
        query = f"""INSERT INTO product (name, description, price) VALUES ('{product.name}', 
        '{product.description}', '{product.price}');"""
        super().execute(query)


    def read(self) -> list:
        products = []
        query = 'SELECT * FROM product;'
        result = super().read(query)
        for p in result:
            product = Product(p[1], p[2], p[3], p[0])
            products.append(product)
        return products


    def delete(self, id:int) -> None:
        query = f"delete from product where id = {id};"
        super().execute(query)    
            
            
    def update(self, product: Product) -> None:    
        query = f"""UPDATE product SET name = '{product.name}', description = '{product.description}',
                        price  = {product.price} WHERE id={product.id};"""
        super().execute(query)              
        