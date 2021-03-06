import sys
from flask import Flask, render_template, request

sys.path.append('.')


from backend.data import *



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


@app.route('/listcategory')
def list_categories():
    categories = read_historic('backend/categories.txt')
    return render_template('listcategory.html', categories=categories)

@app.route('/createcategory')
def create_category():
    return render_template('createcategory.html')


@app.route('/category')
def save_category():
    name = request.args.get('name')
    description = request.args.get('description')
    save_categories(name, description)
    return render_template('succes.html')
  

@app.route('/listseller')
def list_seller():
    sellers = read_historic('backend/seller.txt')
    return render_template('listseller.html', seller_aux=sellers)


@app.route('/createseller')
def create_seller():
    return render_template('createseller.html')
  

@app.route('/seller')
def grava_seller():
    name = request.args.get('name')
    email = request.args.get('email')
    save_seller(name,email)
    return render_template('succes.html')
  

@app.route('/listlog')
def list_log():
    list_log = read_log()
    return render_template('listlog.html', list_log=list_log)
  

app.run(debug=True)
