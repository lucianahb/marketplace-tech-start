from calculadora import soma, subtracao, multiplicacao, divisao

try:
    valor1 = float(imput('Digite um numero: '))
    valor2 = float(imput('Digite um segundo numero: '))
    resultado = divisao(valor1,valor2)
    print(f'{resultado:.2f}')
except ZeroDivisionError as e_z:
    print('Erro de divisão por zero')
except Exception as e:
    print('Erro qualquer')