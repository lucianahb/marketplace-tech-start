from backend.dao.category_dao import save_category, read_categories
from backend.controller.log_controller import create_log
from backend.models.category import Category


def create_category(category: Category) -> None:
    save_category(category)
    create_log(f'Saved category {category.name} with description {category.description}')


def listall_categories():
    list_categories = read_categories()
    create_log(f'Read categories in category table')
    return list_categories