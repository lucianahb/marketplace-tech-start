id_lista = {} #{codigo : produto}
opcao = ''

def Criar():
    codigo = int(input('Digite o ID do produto: '))
    if codigo in id_lista:
        print('Este produto está cadastrado. Digite outro ID')
    else:
        produto = input('Digite o nome do produto: ')
        id_lista[codigo] = produto

def Planilha():
    print('\n--- Planilha de Produtos ---')
    print('-----------------------------')
    for codigo, produto in id_lista.items():
        print(f'ID: {codigo} | Produto: {produto.upper()}')
        print('-----------------------------')
    input('\n(Pressione qualquer tecla para continuar)')

def Atualizar(codigo):
    id_lista[codigo] = input('Digite o novo nome do produto: ')
    print('Nome atualizado!')

def Deletar(codigo):
    del id_lista[codigo]
    input('Produto deletado! (Pressione qualquer tecla para continuar)')

while opcao != 's':
    print('''
        -------- MENU --------
        C = Criar novo produto
        R = Planilha de produtos
        U = Atualizar
        D = Deletar produto
        S = Sair
        ----------------------
    ''')
    opcao = input('Digite uma opção do menu (letra): ').lower()
    if opcao == 'c':
       Criar()
    elif opcao == 'r':
        Planilha()
    elif opcao == 'u':
        Atualizar(int(input('Digite o ID do produto: ')))
    elif opcao == 'd':
        Deletar(int(input('Digite o ID do produto: ')))
    else:
        print('Opção inválida')





