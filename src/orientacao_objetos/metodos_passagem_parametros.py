from typing import List

class Aluno:
    def __init__(
        sef,
        nome: str,
        notas: List[float],
        frequencia: float = 75,
        turma: str = "SuperDev",
    ):
        
        self.nome = nome
        self.notas  = notas
        self.frequencia = frequencia
        self.turma = turma

def exemplo_passagem_parametros_nomeados():
    # Pedro terá a freuqncoa de 75%, pq foi utilizado o volaor de default do
    # parametro de freuencia
    # 2 parâmetros seguindo a ordem do construtor e outro parâmetro pelo
    # nome (turma)
    pedro = Aluno(
        "Pedro Silva",
        [8,7,6.5],
        turma="SuperDev 7",
    )

    # Passando todos os parâmetro pelo nome, podendo passar em qualquer ordem
    maria = Aluno(
        notas=[10, 9.75, 3],
        nome="Maria",
        turma="Adas",
        frequencia=100,
    )

class Player:
    def __init__(
            self, 
            nick: str = "ShadowKiller", 
            classe: str = "Lutador", 
            lane: str = "Top", 
            elo: str = "Bronze", 
            maestria: int = 7, 
            main: str = "Zed"
            ):
        self.nick = nick
        self.classe = classe
        self.lane = lane
        self.elo = elo
        self.maestria = maestria
        self.main = main


def exercicio_player():
    astro = Player(
        nick="AstroBlade", 
        classe="Assassino", 
        lane="Mid"
    )
    luna = Player(
        nick="LunaFlash", 
        elo="Diamante"
    )
    pyro = Player(
        nick="PyroSoul"
    )
    titan = Player(
        nick="TitanBreaker",
        classe="Tanque",
        lane="Top",
        elo="Bronze",
        maestria=5
    )
    geraldinha = Player(
        nick="Grealdinha",
        classe="Suporte",
        main="Lulu",
        elo="Madeira"
    )
    jao = Player(
        nick="Jao",
        classe="Mago",
        lane="Mid",
        elo="Ferro",
        maestria=7,
        main="Anivia"
    )
    wudseven7 = Player(
        nick="Wudseven7",
        classe="Atirador",
        elo="Mestre"
        

    )

    table = Table("Nick", "Classe", "Lane", "Elo", "Maestria", "Main")

    for p in [astro, luna, pyro, titan, yuki, Jao, WudSeven7]:
        table.add_row(
            p.nick,
            p.classe,
            p.lane,
            p.elo,
            str(p.maestria),
            p.main
        )
    
    console = Console()
    console.print(table)


exercicio_player()

print("-----------------------------------------------------------------------")


class Produto:
    def __init__(
            self,
            preco: float, 
            nome: str="Sem nome", 
            categoria: str = "Geral", 
            estoque: int=0
            ):
        self.preco = preco
        self.nome = nome
        self.categoria = categoria
        self.estoque = estoque


def exercicio_02():
    cafe = Produto(
        nome="Café Torrado", 
        preco=18.90, 
        categoria="Mercearia", 
        estoque=120
    )
    chocolate = Produto(
        nome="Chocolate Amargo 70%", 
        preco=8.50, 
        categoria="Doces",
        estoque=50
    )

    table = Table("Produto", "Preço", "Categoria", "Estoque")

    for p in [cafe, chocolate]:
        table.add_row(
            p.nome,
            str(p.preco),
            p.categoria,
            str(p.estoque)
        )
    
    console = Console()
    console.print(table)


exercicio_02()

print("-----------------------------------------------------------------------")


class Carro:
    def __init__(
            self, 
            marca: str, 
            modelo: str, 
            ano: int, 
            cor: str="Branco", 
            portas: int=4, 
            motor: str="1.0", 
            cambio: str="Manual", 
            preco: float=0, 
            km: float=0, 
            usado: bool=False
            ):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.portas = portas
        self.motor = motor
        self.cambio = cambio
        self.preco = preco
        self.km = km
        self.usado = usado


def exercicio_03():
    picanto = Carro(
        marca="Kia",
        modelo="Picanto",
        ano=2009,
        cor="Laranja",
        portas=4,
        motor="1.0",
        cambio="Automático",
        preco=28500.00,
        km=145000,
        usado=True
    )
    civic = Carro(
        marca="Honda",
        modelo="Civic EXL",
        ano=2012,
        cor="Preto",
        portas=4,
        motor="1.8",
        cambio="Automático",
        preco=58000.00,
        km=98000,
        usado=True
    )

    table = Table(
        "Marca", "Modelo", "Ano", "Cor", "Portas", 
        "Motor", "Cambio", "Preço", "KM", "Usado"
    )

    for c in [picanto, civic]:
        table.add_row(
            c.marca,
            c.modelo,
            str(c.ano),
            c.cor,
            str(c.portas),
            c.motor,
            c.cambio,
            str(c.preco),
            str(c.km),
            str(c.usado)
        )

    console = Console()
    console.print(table)

