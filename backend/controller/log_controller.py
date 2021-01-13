from backend.dao.log_dao import write_log, read_log
from backend.models.log import Log


def create_log(msg: str) -> None:
    log = Log(msg)
    write_log(log)


def listall_log():
    list_log = read_log()
    return list_log