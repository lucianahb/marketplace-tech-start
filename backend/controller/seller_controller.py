from backend.dao.seller_dao import save_seller, read_sellers

def create_seller(name_seller: str, phone: str, email: str) -> None:
    save_seller(name_seller, phone, email)


def listall_seller():
    list_sellers = read_sellers()
    return list_sellers