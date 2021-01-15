from flask import Flask, render_template, request,redirect
import sys
sys.path.append('.')

from backend.controller.category_controller import CategoryController
from backend.controller.log_controller import LogController
from backend.controller.marketplace_controller import *
from backend.controller.product_controller import ProductController
from backend.controller.seller_controller import *
from backend.models.seller import *
from backend.models.marketplace import *
from backend.models.product import Product
from backend.models.category import Category
from backend.models.log import Log

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def index():
    return render_template('index.html')

#-------------------marketplace--------------------------------------
@app.route('/createmkp')
def createmkp():
    return render_template('createmkp.html',nome="",descri="",id="",rota="/marketplace")


@app.route('/marketplace')
def savemkp():
    name = request.args.get('name')
    description = request.args.get('description')
   
    market=Marketplace(name,description)
    m=Marketplacecontroller()
    m.create(market)   
    return render_template('succes.html')

@app.route('/list_marketplace')
def table_mkp():
    m=Marketplacecontroller()
    l_aux = m.listall()   
    return render_template('table_marketplace.html',lista =l_aux)

@app.route('/delete_marketplace')
def deletar_mkt():
    id_del = request.args.get('id')
    m=Marketplacecontroller()
    m.delete(id_del)
    return redirect('/list_marketplace')

@app.route('/form_marketplace')
def up_mkt():
    id_up = request.args.get('id')
    nome_aux=request.args.get('name')
    descri_aux= request.args.get('desc')
    return render_template('createmkp.html',nome=nome_aux,descri=descri_aux,id=id_up,rota="/update_bd_marketplace")

@app.route('/update_bd_marketplace')
def update_bd_mkt():
    id_up_bd = request.args.get('identi')
    nome_aux_bd=request.args.get('name')
    descri_aux_bd= request.args.get('description')

    market=Marketplace(nome_aux_bd,descri_aux_bd,id_up_bd)
    m=Marketplacecontroller()
    m.update(market)
    return redirect('/list_marketplace')

#--------------------------------product--------------------------------------------------
@app.route('/createprod')
def createprd():
    return render_template('createprod.html')


@app.route('/product')
def saveprod():
    name = request.args.get('name')
    description = request.args.get('description')
    price = request.args.get('price')
    product = Product(name, description, price)
    ProductController().create(product)
    return render_template('succes.html')

@app.route('/listprod')
def list_products():
    products = ProductController().listall()
    return render_template('listprod.html', products=products)

@app.route('/delete_product')
def delete_products():
    id = int(request.args.get('id'))
    ProductController().delete(id)
    return redirect('/listprod')    


@app.route('/update_product')
def update_products():
    id = request.args.get('id')
    name = request.args.get('name')
    description = request.args.get('description')
    price = request.args.get('price')
    return render_template('createprod.html', update=True, id=id, name=name, description=description, price=price)  


@app.route('/update_product', methods=['POST'])
def save_update_product():
    id = request.form.get('id')
    name = request.form.get('name')
    description = request.form.get('description')
    price = request.form.get('price')
    product = Product(name, description, price, id)
    ProductController().update(product)
    return redirect('/listprod') 


#------------------------------category-------------------------------------------------
@app.route('/listcategory')
def list_categories():
    categories = CategoryController().listall()
   
    return render_template('listcategory.html', categories=categories)


@app.route('/createcategory')
def create_categories():
    return render_template('createcategory.html')


@app.route('/category')
def save_category():
    name = request.args.get('name')
    description = request.args.get('description')
    category = Category(name, description)
    CategoryController().create(category)
    return render_template('succes.html')


@app.route('/delete_category')
def delete_categories():
    id = int(request.args.get('id'))
    CategoryController().delete(id)
    return redirect('/listcategory')    


@app.route('/update_category')
def update_categories():
    id = request.args.get('id')
    name = request.args.get('name')
    description = request.args.get('description')
    return render_template('createcategory.html', update=True, id=id, name=name, description=description)  


@app.route('/update_category', methods=['POST'])
def save_update_category():
    id = request.form.get('id')
    name = request.form.get('name')
    description = request.form.get('description')
    category = Category(name, description, id)
    CategoryController().update(category)  
    return redirect('/listcategory')    
  
#-------------------------------seller------------------------------------------
@app.route('/listseller')
def list_seller():
    s=Sellercontroller()
    sellers = s.listall()
    return render_template('listseller.html', seller_aux=sellers)

@app.route('/createseller')
def create_sellers():
    return render_template('createseller.html',nome="",tel="",email="",id="",rota="/seller")
  
@app.route('/seller')
def grava_seller():
    name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone')

    seller=Seller(name,phone,email)
    s=Sellercontroller()
    s.create(seller)

    return render_template('succes.html')

@app.route('/delete_seller')
def deletar_seller():
    id_del = request.args.get('id')
    s=Sellercontroller()
    s.delete(id_del)
  
    return redirect('/listseller')

@app.route('/form_seller')
def up_seller():
    id_up = request.args.get('id')
    nome_aux=request.args.get('name')
    tel_aux= request.args.get('tel')
    email_aux= request.args.get('email')

    return render_template('createseller.html',nome=nome_aux,tel=tel_aux,email=email_aux,id=id_up,rota="/update_bd_seller")

@app.route('/update_bd_seller')
def update_bd_seller():
    id_up_bd = request.args.get('identi')
    nome_aux_bd=request.args.get('name')
    tel_aux_bd=request.args.get('phone')
    email_aux_bd=request.args.get('email')

    seller=Seller(nome_aux_bd,tel_aux_bd,email_aux_bd,id_up_bd)
    s=Sellercontroller()
    s.update(seller)

    return redirect('/listseller')
  
#-----------------------------------------log------------------------------------------
@app.route('/listlog')
def list_log():
    list_log = LogController().listall()
    return render_template('listlog.html', list_log=list_log)


app.run()
