import csv

#classe tem atributos
class Produto:
    __nome: str
    __descricao: str
    __preco: float
    __largura: float
    __altura: float
    __comprimento: float
    __peso: float
    __categorias: list
    __subcategorias: list    
    
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
            descricao = input("descricao too short! Minimum of 20 characters needed: ")
        self.__descricao = descricao

    def get_price(self) -> float:
        return self.__price

    def set_price(self, price):
        while(price <= 0):
            price = float(input("Price should be greater than 0! Enter again please: "))
        self.__price = price

    def get_weight(self) -> float:
        return self.__weight

    def set_weight(self, weight):
        while(weight <= 0):
            weight = float(input("Weight should be greater than 0! Enter again please: "))
        self.__weight = weight

    def get_length(self) -> float:
        return self.__length

    def set_length(self, length):
        while (length <= 0):
            length = float(input("Length should be greater than 0! Enter again please: "))
        self.__length = length

    def get_width(self) -> float:
        return self.__width

    def set_width(self, width):
        while (width <= 0):
            width = float(input("Width should be greater than 0! Enter again please: "))
        self.__width = width

    def get_height(self) -> float:
        return self.__height

    def set_height(self, height):
        while (height <= 0):
            height = float(input("Height should be greater than 0! Enter again please: "))
        self.__height = height

    def get_categorias(self) -> list:
        return self.__categorias

    def get_subcategorias(self) -> list:
        return self.__subcategorias

    def add_category(self, cat):
        self.__categorias.append(cat)

    def clear_categorias(self):
        self.__categorias = list()

    def clear_subcategorias(self):
        self.__subcategorias = list()

    def add_subcategory(self, sub):
        self.__subcategorias.append(sub)   
    
p = Product()
    


#métodos = crud, por exemplo, verbos
#Criar()
#Listar()
#Update()
#Deletar()
#Sair()

