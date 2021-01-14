from backend.dao.seller_dao import *
from backend.controller.log_controller import create_log
from backend.models.seller import *


def create_seller(seller:Seller) -> None:
    save_seller(seller)
    create_log(f'Saved Seller {seller.name_seller} with phone {seller.tel} and email {seller.email}' )


def listall_seller():
    list_sellers = read_sellers()
    create_log(f'Read sellers in seller table')
    return list_sellers

def delete_item_seller(id):
    delete_seller(id)
    create_log(f'ID {{id}} deleted of the seller table.')

def updata_bd_seller(id,nome,tel,email):
    update_seller(id,nome,tel,email)
    create_log(f'ID {{id}} in marketplace table updated with name {{nome}}, phone {{descri}} and email {{email}}.')