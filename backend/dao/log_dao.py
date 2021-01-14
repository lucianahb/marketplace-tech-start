from backend.models.log import Log
from backend.dao.conexao_bd import Conexao


def save_log(log: Log):
    with Conexao() as conn:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO log (description) VALUES ('{log.description}')")
        conn.commit()


def read_logs() -> list:
    logs = []
    with Conexao() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM log')
        result = cursor.fetchall()
        for l in result:
            log = Log(l[3], l[1], l[2], l[0])
            logs.append(log)     
    return logs