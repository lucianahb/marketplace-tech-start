from backend.dao.marketplace_dao import save_mkp, read_marketplace
from backend.controller.log_controller import create_log
from backend.models.marketplace import *

def create_marketplace(marketplace:Marketplace) -> None:
    save_mkp(marketplace)
    create_log(f'Saved Marketplace {marketplace.name_mkt} with description {marketplace.description}')

def listall_marketplace():
    list_marketplace = read_marketplace()
    create_log(f'Read marketplaces in marketplace table')
    return list_marketplace