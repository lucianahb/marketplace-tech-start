from backend.controller.base_controller import BaseController
from backend.dao.log_dao import *


class LogController(BaseController):
    def __init__(self) -> None:
        self.__dao = LogDao()
        super().__init__(self.__dao)