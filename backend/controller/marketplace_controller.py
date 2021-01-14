from backend.dao.marketplace_dao import save_mkp, read_marketplace,delete_marketplace,update_marketplace
from backend.controller.log_controller import create_log
from backend.models.marketplace import *

def create_marketplace(marketplace:Marketplace) -> None:
    save_mkp(marketplace)
    create_log(f'Saved Marketplace {marketplace.name_mkt} with description {marketplace.description}.')

def listall_marketplace():
    list_marketplace = read_marketplace()
    create_log(f'Read marketplaces in marketplace table.')
    return list_marketplace

def delete_item_mkt(id):
    delete_marketplace(id)
    create_log(f'ID {{id}} deleted of the marketplace table.')

def updata_bd_market(m:Marketplace):
    update_marketplace(m)
    create_log(f'ID {{m.id}} in marketplace table updated with name {{m.name_mkt}} and description{{m.description}}.')

