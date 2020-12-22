class Produto:
    __nome: str
    __descricao: str
    __preco: float
    __peso: float
    __dimensoes: str
    __altura: float
    __largura: float
    __comprimento: float
    __categorias: []
    __subcategorias: []


    def __init__(self, nome):
        self.__nome = nome
        self.__categorias = list()
        self.__subcategorias = list()

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome: str):
        self.__nome = nome

    def get_descricao(self) -> str:
        return self.__descricao

    def set_descricao(self, descricao: str):
        while(len(descricao) < 20):
            descricao = input("Mínimo 20 caracteres para descrição: ")
        self.__descricao = descricao

    def get_preco(self) -> float:
        return self.__preco

    def set_preco(self, preco):
        while(preco <= 0):
            preco = float(input("preco should be greater than 0! Enter again please: "))
        self.__preco = preco

    def get_peso(self) -> float:
        return self.__peso

    def set_peso(self, peso):
        while(peso <= 0):
            peso = float(input("peso precisa ser maior que zero: "))
        self.__peso = peso

    def get_altura(self) -> float:
        return self.__altura

    def set_altura(self, altura):
        while (altura <= 0):
            altura = float(input("altura precisa ser maior que zero: "))
        self.__altura = altura

    def get_largura(self) -> float:
        return self.__largura

    def set_largura(self, largura):
        while (largura <= 0):
            largura = float(input("largura precisa ser maior que zero: "))
        self.__largura = largura

    def get_comprimento(self) -> float:
        return self.__comprimento

    def set_comprimento(self, comprimento):
        while (comprimento <= 0):
            comprimento = float(input("comprimento precisa ser maior que zero: "))
        self.__comprimento = comprimento

    def get_categorias(self) -> list:
        return self.__categorias

    def get_subcategorias(self) -> list:
        return self.__subcategorias

    def add_Categoria(self, cat):
        self.__categorias.append(cat)

    def clear_categorias(self):
        self.__categorias = list()

    def clear_subcategorias(self):
        self.__subcategorias = list()

    def add_subCategoria(self, sub):
        self.__subcategorias.append(sub)


    def print(self):
        print("Nome: " + self.__nome)
        print("Descricao: " + self.__descricao)
        print("Preco: " + str(self.__preco))
        print("Peso: " + str(self.__peso))
        print("Altura: " + str(self.__altura))
        print("Largura: " + str(self.__largura))
        print("Comprimento: " + str(self.__comprimento))
        Listar_categorias(self.__categorias)
        Listar_subcategoria(self.__subcategorias)
