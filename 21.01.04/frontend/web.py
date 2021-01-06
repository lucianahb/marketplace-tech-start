import sys
from flask import Flask, render_template, request

sys.path.append('21.01.04/')


from backend.data import save_mkp, save_prod, read_historic

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

@app.route('/listprod')
def list_products():
    products = read_historic('21.01.04/backend/product.txt')
    return render_template('listprod.html', products=products)

app.run(debug=True)
