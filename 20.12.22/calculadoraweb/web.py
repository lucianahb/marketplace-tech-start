# pip3 install flask
# which pip3 -  caminho da instalacao do pip3
from flask import Flask
from calculadoramaykon import soma, subtrai, multiplica, divide

app = Flask(__name__)

@app.route('/')
def index():
    h1 = '<h1> Calculadora Olist </h1>'
    ol = '''
            <ol> 
                <li><a href='/soma'>Somar</a></li>
                <li><a href='/subtrai'>Subtrair</a></li> 
                <li><a href='/multiplica'>Multiplicar</a></li> 
                <li><a href='/divide'>Dividir</a></li> 
            </ol>
        '''
    return f'{h1} {ol}'

@app.route('/soma')
def somar():
    n1 = 3.0
    n2 = 5.0
    resultado = soma(n1, n2)
    h1 = '<h1> Calculadora </h1>'
    h3 = f'<h3> A soma de {n1} e {n2} é : {resultado}</h3>'
    voltar = "<a href='/'>Voltar</a>"

    return f'{h1} {h3} <br /> {voltar}'

@app.route('/subtrai')
def subtrair():
    n1 = 3.0
    n2 = 5.0
    resultado = subtrai(n1, n2)
    h1 = '<h1> Calculadora </h1>'
    h3 = f'<h3> A subtração de {n1} e {n2} é : {resultado}</h3>'
    voltar = "<a href='/'>Voltar</a>"

    return f'{h1} {h3} <br /> {voltar}'

@app.route('/multiplica')
def multiplicar():
    n1 = 3.0
    n2 = 5.0
    resultado = multiplica(n1, n2)
    h1 = '<h1> Calculadora </h1>'
    h3 = f'<h3> A multiplicação de {n1} e {n2} é : {resultado}</h3>'
    voltar = "<a href='/'>Voltar</a>"

    return f'{h1} {h3} <br /> {voltar}'

@app.route('/divide')
def dividir():
    n1 = 8.0
    n2 = 5.0
    resultado = divide(n1, n2)
    h1 = '<h1> Calculadora </h1>'
    h3 = f'<h3> A divisão de {n1} e {n2} é : {resultado}</h3>'
    voltar = "<a href='/'>Voltar</a>"

    return f'{h1} {h3} <br /> {voltar}'

app.run()