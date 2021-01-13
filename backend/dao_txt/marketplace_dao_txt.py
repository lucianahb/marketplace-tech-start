import json
from backend.controller.log_controller import create_log
from backend.models.marketplace import *

_path_file = ('database/marketplace.txt')

def save_mkp(marketplace:Marketplace):
    arq = open(_path_file, 'a')
    string_mtp = f'{marketplace.name_mkt};{marketplace.description}\n'
    arq.write(string_mtp)
    arq.close()    
  
def read_marketplace() -> list:
    """Reads the data file and returns it as a list

    Args:
        _path_file (str): File path. Example: 'product / product_list.txt'

    Returns:
        list: List containing the lines of the read file
    """
    list_marketplace = []
    file_ = open(_path_file, 'r', encoding='utf-8')

    for line_in_file in file_:

        linha=line_in_file.split(";")
        obj_mkt=Marketplace(linha[0],linha[1])
        list_marketplace.append(obj_mkt)    
    
    file_.close()
    
    return list_marketplace