import psycopg2
from datetime import datetime

_host='pgsql08-farm15.uni5.net'
_user='topskills7'
_password='olist21'
_database='topskills7'
_connection_string = f"host={_host} user={_user} dbname={_database} password={_password}"

def write_log(log: str):
    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()
    hour_format = datetime.now().strftime('%H:%M:%S - %d/%m/%Y')
    cursor.execute(f"INSERT INTO log (hour_format, msg_log) VALUES ('{hour_format}', '{log}')")
    conn.commit()
    cursor.close()
    conn.close()

def read_log() -> list:
    list_log = []

    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM log')
    logs = cursor.fetchall()
    for l in logs:
        log = (f'{l[1]} - {l[2]}')
        list_log.append(log)
    cursor.close()
    conn.close()
    return list_log