class Pessoa:
    __nome : str
    __sobrenome : str
    __idade : int

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome: str):
        self.__nome = nome

    def get_sobrenome(self) -> str:
        return self.__sobrenome

    def set_sobrenome(self, sobrenome: str):
        self.__sobrenome = sobrenome

    def get_idade(self) -> int:
        return self.__idade

    def set_idade(self, idade:int):
        self.__idade = idade


p = Pessoa()
p.set_nome('Luciana')
p.set_sobrenome('Barbosa')
p.set_idade(25)

print(p.get_nome(), p.get_sobrenome(), '-', p.get_idade(), 'anos')
