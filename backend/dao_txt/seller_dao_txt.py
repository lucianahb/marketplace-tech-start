import json
from backend.controller.log_controller import create_log

_path_file = ('database/seller.txt')


def save_seller(name_seller: str, phone: str, email: str) -> None:
    """Save a category in the categories.txt file and record this action in the log.

    Args:
        category (str): Category name
        description (str): Category description
    """
    file_ = open(_path_file, 'a')
    string_prod = f'{{"name": "{name_seller}", "phone": "{phone}", "email": "{email}"}}\n'
    file_.write(string_prod)
    file_.close()
    create_log(
        f'Saved Seller {name_seller} with phone {phone} and email {email}'
    )

def read_sellers() -> list:
    """Reads the data file and returns it as a list

    Args:
        _path_file (str): File path. Example: 'seller / seller_list.txt'

    Returns:
        list: List containing the lines of the read file
    """
    list_sellers = []
    file_ = open(_path_file, 'r')
    for line_in_file in file_:
        line = line_in_file.strip()
        json_line = json.loads(line)
        list_sellers.append(json_line)
    file_.close()
    create_log(f'Read sellers in {_path_file:}')
    return list_sellers