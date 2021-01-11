from backend.dao_txt.categories_dao_txt import save_categories, read_categories

def create_categories(category: str, description: str) -> None:
    save_categories(category, description)


def listall_categories():
    list_categories = read_categories()
    return list_categories