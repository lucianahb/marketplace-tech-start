def write_mkp(marketplace, description):  
    arq = open('21.01.04/data/marketplace.txt', 'a')
    string_mtp = f'{marketplace};{description}\n'
    arq.write(string_mtp)
    arq.close()
    
def write_prod(product, description, price):
    arq = open('21.01.04/data/product.txt', 'a')
    string_prod = f'{product};{description};{price}\n'
    arq.write(string_prod)
    arq.close()

def save_mkp(marketplace, description):
    write_mkp(marketplace, description)

def save_prod(product, description, price):
    write_prod(product, description, price)

