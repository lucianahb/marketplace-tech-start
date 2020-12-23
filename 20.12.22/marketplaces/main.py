from marketplaces import Marketplace, Category

def menu():
    options = ['Submarino', 'Via Varejo', 'B2W', 'Zoom', 'Sair']

    print('\nMENU: ')

    for i, option in enumerate(options):
        print(f'[{i+1}] - {option}')

    op = int(input('Selecione uma opção: '))
    return op

while True:
    try:
        op = menu()
        if op == 1:
            print(op)
            resultado = Category.categories.keys()
        elif op == 2:
            resultado = sub(valor1, valor2)
        elif op == 3:
            resultado = multi(valor1, valor2)
        elif op == 4:
            resultado = divi(valor1, valor2)
        elif op == 5:
            exit(0) #tentar alterar
        else:
            print('Digite uma opção válida!')
        print(f'Agora escolha uma categoria: {resultado}.')
        
    except ValueError:
        print('Opção indisponível. Tente novamente.')
    