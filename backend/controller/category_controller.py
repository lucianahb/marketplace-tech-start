from backend.dao.category_dao import *
from backend.controller.log_controller import create_log
from backend.models.category import Category


def create_category(category: Category) -> None:
    save_category(category)
    create_log(f'Saved category {category.name} with description {category.description}')


def listall_categories():
    list_categories = read_categories()
    create_log(f'Read categories in category table')
    return list_categories


def delete_category(id:int) -> None:
    delete_categories(id)
    create_log(f'Deleted category ID {id}')
    
    
def update_category(id: int, name:str, description: str) -> None:
    category = Category(id=id, name=name, description=description)
    update_categories(category)  
    create_log(f'Updated category {category.name} with description {category.description}')