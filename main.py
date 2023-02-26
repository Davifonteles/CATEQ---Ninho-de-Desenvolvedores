from psycopg2 import Error
from Controle.ClassConexao import conexao
from Modelo.classLivro import Livro
from Modelo.ClassCliente import Cliente

# DROP TABLE IF EXISTS Clientes
# CREATE TABLE Clientes(
#        id INT GENERATED ALWAYS AS IDENTIFY,
#        nome varchar(255) NOT NULL,
#        cpf char(11) NOT NULL UNIQUE,
#        PRIMARY KEY (id)

# );

# DROP TABLE IF EXISTS Livros
# CREATE TABLE livros(

#        id INT GENERATED ALWAYS AS IDENTIFY,
#        nome varchar(255) NOT NULL,
#        autor varchar(255) NOT NULL,
#        PRIMARY KEY(id)
# );

# DROP TABLE IF EXISTS Aluguel;
# CREATE TABLE Aluguel(
#        id int GENERATED ALWAYS AS IDENTIFY,
#        id_Cliente int NOT NULL,
#        id_Livro int NOT NULL,
#        data_aluguel TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#        PRIMARY KEY(id)

#        Constraint fk_Cliente
#            FOREIGN KEY (id_cliente)
#            ON DELETE CASCADE
#            ON UPDATE NO ACTION

#        Constraint fk_Livro
#            FOREIGN KEY (id_livro)
#            REFERENCES livros (id)
#            ON DELETE SET NULL
#            ON UPDATE NO ACTION

# );

def menuClientes(conexao):
    print("Lista de Clientes: ")
    resultado = conexao.consultarBanco('''
    Select * FROM Clientes
    ORDER BY id ASC
    ''')
    print("ID"/"Nome")
    for Cliente in resultado:
        print(f"{Cliente[0]} / {Cliente[1]}")

    print(f'''
    Escolha uma das opções:
    1. Ver cliente especifico
    2. Inserir novo cliente
    0. Voltar para o menu principal
    ''')
    opcoes = int(input("Digite o número da opcão desejada: "))
    match opcoes:
        case 1:
            while True:
                ClienteID = input("Digite o id do cliente")
                ClienteEscolhido = Cliente(ClienteID, None, None)
                resultado = conexao.consultarBanco(ClienteEscolhido.consultarClientePorID())
                if resultado != []:
                    ClienteEscolhido._nome = resultado[0][1]
                    ClienteEscolhido._cpf = resultado[0][2]
                    ClienteEscolhido._imprimirCliente()

                    while True:
                        print(f'''
                        Escolha uma das opções:
                        1. Ver alugueis
                        0. Voltar para o menu principal
                        ''')
                        opcoes = input("Digite o numero da opcap: ")
                        match opcoes:
                            case "1":
                                resultado = conexao.consultarBanco(ClienteEscolhido.consultarAlugueis())
                                if resultado != []:
                                    print("ID"/"Data")
                                    for aluguel in resultado:
                                        print(f"{aluguel[0]} / {aluguel[3]}")

                                else:
                                    print("Esse usuario nao possui alugueis")
                                input("Tecle ENTER para continuar")
                            case "0":
                                print("saindo do menu cliente")
                                break
                            case _:
                                print("voce escolheu uma opçao invalida")

                    break
                else:
                    print("voce escolheu um ID invalido")

while True:
    try:
        con = conexao("Biblioteca", "postgres", "postgres", "localhost", "5432")
        break

    except (Error) as error:
        print("Ocorreu um erro - ", error)

while True:
    try:
        print("Bem vindo a biblioteca 'Biblioteca dos Livros")

        print(f'''
    Escolha uma das opcoes:
    1. ver clientes
    2. ver livros
    3. ver alugueis
    0. sair

        ''')
        opcoes = input("Digite o número da opcao do menu:")
        
        match opcoes:
            case "1":
                menuClientes(con)
            case "2":
                print("Vendo livros")
            case "3":
                print("vendo alugueis")
            case "0":
                print("Saindo da aplicação...")
                break
            case _:
                print("voce digitou uma opcao invalida")

        input("pressione qualquer tecla para continuar")

        con.fechar

    except (Error) as error:
        print("Ocorreu um erro -", error)
