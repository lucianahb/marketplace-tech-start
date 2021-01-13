from backend.dao.product_dao import save_product, read_products
from backend.models.product import Product
from backend.controller.log_controller import create_log


def create_product(product: Product) -> None:
    save_product(product)
    create_log(f'Saved Product {product.name} with description {product.description} and price {product.price}')


def listall_products():
    list_products = read_products()
    create_log(f'Read products in product table')
    return list_products