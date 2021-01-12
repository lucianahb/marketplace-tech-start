from backend.dao.seller_dao import save_seller, read_sellers
from backend.models.seller import *


def create_seller(seller:Seller) -> None:
    save_seller(seller)


def listall_seller():
    list_sellers = read_sellers()
    return list_sellers