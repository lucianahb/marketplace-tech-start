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


def save_prod(product, description, price):
    arq = open('21.01.04/backend/product.txt', 'a')
    string_prod = f'{{"name": "{product}", "description": "{description}", "price": "{price}"}}\n'
    arq.write(string_prod)
    arq.close()
    write_log(
        f'Saved Product {product} with description {description} and price {price}'
    )
    
    
def read_historic(path_file: str) -> list:
    file_lines = []
    file_ = open(path_file, 'r')
    for line_in_file in file_:
        line = line_in_file.strip()
        json_line = json.loads(line)
        file_lines.append(json_line)
    file_.close()
    return file_lines


def read_products(products_list: list):
    pass

dic = read_historic('21.01.04/backend/product.txt')
print(dic)
for l in dic:
    print(l['name'])