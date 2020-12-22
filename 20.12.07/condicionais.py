#estruturas de decisão - condicionais

#if else - Existe
idade = 17
if idade < 0:
    print('idade inválida')
elif idade < 18:
    print('de menor')
else:
    print('de maior')

#ternário - Existe
print('de menor' if idade < 18 else 'de maior')
