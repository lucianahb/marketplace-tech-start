from datetime import datetime


def write_mkp(marketplace, description):
    arq = open('backend/marketplace.txt', 'a')
    string_mtp = f'{marketplace};{description}\n'
    arq.write(string_mtp)
    arq.close()


def write_prod(product, description, price):
    arq = open('backend/product.txt', 'a')
    string_prod = f'{product};{description};{price}\n'
    arq.write(string_prod)
    arq.close()


def write_log(log):
    hour_format = datetime.now().strftime('%H:%M:%S - %d/%m/%Y')
    arq = open('backend/log.txt', 'a')
    string_log = f'{hour_format} - {log}\n'
    arq.write(string_log)
    arq.close()


def save_mkp(marketplace, description):
    write_mkp(marketplace, description)
    write_log(
        f'Saved Marketplace {marketplace} with description {description}'
    )


def save_prod(product, description, price):
    write_prod(product, description, price)
    write_log(
        f'Saved Product {product} with description {description} and price {price}'
    )

def lista_txt(cam: str) -> list:
    list_aux = []

    arquivo = open(cam, 'r')

    for linha in arquivo:
        linha = linha.strip()
        list_aux.append(linha)

    arquivo.close()

    cam_aux = cam.split('/')
    dado_aux = f'{cam_aux[1]} acessado em :{datetime.now().strftime("%b %d %Y %H:%M:%S")} para mostrar lista.'
   # grava_txt('C:/Users/Gustavo/PycharmProjects/marketplace_categoria/marketplace_categoria/back/txt/log_acesso.txt', dado_aux, 'a')

    return list_aux
