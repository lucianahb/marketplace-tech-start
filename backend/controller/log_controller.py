from backend.dao.log_dao import save_log, read_logs
from backend.models.log import Log


def create_log(msg: str) -> None:
    log = Log(msg)
    save_log(log)


def listall_logs():
    list_log = read_logs()
    return list_log