from backend.dao.log_dao import write_log, read_log

def create_log(log: str) -> None:
    write_log(log)


def listall_log():
    list_log = read_log()
    return list_log