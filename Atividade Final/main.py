from Controle.Conexao import Conexao
from Modelo.Carro import Carro
from Modelo.Cliente import Cliente
from Modelo.Lista import Lista

from psycopg2 import Error

try:
  con = Conexao("Golf", "postgres", "123", "localhost", "5432")
    
  def mostrar(tipo):
    if tipo == "Carros":
      lista = con.consultaCompleta("Carros")
    elif tipo == "Clientes":
      lista = con.consultaCompleta("Clientes")
    for item in lista:
       print(f'''
            ID - {item[0]}
            Nome - {item[1]}
            ''')
          
    def mostrarListas(id_Clientes):
      listaDeColecoes = con.consultarBanco(f'''
                                        SELECT id, nome FROM lista
                                        WHERE id_cliente = '{id._Cliente}'
                                        ''')
        
    print("Sua lista de Listas")
    for colecao in listaDeColecoes:
          print(f'''
               ID - {lista[0]}
               Nome - {lista[1]}''')
          
    def listarLista(id_clientes, id_lista):
        listaCarros = con.consultarBanco(f'''
                                     SELECT lista_carros.id, carros.nome FROM lista_carros
                                      INNER JOIN lista
                                        ON lista_carros.id_carro = carros.id
                                      INNER JOIN carros
                                        ON lista_carros.id_carro = carros.id
                                      INNER JOIN clientes
                                        ON lista.id_clientes = clientes.id
                                      WHERE clientes.id = '{id_clientes}' AND lista_carros.id_lista = '{id_lista}
                                      ''')
        for carro in listaCarros:
         print(f"{carro[0]} - {carro[1]}")
    def inserirCarroNaLista(id_lista, id_carro):
      query = (f'''
              INSERT INTO lista_carros (id_listas, id_carro)
                VALUES('{id_lista}', '{id_carro}')
              ''')
      return query
    
    def deletarItemDaLista(id):
      query = (f'''
              DELETE FROM lista_carros
                WHERE id = '{id}'
              ''')
      return query
    
    def criarObjeto(acao, tabela, tipo): 
       escolha = int(input(f"Escolha pelo ID qual {tipo} você quer {acao}: "))
       opcaoEscolhida = con.consultarBanco(con.consultaPorId(tabela, escolha))
       if tipo == "carro":
          objetoCriado = Carro(opcaoEscolhida[0][0], opcaoEscolhida[0][1], opcaoEscolhida[0][2], opcaoEscolhida[0][3], opcaoEscolhida[0][4], opcaoEscolhida[0][5])
       elif tipo == "cliente":
          objetoCriado = Cliente(opcaoEscolhida[0][0], opcaoEscolhida[0][1], opcaoEscolhida[0][2], opcaoEscolhida[0][3], opcaoEscolhida[0][4], opcaoEscolhida[0][5])
       elif tipo == "Lista":
          objetoCriado = Lista(opcaoEscolhida[0][0], opcaoEscolhida[0][1], opcaoEscolhida[0][2])
       return objetoCriado
    
    def gerarMenu(titulo, campos):
       print(f'''
           MENU {titulo}
Escolha o que voce deseja fazer''')
    for i in range(len(campos)):
       print(f"{i+1} - {campos[i]}")
    print("0 - Sair")
    escolhaMenuGerado = int(input("Digite o número da opção escolhida: "))
    return escolhaMenuGerado

