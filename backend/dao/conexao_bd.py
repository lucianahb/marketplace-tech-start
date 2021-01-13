def conexao()-> str:
    host='pgsql08-farm15.uni5.net'
    user='topskills7'
    password='olist21'
    database='topskills7'
    connection_string = f"host={host} user={user} dbname={database} password={password}"
    return connection_string