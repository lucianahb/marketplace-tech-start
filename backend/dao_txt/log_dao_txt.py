import json
from datetime import datetime


_path_file = ('database/log.txt')


def write_log(log: str):
    hour_format = datetime.now().strftime('%H:%M:%S - %d/%m/%Y')
    arq = open(_path_file, 'a')
    string_log = f'{hour_format} - {log}\n'
    arq.write(string_log)
    arq.close()


def read_log() -> list:
    """Read log file

    Returns:
        list: list of log rows
    """
    list_log = []
    log_file = open(_path_file, 'r')
    for row in log_file:
        clean_row = row.strip()
        list_log.append(clean_row)
    return list_log

