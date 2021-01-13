from backend.dao.conexao_bd import conexao
import psycopg2
from datetime import datetime
from backend.models.log import Log
from backend.dao.conexao_bd import *


def write_log(log: Log):
    conn = psycopg2.connect(conexao())
    cursor = conn.cursor()
    hour_format = datetime.now().strftime('%H:%M:%S - %d/%m/%Y')
    cursor.execute(f"INSERT INTO log (hour_format, msg_log) VALUES ('{hour_format}', '{log.msg_log}')")
    conn.commit()
    cursor.close()
    conn.close()


def read_log() -> list:
    logs = []
    conn = psycopg2.connect(conexao())
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM log')
    result = cursor.fetchall()
    for l in result:
        log = Log(l[2], l[1], l[0])
        logs.append(log)
    cursor.close()
    conn.close()
    return logs