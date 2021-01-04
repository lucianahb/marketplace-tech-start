def write_mkp(marketplace, description):  
    arq = open('marketplace.txt', 'a')
    string_mtp = f'{marketplace};{description}\n'
    arq.write(string_mtp)
    arq.close()
    
def write_prod(product, description, price):
    arq = open('product.txt', 'a')
    string_prod = f'{product};{description};{price}\n'
    arq.close()

def save_mkp(marketplace, description):
    write_mkp(marketplace, description)

def save_prod(product, description, price):
    write_prod(product, description, price)

