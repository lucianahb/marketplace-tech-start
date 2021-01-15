from backend.controller.base_controller import BaseController
from backend.dao.category_dao import *


class CategoryController(BaseController):
    def __init__(self) -> None:
        self.__dao = CategoryDao()
        super().__init__(self.__dao)