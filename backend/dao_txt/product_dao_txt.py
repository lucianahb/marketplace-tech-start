import json
from backend.controller.log_controller import create_log


_path_file = ('database/product.txt')


def save_prod(product: str, description: str, price: str) -> None:
    """Save a product in the products.txt file and record this action in the log.

    Args:
        product (str): Product name
        description (str): Product description
        price (str): Product price
    """
    file_ = open(_path_file, 'a')
    string_prod = f'{{"name": "{product}", "description": "{description}", "price": "{price}"}}\n'
    file_.write(string_prod)
    file_.close()


def read_products() -> list:
    """Reads the data file and returns it as a list

    Args:
        _path_file (str): File path. Example: 'product / product_list.txt'

    Returns:
        list: List containing the lines of the read file
    """
    list_products = []
    file_ = open(_path_file, 'r')
    for line_in_file in file_:
        line = line_in_file.strip()
        json_line = json.loads(line)
        list_products.append(json_line)
    file_.close()
    return list_products