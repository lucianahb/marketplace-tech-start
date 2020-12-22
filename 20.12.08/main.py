import Categorias
import Produtos

def Criar_categorias(categorias_set):
    file = 'categories.csv'
    #extrai categoria do arquivo
    with open(file, newline='') as csvfile:
        reader = list(csv.reader(csvfile, delimiter=","))
        reader.pop(0)  # remove uma coluna

    cont = 1
    # Insere categorias na lista
    for row in reader:
        cat = Categoria(cont, row[0])
        lista_categorias.append(cat)
        cont += 1

def Listar_categorias(lista_categorias):
    print("categorias:")
    for cat in lista_categorias:
        cat.print()

def Pesquisar_categoria(id, lista_categorias) -> Categoria:
    for cat in lista_categorias:
        if cat.get_id() == id:
            return cat
    print("Categoria não encontrada!")
    return None

def Criar_subcategoria(lista_categorias, lista_subcategorias):
    print("Let's create a new subCategoria:")
    nome = input("Subcategorias nome: ")
    print("Now, tell me the id of the pai Categoria of this new one: ")
    Listar_categorias(lista_categorias)
    pai_id = int(input())
    pai = None

    for cat in lista_categorias:
        if cat.get_id() == pai_id:
            print(cat.get_nome())
            pai = cat
            id = len(lista_subcategorias) + 1
            sub = SubCategoria(id, nome, pai)
            lista_subcategorias.append(sub)
            return

def Listar_subcategoria(lista_subcategorias):
    print("Subcategorias")
    for sub in lista_subcategorias:
        sub.print()

def Pesquisar_subcategoria(id, lista_subcategorias) -> SubCategoria:
    for sub in lista_subcategorias:
        if sub.get_id() == id:
            return sub
    print("SubCategoria not found!")
    return None

def Criar(lista_categorias, lista_subcategorias) -> Produto:
    nome = input("Nome do Produto: ")
    descricao = input("Descrição (+20 carcteres): ")
    preco = float(input("Preço (R$): "))
    peso = float(input("Peso (g): "))
    altura = float(input("Altura (cm): "))
    largura = float(input("Largura (cm): "))
    comprimento = float(input("Comprimento (cm): "))

    p = Produto(nome)
    p.set_descricao(descricao)
    p.set_preco(preco)
    p.set_peso(peso)
    p.set_altura(altura)
    p.set_largura(largura)
    p.set_comprimento(comprimento)

    print("Categorias: ")

    Listar_categorias(lista_categorias)
    cat = 1

    while(cat != 0):
        cat = int(input("Digite o número da categoria (ou 0 para concluir): "))
        if(cat > 0):
            c = Pesquisar_categoria(cat, lista_categorias)
            if c is not None:
                p.add_Categoria(c)

    print("Se você criou uma categoria, digite o número correspondente: ")

    Listar_subcategoria(lista_subcategorias)
    sub = 1

    while (sub != 0):
        sub = int(input("SubCategoria ID (0 to end): "))
        if (sub > 0):
            s = Pesquisar_subcategoria(sub, lista_subcategorias)
            if s is not None:
                p.add_subCategoria(s)

    return p

'''
def Planilha():
    print('\n--- Planilha de Produtos ---')
    print('-----------------------------')
    for nome in lista_produtos.index: ###Não sei fazer
        print(f'Nome: {nome}')
        print('-----------------------------')
    input('\n(Pressione qualquer tecla para continuar)')
'''

def Pesquisar(lista_produtos, key) -> Produto:
    for p in lista_produtos:
        if p.get_nome() == key:
            return p

    print('Não foi encontrado o produto' + key)
    return None

def Atualizar(lista_produtos):
    key = input("Nome do produto a ser atualizado: ")
    p = Pesquisar(lista_produtos, key)

    if p is None:
        print("Produto not found!")
    else:
        print("Let's update it then!")
        print("Current nome: " + p.get_nome())
        nome = input("New nome: ")
        p.set_nome(nome)
        print()
        print("Current descricao: " + p.get_descricao())
        descricao = input("New descricao: ")
        p.set_descricao(descricao)
        print()
        print("Current preco: " + str(p.get_preco()))
        preco = float(input("New preco: "))
        p.set_preco(preco)
        print()
        print("Current peso: " + str(p.get_peso()))
        peso = float(input("New peso: "))
        p.set_peso(peso)
        print()
        print("Current altura: " + str(p.get_altura()))
        altura = float(input("New altura: "))
        p.set_altura(altura)
        print()
        print("Current largura: " + str(p.get_largura()))
        largura = float(input("New largura: "))
        p.set_largura(largura)
        print()
        print("Current comprimento: " + str(p.get_comprimento()))
        comprimento = float(input("New comprimento: "))
        p.set_comprimento(comprimento)

        print("Current categorias: ")
        Listar_categorias(p.get_categorias())
        p.clear_categorias()

        print("Now, please choose which categorias it should be included in: ")

        Listar_categorias(lista_categorias)
        cat = 1

        while (cat != 0):
            cat = int(input("Categoria ID (0 to end): "))
            if (cat > 0):
                c = Pesquisar_categoria(cat, lista_categorias)
                if c is not None:
                    p.add_Categoria(c)

        print("Current Subcategorias: ")
        Listar_subcategoria(p.get_subcategorias())
        p.clear_subcategorias()

        print("Now, please choose which subcategorias it should be included in: ")

        Listar_subcategoria(lista_subcategorias)
        sub = 1

        while (sub != 0):
            sub = int(input("SubCategoria ID (0 to end): "))
            if (sub > 0):
                s = Pesquisar_subcategoria(sub, lista_subcategorias)
                if s is not None:
                    p.add_subCategoria(s)

        print("Produto successfully updated!")

def Deletar(lista_produtos):
    key = input("Digite o nome do produto a ser deletado: ")
    p = Pesquisar(lista_produtos, key)

    if p is None:
        print("Produto não encontrado")

    else:
        lista_produtos.remove(p)

opcao = -1
lista_produtos = list()
lista_categorias = list()
lista_subcategorias = list()

Criar_categorias(lista_categorias)
Listar_categorias(lista_categorias)

def Menu() -> int:
    opcao = -1

    while opcao < 0 or opcao > 5:
        print(40 * '*')
        opcao = int(input('''
        -------- MENU --------
        1 - Criar novo produto
        2 - Pesquisar produto
        3 - Editar um produto
        4 - Deletar produto
        5 - Criar nova subcategoria
        0 - Sair
        ----------------------
        Digite o número correspondente: '''))
        print()
    return opcao

while opcao != 0:
    opcao = Menu()

    if opcao == 1:
        lista_produtos.append(Criar(lista_categorias, lista_subcategorias))
    elif opcao == 2:
        key = input("Digite o nome do produto para pesquisá-lo: ")
        p = Pesquisar(lista_produtos, key)
        if p is not None:
            p.print()
    elif opcao == 3:
        Atualizar(lista_produtos)
    elif opcao == 4:
        Deletar(lista_produtos)
    elif opcao == 5:
        Criar_subcategoria(lista_categorias, lista_subcategorias)
        Listar_subcategoria(lista_subcategorias)
    #elif opcao == 6:
        #Planilha()
    elif opcao > 5 or opcao < 0:
        print('Opção inválida')
