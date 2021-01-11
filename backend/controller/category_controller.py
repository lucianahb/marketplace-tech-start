from backend.dao.category_dao import save_categories, read_categories

def create_categories(category: str, description: str) -> None:
    save_categories(category, description)


def listall_categories():
    list_categories = read_categories()
    return list_categories