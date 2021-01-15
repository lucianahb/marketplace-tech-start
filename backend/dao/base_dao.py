import sys
sys.path.append('.')

from backend.dao.conexao_bd import Conexao

class Basedao:
    def execute(self,query:str)->None:
        with Conexao() as conn:
            cursor=conn.cursor()
            cursor.execute(query)
            conn.commit()

    def read(self,query:str)->tuple:
        with Conexao() as conn:
            cursor=conn.cursor()
            cursor.execute(query)
            result=cursor.fetchall()
        return result

            

