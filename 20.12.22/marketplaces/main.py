from marketplaces import Marketplace, Category, Subcategory

mktplaces = [Marketplace('Amazon'), Marketplace('B2W'), Marketplace('Zoom'), Marketplace('Carrefour'), Marketplace('Sair')]
categorias = [Category('Móveis', mktplaces[1]), Category('Telefonia', mktplaces[0]), Category('Eletrodomésticos', mktplaces[1])]
subcategorias = [Subcategory('Sofá', categorias[0]), Subcategory('Mesa', categorias[0])]

def menu(): 

    print('\nMENU: ')

    i = 1

    for option in mktplaces:
        print(f'{i} - {option}')
        i += 1

    op = int(input('Selecione uma opção: '))
    return op

while True:
    try:
        op = menu()
        if op == 1:
            print(f'\nVocê escolheu a opção {mktplaces[0]}\n')
            for i in categorias:
                if i.get_parentname() ==  mktplaces[0].get_name():
                    print(i.get_name())
                    
        elif op == 2:
            item = 1
            print(f'\nVocê escolheu a opção {mktplaces[1]}\n')
            for i in categorias:
                if i.get_parentname() ==  mktplaces[1].get_name():
                    print(f'{item} - {i.get_name()}')
                    item += 1
            escolher_cat = int(input(f'Digite uma opção de categoria: '))
            return escolher_cat

        elif op == 3:
            print(f'\nVocê escolheu a opção {mktplaces[2]}\n')
            for i in categorias:
                if i.get_parentname() ==  mktplaces[2].get_name():
                    print(i.get_name())

        elif op == 4:
            print(f'\nVocê escolheu a opção {mktplaces[3]}\n')
            for i in categorias:
                if i.get_parentname() ==  mktplaces[3].get_name():
                    print(i.get_name())
            
        elif op == 5:
            exit(0) #tentar alterar
        else:
            print('Digite uma opção válida!')
        #print(f'Agora escolha uma categoria: {resultado}.')
        break
        
    except ValueError:
        print('Opção indisponível. Tente novamente.')
