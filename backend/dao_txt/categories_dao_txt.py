import json
from backend.controller.log_controller import create_log


_path_file = ('database/categories.txt')


def save_categories(category: str, description: str) -> None:
    """Save a category in the categories.txt file and record this action in the log.

    Args:
        category (str): Category name
        description (str): Category description
    """
    file_ = open(_path_file, 'a')
    string_prod = f'{{"name": "{category}", "description": "{description}"}}\n'
    file_.write(string_prod)
    file_.close()


def read_categories() -> list:
    """Reads the data file and returns it as a list

    Args:
        _path_file (str): File path. Example: 'product / product_list.txt'

    Returns:
        list: List containing the lines of the read file
    """
    list_categories = []
    file_ = open(_path_file, 'r')
    for line_in_file in file_:
        line = line_in_file.strip()
        json_line = json.loads(line)
        list_categories.append(json_line)
    file_.close()
    return list_categories