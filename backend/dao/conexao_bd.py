import psycopg2
class Conexao:
        
    def __get_conexao(self)-> str:
        host='pgsql08-farm15.uni5.net'
        user='topskills7'
        password='olist21'
        database='topskills7'
        connection_string = f"host={host} user={user} dbname={database} password={password}"
        return connection_string


    def __enter__(self):
        self.__conexao = psycopg2.connect(self.__get_conexao())
        return self.__conexao
        
        
    def __exit__(self, type, value, trace):
        self.__conexao.close()    