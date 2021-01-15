import sys
sys.path.append('.')

from backend.controller.base_controller import Basecontroller
from backend.dao.marketplace_dao import Marketplacedao

class Marketplacecontroller(Basecontroller):

    def __init__(self):
        self.__dao = Marketplacedao()
        super().__init__(self.__dao)
