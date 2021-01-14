from backend.dao.product_dao import *
from backend.models.product import Product
from backend.controller.log_controller import create_log


def create_product(product: Product) -> None:
    save_product(product)
    create_log(f'Saved Product {product.name} with description {product.description} and price {product.price}')


def listall_products() -> list:
    list_products = read_products()
    create_log(f'Read products in product table')
    return list_products


def delete_product(id:int) -> None:
    delete_products(id)
    create_log(f'Deleted product ID {id}')
    
    
def update_product(id: int, name:str, description: str, price:float) -> None:
    product = Product(id=id, name=name, description=description, price=price)
    update_products(product)    
    create_log(f'Updated product {product.name} with description {product.description} and price {product.price}')