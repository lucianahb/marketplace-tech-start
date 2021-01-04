import sys
from flask import Flask, render_template, request

sys.path.append('21.01.04/data')

from data import save_mkp, save_prod

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
    return '<h1> Marketplace salvo! </h1>'

app.run(debug=True)