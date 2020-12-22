#12/04/2020
#Aulas 1, 2 e 3 com Mykon

# VARIÁVEIS

# tipos
int
str
bool
float
print('\n...............')
#mas não declaro tipo, declaro assim: 
idade = 18
print( id(idade)) #id pega endereço da memória
nome = "Luciana"
verdadeiro = False
salario = 1800.00

#variável reserva um endereço na memória
#o que acontece com isso?
idade = "De Maior"
print( id(idade))

idade = 18
print( id(idade)) #id pega endereço da memória

idade = "De Maior"
print( id(idade))
print('...............\n')

#python identifica tipo, aloca memória.
#___________________________________________________

#VARIÁVEIS
#list
nomes_l = ['maykon', 'joelma', 1, 5, [3, 2, 4]]
print(nomes_l[4])  #[3, 2]
print(nomes_l)  #printa tudo
#print(nomes_l[3][1])


#tupla
nomes_t = ('maykon', 'joelma', 1, 5, [3, 2, 4])
# não posso: nomes_t[1] = 'chimbinha' porque tupla não suporta mudança

#dict
pessoa_1 = {
    'nome': 'Maykon',
    'idade': 18
}
print(pessoa_1['nome'])

#set
#é parcialmente mutável
#posso adicionar, remover valores, dar update
#o legal do set é que ele remove os repetidos
#ele se ordena randomicamente!!
conjunto = {1, 2, 3, 'luciana', 4, 4}
#ou posso declarar dessa forrma:
conjunto_1 = set([4, 5, 6, 7, 8])
print(conjunto.union(conjunto_1))
print('...............\n')


import math as m
#m. aparecem todas funções dessa biblioteca
potencia = m.pow(3,2)
print(potencia)

print('...............\n')


