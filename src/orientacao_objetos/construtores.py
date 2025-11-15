class Cachorro:
    # Construtor com 4 parâmetros (3 parâmetros sem valor default e 1 com valor default)
    def __init__(self, raca_param: str, peso: float, idade: int , comr: str = "Caramelo"):
        # Atributos são preenchidos com os dados dos parâmetros
        # o parâmetro cor tem um valor default(padrão) que é "Caramelo"
        self.raca = raca_param
        self.peso = idade
        self.cor = cor
        # Atributo com valor pré-definido
        self.cidade_natal = "Blumenau"


def exemplo_construtor_cachorro():
    # Cachorro(raca, peso, idade)
    tobby = Cachorro("Dobberman", 45.20, 15, "Preto")
    print("raça:", tobby.raca)
    print("peso:", tobby.peso)
    print("idade:", tobby.idade)
    print("cidade natal:", tobby.cidade_natal)
    print("cor:", tobby.cor)

    daschund = Cachorro("Salsicha", 70.00, 5,)
    print("raça:", daschund.raca)
    print("peso:", daschund.peso)
    print("idade:", daschund.idade)
    print("cidade natal:", daschund.cidade_natal)
    print("cor:", daschund.cor)


class Passagem:
    def __init__(
        self,
        destino_param: str,
        quantidade_dias: int,
        data_inicio: date,
        quantidade_pessoas: int = 2,
        partida: str = "São Paulo"
    ):
        self.destino = destino
        self.quantidade_dias = quantidade_dias
        self.data_inicio = data_inicio
        self.quantidade_pessoas = quantidade_pessoas
        self.partida = partida


def apresentar_passagem(passagem: Passagem):
    print("\n-----------------------------")
    print("DESTINO:", passagem.destino)
    print("DIAS:", passagem.quantidade_dias)
    print("DATA INÍCIO:", passagem.data_inicio)
    print("PESSOAS:", passagem.quantidade_pessoas)
    print("PARTIDA:", passagem.partida)
    print("---------------------------------")


def exemplo_exercicio_passagem():
    print("- PASSAGEM 1 -")
    passagem1 = Passagem(
        "Rio de Janeiro",
        5,
        date(2025, 1, 15)
    )

    print("Destino:", passagem1.destino)
    print("Qtd Dias:", passagem1.qtd_dias)
    print("Data Início:", passagem1.data_inicio)
    print("Pessoas:", passagem1.quantidade_pessoas)
    print("Partida:", passagem1.partida)

    print("\n- PASSAGEM 2 -")
    passagem2 = Passagem(
        "Salvador",
        7,
        date(2025, 3, 10),
        4
    )

    print("Destino:", passagem2.destino)
    print("Qtd Dias:", passagem2.qtd_dias)
    print("Data Início:", passagem2.data_inicio)
    print("Pessoas:", passagem2.quantidade_pessoas)
    print("Partida:", passagem2.partida)

    print("\n- PASSAGEM 3 -")
    passagem3 = Passagem(
        "Florianópolis",
        3,
        date(2025, 5, 20),
        3,
        "Curitiba"
    )

    print("Destino:", passagem3.destino)
    print("Qtd Dias:", passagem3.qtd_dias)
    print("Data Início:", passagem3.data_inicio)
    print("Pessoas:", passagem3.quantidade_pessoas)
    print("Partida:", passagem3.partida)
