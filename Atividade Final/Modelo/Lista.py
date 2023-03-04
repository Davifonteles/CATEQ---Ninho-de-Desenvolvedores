class Lista:
    def __init__(self, id, id_cliente, nome):
        self._id = id
        self._id_cliente = id_cliente
        self._nome = nome

    def setId_cliente(self, novoId_cliente):
        self._id_cliente = novoId_cliente
    def getId_cliente(self):
        return self._id_cliente
    
    def setNome(self, novoNome):
        self._nome = novoNome
    def getNome(self):
        return self._nome
    
    def inserirLista(self):
        query = (f'''
                INSERT INTO colecao (id_cliente, nome)
                                        VALUES (' {self._id_cliente}', '{self._nome}')
                ''')
        return query
    
    def visualizarLista(self):
        query = (f'''
                  SELECT id, nome FROM Colecao
                      WHERE id_cliente = '{self._id_cliente}'
                ''')
        print("Sua lista de coleções")
        for colecao in query:
            print(f"{colecao[0]} - {colecao[1]}")

    def deletarLista(self):
        query = (f'''
                DELETE FROM colecao
                    WHERE id = '{self._id}'
                ''')
        return query