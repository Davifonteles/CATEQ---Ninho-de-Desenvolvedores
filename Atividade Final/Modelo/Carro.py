class Carro:
    def __init__(self, id, nome, numLugares, ano, modelo):
        self._id = id
        self._nome = nome
        self._numLugares = numLugares
        self._ano = ano
        self._modelo = modelo

    def setNome(self, novoNome):
        self._nome = novoNome
    def getNome(self):
        return self._nome
    
    def setNumLugares(self, novoNumLugares):
        self._numLugares = novoNumLugares
    def getNumLugares(self):
        return self._numLugares
    
    def setAno(self, novoAno):
        self._ano = novoAno
    def getAno(self):
        return self._ano
    
    def setModelo(self, novoModelo):
        self._modelo = novoModelo
    def getModelo(self):
        return self._modelo
    
    def inserirCarro(self):
        query = (f'''
                INSERT INTO "carros"
                  VALUES(DEFAULT, '{self._nome}', '{self._numLugares}', '{self._ano}', {self._modelo}')
                ''')
        return query
    
    def verCarro(self):
        print(f'''
        ID - {self._id}
        Nome - {self._nome}
        Número de Lugares - {self._numLugares}
        Ano - {self._ano}
        Modelo - {self._modelo}
        ''')

    def mudarCarro(self):
        query = (f'''
                UPDATE "Carros"
                  SET "nome" = '{self._nome}',
                      "numLugares" = '{self._numLugares}',
                      "ano" = '{self._ano}',
                      "modelo" = '{self._modelo}'
                  WHERE "id" = '{self._id}'
                ''')
        return query
    
    def deletarCarro(self):
        query = (f'''
                DELETE FROM "Carros"
                  WHERE "id" = {self._id}
                ''')
        return query