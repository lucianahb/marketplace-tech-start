#Estruturas de repetição

#while - Existe
par = True
while(par):
    print('par')
    break


#do while - Não existe
#for - Existe
#range é uma função para criação de intervalors
for i in range(10):
    print(i) #printa de 0 a 9

for j in range(2,10):
# início incluso, o fim é -1)
    print(j) #2, 3, 4, 5, 6, 7, 8, 9

for k in range(2,10,2):
# pulando de 2 em 2
    print(k) #2, 4, 6, 8

for l in range(10,1,-1):
# decremento
    print(l) #10, 9, 8, 7, 6, 5, 4, 3, 2

#foreach - Existe porém como for
lista = ['joelma', 'chimbinha', 'pagode japones']
for nome in lista:
    print(nome)

