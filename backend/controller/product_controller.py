from backend.dao_txt.product_dao_txt import save_prod, read_products

def create_product(product: str, description: str, price: str) -> None:
    save_prod(product, description, price)


def listall_product():
    list_products = read_products()
    return list_products