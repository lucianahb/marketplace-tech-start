import sys
sys.path.append('.')

from backend.controller.base_controller import BaseController
from backend.dao.seller_dao import Sellerdao

class Sellercontroller(BaseController):

    def __init__(self):
        self.__dao = Sellerdao()
        super().__init__(self.__dao)
