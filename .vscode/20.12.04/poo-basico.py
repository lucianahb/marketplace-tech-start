class Pessoa:
    nome = 'luciana'
    sobrenome = 'barbosa'
    idade = 25
#quando quero que outras pessoas usem minha classe
#devo criar uma variável pra ela
p = Pessoa()
print(p)
#só que assim só vai pegar onde tá na memória, então:
print(p.nome)
print('...............\n')

#Maaaas, por padrão, não defino valores pra classe, pra proteger ela
#(type hinting) = dica de tipo, não é obrigatório o tipo
class PessoaCerta:
    __nome : str
    sobrenome : str
    idade : int

    #Funções em python: e uso o self pq ele tá dentro do escopo
    def nome_completo(self) -> None:
        print(self.nome + ' ' + self.sobrenome)

    def get_idade(self)->int:
        return self.idade

    def set_idade(self, idade:int)-> None:
        self.idade = idade     
    

p1 = PessoaCerta()
p1.nome = 'LUCIANA'
p1.sobrenome = 'HEIT'
p1.set_idade(25)

print(p1.nome_completo())
print(p1.get_idade())

#um underline antes da variável é protegido: _nome
#2 underline antes da variável é privado: __nome

p = Pessoa()
p.set_idade(10)


print(p.ge)