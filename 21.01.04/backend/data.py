from datetime import datetime


def write_mkp(marketplace, description):
    arq = open('21.01.04/backend/marketplace.txt', 'a')
    string_mtp = f'{marketplace};{description}\n'
    arq.write(string_mtp)
    arq.close()


def write_prod(product, description, price):
    arq = open('21.01.04/backend/product.txt', 'a')
    string_prod = f'{product};{description};{price}\n'
    arq.write(string_prod)
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
    write_prod(product, description, price)
    write_log(
        f'Saved Product {product} with description {description} and price {price}'
    )
