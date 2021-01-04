# pip3 install flask
# which pip3 -  caminho da instalacao do pip3
from flask import Flask, render_template
from marketplaces import Marketplace, Category, Subcategory, Dados

app = Flask(__name__)

mktplaces = []
result_mktplaces = Dados.get_mktplaces()
for i in result_mktplaces:
    mktplaces.append(Marketplace(i['mktplace']))

categorias = []
result_cat = Dados.get_cat()
for i in result_cat:
    for j in mktplaces:
        if i['mkplace'] == j.get_name():
            categorias.append(Category(i['categoria'], j))

subcategorias = []
result_subcat = Dados.get_subcat()
for i in result_subcat:
    for j in categorias:
        if i['categoria'] == j.get_name():
            subcategorias.append(Subcategory(i['subcategoria'], j))
            break

@app.route('/')
def index():
    return render_template('index.html', mktplaces = mktplaces)

@app.route('/category/<mktplaces>')
def category(mktplaces):
    print(mktplaces)
    return render_template('category.html', cat = categorias, mktplaces = mktplaces)

@app.route('/subcategory/<cat>')
def subcategory(cat):
    return render_template('subcategory.html', subcat = subcategorias, cat = cat)

app.run(debug=True)

# mktplaces = [Marketplace('Amazon'), 
#             Marketplace('B2W'), 
#             Marketplace('Zoom'), 
#             Marketplace('Carrefour'), 
#             Marketplace('Sair')]

# categorias = [Category('Móveis', mktplaces[1]), 
#             Category('Telefonia', mktplaces[0]), 
#             Category('Eletrodomésticos', mktplaces[1])]

# subcategorias = [Subcategory('Sofá', categorias[0]), 
#                 Subcategory('Mesa', categorias[0]), 
#                 Subcategory('Samsung', categorias[1])]
