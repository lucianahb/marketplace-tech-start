from backend.models.log import Log
from .base_dao import BaseDao


class LogDao(BaseDao):
    def save(self, log: Log) -> None:
        query = f"INSERT INTO log (description) VALUES ('{log.description}');"
        super().execute(query)


    def read(self) -> list:
        logs = []
        query = 'SELECT * FROM log'
        result = super().read(query)
        for l in result:
            log = Log(l[3], l[1], l[2], l[0])
            logs.append(log)     
        return logs