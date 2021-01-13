from backend.dao.conexao_bd import conexao
import psycopg2
from datetime import datetime
from backend.models.log import Log
from backend.dao.conexao_bd import *


def save_log(log: Log):
    with psycopg2.connect(conexao()) as conn:
        cursor = conn.cursor()
        hour_format = datetime.now().strftime('%H:%M:%S - %d/%m/%Y')
        cursor.execute(f"INSERT INTO log (hour_format, msg_log) VALUES ('{hour_format}', '{log.msg_log}')")
        conn.commit()


def read_logs() -> list:
    logs = []
    with psycopg2.connect(conexao()) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM log')
        result = cursor.fetchall()
        for l in result:
            log = Log(l[2], l[1], l[0])
            logs.append(log)
    return logs