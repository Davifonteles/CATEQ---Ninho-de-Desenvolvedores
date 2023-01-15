import random 

class Pokemon:  
    def __init__(self, nome, especie, tipo, ataque, defesa, hp, especial):
        self._nome = nome 
        self._especie = especie 
        self._tipo = tipo
        self._ataque = ataque
        self._defesa = defesa
        self._hp = hp
        self._movimento = "Ataque rapido"
        self._especial = especial


class Aquatico(Pokemon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp, especial):
        super().__init__(nome, especie, tipo, ataque, defesa, hp, especial)
        self._tipo = "aquatico"
        self._movimento = "Jato de água"

        
class Fogo(Pokemon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp, especial):
        super().__init__(nome, especie, tipo, ataque, defesa, hp, especial)
        self._tipo = "fogo"
        self._movimento = "Lança chamas"

       
class Grama(Pokemon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp, especial):
        super().__init__(nome, especie, tipo, ataque, defesa, hp, especial)
        self._tipo = "grama"
        self._movimento = "Chicote de cipó"

class Eletrico(Pokemon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp, especial):
        super().__init__(nome, especie, tipo, ataque, defesa, hp, especial)
        self._tipo = "eletrico"
        self._movimento = "Carga selvagem"

class Gelo(Pokemon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp, especial):
        super().__init__(nome, especie, tipo, ataque, defesa, hp, especial)
        self._tipo = "gelo"
        self._movimento = "Queda de gelo"

class Lutador(Pokemon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp, especial):
        super().__init__(nome, especie, tipo, ataque, defesa, hp, especial)
        self._tipo = "lutador"
        self._movimento = "Corpo a corpo"
        self._especial = "Soco dos Céus"

class Psíquico(Pokemon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp, especial):
        super().__init__(nome, especie, tipo, ataque, defesa, hp, especial)
        self._tipo = "psíquico"
        self._movimento = "Presas psíquicas"


class Treinador:
    def __init__(self, nome, pokemons):
        self._nome = nome
        self._pokemons = pokemons

    def escolherPokemon(self):
        return random.choice(self._pokemons)

class Jogador(Treinador):
    def __init__(self, nome, pokemons):
        super().__init__(nome, pokemons)

    def escolherPokemon(self):
        while True:
            print(f"Escolha seu pokemon: ")

            for i in range(len(self._pokemons)):
                print(f"{i+1}. {self._pokemons[i]._nome}")

            pokemonEscolhido = input("Digite o número do pokemon escolhido: ")

            if (pokemonEscolhido.isnumeric()):
                if (int(pokemonEscolhido) <= len(self._pokemons)):
                    return self._pokemons[int(pokemonEscolhido)-1]
                else:
                    print("Você escreveu um número maior do que o disponível.")
            else: 
                print("Você escreveu um caractere inválido")

    def capturarPokemon(self, pokemonCapturado): 
        self._pokemons.append(pokemonCapturado)
        print(f"Você capturou o {pokemonCapturado._nome}")
    
    def listarPokemons(self): 
        print("Sua lista de pokemons: ")
        for i in range(len(self._pokemons)):
                print(f"{i+1}. {self._pokemons[i]._nome}")

         

class Inimigo(Treinador):
    def __init__(self, nome, pokemons):
        super().__init__(nome, pokemons)

    
def batalhaPokemon(treinador1, treinador2): 

    p1 = treinador1.escolherPokemon()
    p2 = treinador2.escolherPokemon()

    p1Forca = (p1._ataque + p1._defesa + p1._hp + p1._especial) * random.randint(1,3)
    p2Forca = (p2._ataque + p2._defesa + p2._hp + p2._especial) * random.randint(1,3)

    print(f"{p1._nome} atacou com {p1._movimento} e com especial {p1._especial} e força {p1Forca}")
    print(f"{p2._nome} atacou com {p2._movimento} e com especial {p2._especial} e força {p2Forca}")

    if (p1Forca > p2Forca):
        print(f"O vencedor foi {p1._nome} com força {p1Forca} do treinador {treinador1._nome}")
    elif (p1Forca < p2Forca):
        print(f"O vencedor foi {p2._nome} com força {p2Forca} do treinador {treinador2._nome}")
    else:
        print("Deu empate")

pokemonsDisponiveis = [
Fogo("Charmander", "Charmander", "Fogo", 250,100,150,600),
Fogo("Charmeleon", "Charmeleon", "Fogo", 350, 300, 350,1000),
Grama("Bulbasauro", "Bulbasauro", "Grama",200,100,150,500),
Grama("Ivysauro", "Ivysauro", "Grama",350,150,350,800),
Aquatico("Wartortle", "Wartortle", "Aquatico",300,100,150,450),
Aquatico("Marill", "Marill", "Aquatico", 300,150,100,600),
Eletrico("Pikachu", "Pikachu", "Eletrico", 300,100,200,1000),
Eletrico("Raichu", "Raichu", "Eletrico", 450,200,400,2000),
Gelo("Vulpix", "Vulpix", "Gelo", 350,200,300,500),
Gelo("Glaceon", "Glaceon", "Gelo", 300,300,400,2000),
Lutador("Machop", "Machop", "Lutador", 150,100,200,1000),
Lutador("Machamp","Machamp", "Lutador", 300,250,300,2000),
Psíquico("Abra", "Abra", "Psíquico", 200,150,300,500),
Psíquico("Alakazam", "Alakazam", "Psíquico", 350,250,400,1500)

]


nomeJogador = input("Digite seu nome: ")

print("Escolha seu Pokemon inicial: ")

for i in range(3):
    print(f"{i+1}. {pokemonsDisponiveis[i]._nome}")

pokemonInicial = pokemonsDisponiveis[int(input("Digite o pokemon escolhido: "))-1]

print(f"O pokemon escolhido foi o {pokemonInicial._nome}")

jogador = Jogador(nomeJogador, [pokemonInicial])
inimigo = Inimigo("Manoel Gomes", pokemonsDisponiveis)

while True:

    print("""
    Escolha o que você quer fazer:
    1. Ver seus Pokemons
    2. Capturar um novo Pokemon
    3. Batalhar contra um oponente
    0. Sair do jogo
    """)

    menu = input("Digite a opção escolhida:")

    if menu =="0":
        print("Você saiu do jogo.")
        break
    elif menu=="1":
        jogador.listarPokemons()
    elif menu=="2":
        print("Escolha um pokemon para capturar: ")

        for i in range(len(pokemonsDisponiveis)):
            print(f"{i+1}. {pokemonsDisponiveis[i]._nome}")
        
        capturado = pokemonsDisponiveis[int(input("Digite o pokemon escolhido: "))-1]
        jogador.capturarPokemon(capturado)
    elif menu=="3":
        batalhaPokemon(jogador,inimigo)
    else:
        print("Você digitou algo inválido, tente novamente.")