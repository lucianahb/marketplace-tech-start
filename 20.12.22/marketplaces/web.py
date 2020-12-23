# pip3 install flask
# which pip3 -  caminho da instalacao do pip3
from flask import Flask
from marketplaces import Marketplace, Category, Subcategory


app = Flask(__name__)


@app.route('/')
def index():
    h1 = "<h1>Marketplaces</h1>"
    div = '''
            <div>
                <label for="marketplace">Marketplace choices</label>
                <select name="marketplace" required>
                    <option value="">Choose a marketplace</option>
                </select>
            </div>
        '''

    return f'{h1} {div}'


app.run()