class Contato():
    def __init__(self, id, produto, descricao, peso, preco, dimensao):
        self.id = id
        self.produto = produto
        self.descricao = descricao
        self.preco = preco
        self.peso = peso
        self.dimensao = dimensao
        
        '''self.id = int(nput('Digite seu nome: '))
        self.nome = str(nput('Digite seu nome: '))
        self.descricao = str(nput('Digite seu nome: '))
        self.preco = float(nput('Digite seu nome: '))
        self.peso = float(nput('Digite seu nome: '))
        self.dimensoes = float(nput('Digite seu nome: '))
'''
    def __repr__(self):
        return '{},{}'.format(self.id, self.produto)

    def __str__(self):
        return self.__repr__()

    def salve_se(self, arquivo):
        arquivo.write("{}\n".format(self))

    @staticmethod
    def abra_se(line):
        pedacos = line.split(',')
        contato = Contato(pedacos[0],pedacos[1])
        return contato

class Agenda():
    def __init__(self, arquivoPadrao="agendaoo.txt"):
        self.listaDeContatos = []
        self._arquivoPadrao = ""
        self.arquivoPadrao = arquivoPadrao
        try:
            self.abrir_agenda()
        except Exception:
            pass
    @property
    def arquivoPadrao(self):
        return self._arquivoPadrao

    @arquivoPadrao.setter
    def arquivoPadrao(self, arquivo):
        arq, ext = arquivo.split('.')
        if ext!="txt":
            print("Somente extensões txt são aceitas!")
            return
        self._arquivoPadrao = arquivo

    def salvar_agenda(self):
        arquivo = self.arquivoPadrao
        f = open(arquivo, 'w')
        if f.writable():
            for contato in self.listaDeContatos:
                f.write(contato.__repr__())
            print("Agenda salva com sucesso!")
        f.close()

    def novo_contato(self):
        id = input("Entre com o id: ")
        produto = input("Entre com o produto: ")
        self.listaDeContatos.append(Contato(id, produto))
        print("Contato adicionado com sucesso!")

    def abrir_agenda(self):
        arquivo = self.arquivoPadrao
        print(arquivo)
        try:
            f = open(arquivo, 'r')
            if f.readable():
                nContatos = 0
                for line in f.readlines():
                    self.listaDeContatos.append(Contato.abra_se(line.rstrip('\n')))
                    nContatos += 1
                print ("{} contato(s) aberto(s) do disco.".format(nContatos))
                f.close()
        except FileNotFoundError as e:
            print("O arquivo não foi encontrado. {} realmente existe?".format(arquivo))

    def __repr__(self):
        if len(self.listaDeContatos)==0:
            return("Sem contatos adicionados.")
        str = "Lista de Contatos: "
        str+="\n--------------------------------------"
        for contato in self.listaDeContatos:
            str+='\n'+contato.__str__()
        str+="\n--------------------------------------\n"
        return str
'''
def menu():
    print("1- Adicionar \n2- Mostrar \n3- Salvar \n0 - Sair")
    return int(input("Entre com a opção: "))


if __name__ == '__main__':
    minhaAgenda = Agenda()
    op = -10
    while op!=0:
        op = menu()
        if op==1:
            minhaAgenda.novo_contato()
        elif op==2:
            print(minhaAgenda)
        elif op==3 or op==0:
            minhaAgenda.salvar_agenda()
'''
def Menu():
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