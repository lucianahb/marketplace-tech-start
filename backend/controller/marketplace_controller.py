from backend.dao_txt.marketplace_dao_txt import save_mkp, read_marketplace

def create_marketplace(marketplace: str, description: str) -> None:
    save_mkp(marketplace, description)


def listall_marketplace():
    list_marketplace = read_marketplace()
    return list_marketplace