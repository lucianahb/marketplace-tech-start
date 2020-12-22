from calculadora import soma, sub, multi, divi

def menu():
    options = ['Somar', 'Subtrair', 'Multiplicar', 'Dividir', 'Sair']

    print('\nMENU: ')

    for i, option in enumerate(options):
        print(f'[{i+1}] - {option}')

    op = int(input('Selecione uma opção: '))
    return op

while True:
    try:
        op = menu()
        valor1 = float(input('Digitar um numero: ')) #tentar alterar de lugar
        valor2 = float(input('Digitar um segundo numero: ')) #tentar alterar de lugar
        if op == 1:
            resultado = soma(valor1, valor2)
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
        print(f'O resultado da operação é {resultado}.')
    except ValueError:
        print('Opção indisponível. Tente novamente.')
    