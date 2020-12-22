class Categoria:
    __id: int
    __nome: str

    def __init__(self, id, nome):
        self.__id = id
        self.__nome = nome

    def get_id(self) -> int:
        return self.__id

    def get_nome(self) -> str:
        return self.__nome

    def set_id(self, id: int):
        self.__id = id

    def set_nome(self, nome: str):
        self.__nome = nome

    def print(self):
        print(str(self.__id) + ": " + self.__nome)


class SubCategoria:
    __id: int
    __nome: str
    __pai: Categoria

    def __init__(self, id, nome, pai):
        self.__id = id
        self.__nome = nome
        self.__pai = pai

    def get_id(self) -> int:
        return self.__id

    def get_nome(self) -> str:
        return self.__nome

    def get_pai(self) -> str:
        return self.__pai

    def set_id(self, id: int):
        self.__id = id

    def set_nome(self, nome: str):
        self.__nome = nome

    def set_pai(self, pai: Categoria):
        self.__pai = pai

    def print(self):
        print(str(self.__id) + ": " + self.__nome + " -> " + self.__pai.get_nome())
