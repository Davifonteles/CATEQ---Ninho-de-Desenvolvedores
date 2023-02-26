from psycopg2 import connect

class Conexao:
    
    def __init__(self, parametroDb, parametroHost, parametroPort, parametroUser, parametroPassword):
        self._conexao = connect(database = parametroDb, host = parametroHost, port = parametroPort, user = parametroUser, password = parametroPassword)

    def consultarBanco(self, sql):
        cursor = self._conexao.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        cursor.close()
        return resultado

    def manipularBanco(self, sql):
        cursor = self._conexao.cursor()
        cursor.execute(sql)
        self._conexao.commit()  
        cursor.close