from backend.controller.base_controller import BaseController
from backend.dao.product_dao import *


class ProductController(BaseController):
    def __init__(self) -> None:
        self.__dao = ProductDao()
        super().__init__(self.__dao)