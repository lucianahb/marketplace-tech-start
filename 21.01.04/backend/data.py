import json
from datetime import datetime


def write_mkp(marketplace, description):
    arq = open('21.01.04/backend/marketplace.txt', 'a')
    string_mtp = f'{marketplace};{description}\n'
    arq.write(string_mtp)
    arq.close()



def write_log(log):
    hour_format = datetime.now().strftime('%H:%M:%S - %d/%m/%Y')
    arq = open('21.01.04/backend/log.txt', 'a')
    string_log = f'{hour_format} - {log}\n'
    arq.write(string_log)
    arq.close()


def save_mkp(marketplace, description):
    write_mkp(marketplace, description)
    write_log(
        f'Saved Marketplace {marketplace} with description {description}'
    )


def save_prod(product: str, description: str, price: str) -> None:
    """Save a product in the products.txt file and record this action in the log.

    Args:
        product (str): Product name
        description (str): Product description
        price (str): Product price
    """
    file_ = open('21.01.04/backend/product.txt', 'a')
    string_prod = f'{{"name": "{product}", "description": "{description}", "price": "{price}"}}\n'
    file_.write(string_prod)
    file_.close()
    write_log(
        f'Saved Product {product} with description {description} and price {price}'
    )
    
    
def read_historic(path_file: str) -> list:
    """Reads the data file and returns it as a list

    Args:
        path_file (str): File path. Example: 'products / products_list.txt'

    Returns:
        list: List containing the lines of the read file
    """
    file_lines = []
    file_ = open(path_file, 'r')
    for line_in_file in file_:
        line = line_in_file.strip()
        json_line = json.loads(line)
        file_lines.append(json_line)
    file_.close()
    write_log(f'Read historic in {path_file:}')
    return file_lines
