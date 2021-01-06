import sys
from flask import Flask, render_template, request

sys.path.append('.')


from backend.data import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/createmkp')
def createmkp():
    return render_template('createmkp.html')


@app.route('/marketplace')
def savemkp():
    name = request.args.get('name')
    description = request.args.get('description')
    save_mkp(name, description)
    return '<h1> Marketplace saved! </h1>'


@app.route('/createprod')
def createprd():
    return render_template('createprod.html')


@app.route('/product')
def saveprod():
    name = request.args.get('name')
    description = request.args.get('description')
    price = request.args.get('price')
    save_prod(name, description, price)
    return '<h1> Product saved! </h1>'

@app.route('/list_marketplace')
def table_mkp():    
    l_aux = lista_txt('backend/marketplace.txt')
    l_table = []


    print(l_aux)
    for i in l_aux:
        
        i_aux=i.split(';')
        l_table.append({'nome': i_aux[0],'desc': i_aux[1],'rota': '/'})

    return render_template('table_marketplace.html',lista =l_table)



app.run()
