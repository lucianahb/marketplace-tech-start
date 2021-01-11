import json
from backend.controller.log_controller import create_log

_path_file = ('database/marketplace.txt')

def save_mkp(marketplace: str, description: str):
    arq = open(_path_file, 'a')
    string_mtp = f'{{"name": "{marketplace}", "description": "{description}"}}\n'
    arq.write(string_mtp)
    arq.close()    
    create_log(
        f'Saved Marketplace {marketplace} with description {description}'
    )

def read_marketplace() -> list:
    """Reads the data file and returns it as a list

    Args:
        _path_file (str): File path. Example: 'product / product_list.txt'

    Returns:
        list: List containing the lines of the read file
    """
    list_marketplace = []
    file_ = open(_path_file, 'r')
    for line_in_file in file_:
        line = line_in_file.strip()
        json_line = json.loads(line)
        list_marketplace.append(json_line)
    file_.close()
    create_log(f'Read marketplace in {_path_file:}')
    return list_marketplace