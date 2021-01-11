from backend.dao.marketplace_dao import save_mkp, read_marketplace

def create_marketplace(marketplace: str, description: str) -> None:
    save_mkp(marketplace, description)


def listall_marketplace():
    list_marketplace = read_marketplace()
    return list_marketplace