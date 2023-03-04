class Cliente:
    def __init__(self, id, nome, cpf):
        self._id = id
        self._nome = nome
        self._cpf = cpf

    def setNome(self, novoNome):
        self._nome = novoNome
    def getNome(self):
        return self._nome
    
    def setCpf(self, novoCpf):
        self._cpf = novoCpf
    def getCpf(self):
        return self._cpf
    
    def inserirCliente(self):
     query = (f'''
             INSERT INTO "Cliente"
               VALUES(DEFAULT, '{self._nome}', '{self._cpf}')
             ''')
     return query
    
    def visualizarCliente(self):
        print(f'''
        ID - {self._id}
        Nome - {self._nome}
        CPF - {self._cpf}
        ''')

    def atualizarCliente(self):
     query = (f'''
             UPDATE "Cliente"
               SET "Nome" = '{self._nome}
                   "Cpf" = '{self._cpf}
               WHERE "id" = '{self._id}'
               ''')
     return query
    
    def deletarCliente(self):
     query = (f'''
             DELETE FROM "Cliente"
               WHERE "id" = {self._id}
             ''')
     return query  

    