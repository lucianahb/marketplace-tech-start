import sys
sys.path.append('.')

from backend.controller.base_controller import BaseController
from backend.dao.marketplace_dao import Marketplacedao

class Marketplacecontroller(BaseController):

    def __init__(self):
        self.__dao = Marketplacedao()
        super().__init__(self.__dao)