while True:
   escolhaMenuPrincipal = gerarMenu("PRINCIPAL, ["Manipular carros", "Manipular clientes", "Manipular listas"])
   match escolhaMenuPrincipal:
     case 0:
       break
       
    case 1:
    
      while True:
      escolhaMenuCarros = gerarMenu("DE CARROS", ["Inserir novo carro", "ver carro", "mudar carro", "excluir carro"])
      match escolhaMenuCarros:
        case 0:
          break
        case 1:
          novoCarro = Carro(None, input("Nome: "), input("Numero de lugares"), input("Ano"), input("Modelo"))
          con.manipularBanco(novoCarro.inserirCarro())
          print("Carro cadastrado com sucesso")
        case 2:
          mostrar("Carros")
          novoObjeto = criarObjeto(acao = "atualizar", tabela = "carros", tipo = "carro")
          novoObjeto.visualizarCarro()
        case 3:
          mostrar("Carros")
          novoObjeto = criarObjeto(acao = "atualizar", tabela = "carros", tipo = "carro")
          escolhaMenu = gerarMenu("DE CAMPOS", ["Nome", "Número de lugares", "ano", "modelo"])
          match escolhaMenu:
            case 1:
              novoObjeto.setNome(input("Digite o novo nome: "))
            case 2:
              novoObjeto.setNumLugares(input("Digite o novo número de lugares: "))
            case 3:
              novoObjeto.setAno(input("Digite o novo ano"))
            case 4:
              novoObjeto.setModelo(input("Digite o novo modelo"))
          con.manipularBanco(novoObjeto.atualizarCarro())
          print("Carro atualizado com sucesso")
        case 4:
          mostrar("carros")
          novoObjeto = criarObjeto(acao = "deletar", tabela = "carros", tipo = "carro")
          con.manipularBanco(novoObjeto.deletarCarro())
          print("carro deletado com sucesso")

    case 2:
    
      while True:
        escolhaMenuClientes = gerarMenu ("DE CLIENTES", ["inserir novo cliente", "visualizar cliente", "atualizar cliente", "deletar cliente"])
        match escolhaMenuClientes:
          case 0:
            break
          case 1:
            novoCliente = Cliente(None, input("Nome: "), input("cpf: "))
            con.manipularBanco(novoCliente.inserirCarro())
            print("Carro cadastrado com sucesso")
          case 2:
            mostrar("Carros")
            novoObjeto = criarObjeto(acao = "visualizar", tabela = "clientes", tipo = "cliente")
            novoObjeto.visualizarCliente()
          case 3:
            mostrar("Clientes")
            novoCliente = criarCliente(acao = "atualizar", tabela = "clientes", tipo = "cliente")
            escolhaMenu = gerarMenu("DE CAMPOS", ["Nome", "cpf"])
            match escolhaMenu:
              case 1:
                novoObjeto.setNome(input("digite o novo nome: "))
              case 2:
                novoObjeto.setcpf(input("digite o novo cpf: "))
            con.manipularBanco(novoObjeto.atualizarCliente())
            print("Cliente atualizado com sucesso")

          case 4:
            mostrar("Cliente")
            novoObjeto = criarObjeto(acao = "deletar", tabela = "clientes", tipo = "cliente")
            con.manipularBanco(novoObjeto.deletarCliente())
            print("cliente deletado com sucesso")

    case 3:
      
      while True:
        escolhaMenuLista = gerarMenu("DO CLIENTE", ["Criar lista", "visualizar listas", "deletar da lista"])
        match escolhaMenuLista:
          case 0:
            break
          case 1:
            novaLista = Lista(None, id_cliente, input("Nome: "))
            con.manipularBanco(novaLista.inserirLista())
            print("Lista cadastrada com sucesso: ")
          case 2:
            print("suas listas existentes: ")
            mostrarListas(id_cliente)
          case 3:
            mostrarListas(id_cliente)
            listaEditar = criarObjeto(acao = "atualizar", tabela = "lista", tipo = "lista")
            while True:
              escolhaLista = gerarMenu("DA LISTA", ["Inserir item na lista", "visualizar item da litsa", "deletar item da lista"])
              match escolhaLista:
                case 0:
                  break
                case 1:
                  mostrar("Carros")
                  id_carro = int(input("escolha pelo ID qual carro voce quer inserir na sua lista"))
                  con.manipularBanco(inserirCarroNaLista(listaEditar.id. id_carrp))
                  print("Item na coleção adicionado com sucesso. ")
                case 2:
                  print("sua lista: ")
                  listarLista(id_cliente, listaEditar.id)
                case 3:
                  print("sua lista: ")
                  listarLista(id_cliente, listaEditar.id)
                  id_item = int(input("escolha pelo ID qual item da sua lista voce quer deletar: "))
                  con.manipularBanco(deletarItemDaLista(id_item))
                  print("Lista atualizada com sucesso")
            case 4:
              mostrarListas(id_cliente)
              listaExcluir = criarObjeto(acao = "deletar", tabela = "lista", tipo = "lista")
              con.manipularBanco(listaExcluir.deletarLista())
except(Error) as error:
  print("Ocorreu um erro", error)
          



    
