import psycopg2


class Connection:
    def __get_connection(self)-> str:
        host='pgsql08-farm15.uni5.net'
        user='topskills7'
        password='olist21'
        database='topskills7'
        connection_string = f"host={host} user={user} dbname={database} password={password}"
        return connection_string


    def __enter__(self):
        self.__connection = psycopg2.connect(self.__get_connection())
        return self.__connection
        
        
    def __exit__(self, type, value, trace):
        self.__connection.close()    
        