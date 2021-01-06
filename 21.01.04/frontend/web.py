import sys
from flask import Flask, render_template, request

sys.path.append('.')


from backend.data import save_mkp, save_prod, read_historic


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

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
    return render_template('succes.html')


@app.route('/createprod')
def createprd():
    return render_template('createprod.html')


@app.route('/product')
def saveprod():
    name = request.args.get('name')
    description = request.args.get('description')
    price = request.args.get('price')
    save_prod(name, description, price)
    return render_template('succes.html')

@app.route('/list_marketplace')
def table_mkp():    
    l_aux = read_historic('backend/marketplace.txt')
    return render_template('table_marketplace.html',lista =l_aux)


@app.route('/listprod')
def list_products():
    products = read_historic('backend/product.txt')
    return render_template('listprod.html', products=products)


app.run()
