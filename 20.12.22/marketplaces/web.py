# pip3 install flask
# which pip3 -  caminho da instalacao do pip3
from flask import Flask, render_template
from marketplaces import Marketplace, Category, Subcategory

app = Flask(__name__)

mktplaces = [Marketplace('Amazon'), Marketplace('B2W'), Marketplace('Zoom'), Marketplace('Carrefour'), Marketplace('Sair')]
categorias = [Category('Móveis', mktplaces[1]), Category('Telefonia', mktplaces[0]), Category('Eletrodomésticos', mktplaces[1])]
subcategorias = [Subcategory('Sofá', categorias[0]), Subcategory('Mesa', categorias[0]), Subcategory('Mesa', categorias[1])]


@app.route('/')
def index():
    return render_template('index.html', mktplaces = mktplaces)

@app.route('/category/<mkt>')
def category(mkt):
    return render_template('category.html', cat = categorias, mkt = mkt)


app.run(debug=True)
