from backend.dao.seller_dao import save_seller, read_sellers
from backend.controller.log_controller import create_log
from backend.models.seller import *


def create_seller(seller:Seller) -> None:
    save_seller(seller)
    create_log(f'Saved Seller {seller.name_seller} with phone {seller.tel} and email {seller.email}' )


def listall_seller():
    list_sellers = read_sellers()
    create_log(f'Read sellers in seller table')
    return list_sellers