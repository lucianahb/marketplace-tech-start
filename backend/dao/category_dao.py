from backend.models.category import Category
from .base_dao import BaseDao


class CategoryDao(BaseDao):
    def save(self, category: Category) -> None:
        query = f"INSERT INTO category (name, description) VALUES ('{category.name}', '{category.description}');"
        super().execute(query)


    def read(self) -> list:
        categories = []
        query = 'SELECT * FROM category;'
        result = super().read(query)
        for c in result:
            category = Category(c[1], c[2], c[0])
            categories.append(category)
        return categories


    def delete(self, id:int) -> None:
        query = f"delete from category where id = {id};"
        super().execute(query)
            
            
    def update(cseld, category: Category) -> None:    
        query = f"""UPDATE category SET name = '{category.name}', description = '{category.description}'
                        WHERE id={category.id};"""
        super().execute(query)