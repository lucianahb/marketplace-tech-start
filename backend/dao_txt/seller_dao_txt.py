import json
from backend.controller.log_controller import create_log
from backend.models.seller import *

_path_file = ('database/seller.txt')


def save_seller(seller:Seller) -> None:
    """Save a category in the categories.txt file and record this action in the log.

    Args:
        category (str): Category name
        description (str): Category description
    """
    with open(_path_file, 'a') as file_:
        string_prod = f'{seller.name_seller};{seller.tel};{seller.email}\n'
        file_.write(string_prod)        
 
def read_sellers() -> list:
    """Reads the data file and returns it as a list

    Args:
        _path_file (str): File path. Example: 'seller / seller_list.txt'

    Returns:
        list: List containing the lines of the read file
    """
    list_sellers = []
    with open(_path_file, 'r', encoding='utf-8') as file_:
        for line_in_file in file_:
            linha=line_in_file.split(";")
            obj_seller=Seller(linha[0],linha[1],linha[2])
            list_sellers.append(obj_seller)
    return list_sellers