from datetime import datetime
import os
import platform
from typing import List
import questionary
from rich.table import Table
from rich.console import Console
from rich.align import Align
from questionary import select , confirm



class Endereco:
    def __init__(self):
        self.cidade: str = None
        self.pais: str = None


class Jogo:
    def __init__(self):
        self.titulo: str = None
        self.data_lancamento: date = None
        self.preco: float = None
        self.genero: str = None
        self.classificacao: str = None
        self.desenvolvedora: "Desenvolvedora" = None


class Desenvolvedora:
    def __init__(self):
        self.nome: str = None
        self.sede: Endereco = None
        self.proprietario: str = None
        self.jogos: List["Jogo"] = []


def exemplo_01():
    class Endereco:
        def __init__(self):
            self.cidade = None
            self.pais = None

    class Desenvolvedora:
        def __init__(self):
            self.nome = None
            self.proprietario = None
            self.sede = None
            self.jogos = []

    endereco_rockstar = Endereco()
    endereco_rockstar.cidade = "New York"
    endereco_rockstar.pais = "US"

    
    rockstar_games = Desenvolvedora()
    rockstar_games.nome = "Rockstar Games"
    rockstar_games.proprietario = "Take-Two Interactive"
    rockstar_games.sede = endereco_rockstar

    
    gta_vi = Jogo()
    gta_vi.titulo = "GTA VI"
    gta_vi.data_lancamento = date(2077, 2, 28)
    gta_vi.preco = 669.99
    gta_vi.genero = "Ação"
    gta_vi.classificacao = "M"
    gta_vi.desenvolvedora = rockstar_games

    the_witcher = Jogo()
    the_witcher.titulo = "The Witcher 4"
    the_witcher.data_lancamento = date(2077, 12, 31)
    the_witcher.preco = 500
    the_witcher.genero = "RPG"
    the_witcher.classificacao = "M"

    lol = Jogo()
    lol.titulo = "League of Legends"
    lol.data_lancamento = date(2009, 10, 27)
    lol.preco = 0
    lol.genero = "MOBA"
    lol.classificacao = "12"

   
    rockstar_games.jogos.append(gta_vi)
    rockstar_games.jogos.append(the_witcher)
    rockstar_games.jogos.append(lol)

    
    colunas = ["Título", "Lançamento", "Preço", "Gênero", "Classificação"]
    tabela = Table(*colunas)

    tabela.add_row(gta_vi.titulo, str(gta_vi.data_lancamento), str(gta_vi.preco), gta_vi.genero, gta_vi.classificacao)
    tabela.add_row(the_witcher.titulo, str(the_witcher.data_lancamento), str(the_witcher.preco), the_witcher.genero, the_witcher.classificacao)
    tabela.add_row(lol.titulo, str(lol.data_lancamento), str(lol.preco), lol.genero, lol.classificacao)

    console = Console()
    console.print(tabela)



class Marca:
    def __init__(self):
        self.id: int | None = None
        self.nome: str | None = None
        self.fundador: str | None = None
        self.data_fundacao: date | None = None
        self.faturamento: float | None = None


def exercicio_marca():
    puma = Marca()
    puma.id = 1
    puma.nome = "Puma"
    puma.fundador = "Rudolf Dassler"
    puma.data_fundacao = date(1948, 10, 1)
    puma.faturamento = 8.8

    umbro = Marca()
    umbro.id = 2
    umbro.nome = "Umbro"
    umbro.fundador = "Harold Humphreys"
    umbro.data_fundacao = date(1924, 1, 1)
    umbro.faturamento = 0.28

    colunas = ["ID", "Nome", "Fundador", "Data de Fundação", "Faturamento (bi)"]
    tabela = Table(*colunas)

    tabela.add_row(
        str(puma.id),
        puma.nome,
        puma.fundador,
        puma.data_fundacao.strftime("%d/%m/%Y"),
        f"{puma.faturamento:.2f}",
    )

    tabela.add_row(
        str(umbro.id),
        umbro.nome,
        umbro.fundador,
        umbro.data_fundacao.strftime("%d/%m/%Y"),
        f"{umbro.faturamento:.2f}",
    )

    console = Console()
    console.print(tabela)



def limpar_tela():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")


console = Console()
desenvolvedoras: List[desenvolvedora] = []

def menu_sistema():
    menu_geral = ""
    while menu_geral != "sair":
        menu_geral = questionary.select("Escolha o sistema", choices=["Desenvolvedora", "Sair"]).ask().lower()
        limpar_tela()
        if menu_geral == "desenvolvedora":
            exemplo_crud_lista_objetos()


def exemplo_crud_lista_objetos():
    menu = ""
    while menu != "sair":
        menu = questionary.select("Escolha o menu", choices=["Adicionar", "Listar", "Sair"]).ask().lower()
        limpar_tela()
        if menu == "adicionar":
            adicionar_desenvolvedora()
        elif menu == "listar":
            listar_desenvolvedoras()
        
# from rich.align import Align
 
def adicionar_desenvolvedora():
    # Solicitar os dados, instanciando um objeto de desenvolvedora e adicionar na lista
    console.print(Align.center("Cadastro de desenvolvedora"), style="blue")

    desenvolvedora = Desenvolvedora()
    desenvolvedora.nome = questionary.text("Digite o nome da desenvolvedora").ask()
    desenvolvedora.proprietario = questionary.text("Digite o nome do proprietário").ask()

    desenvolvedora.sede = Endereco()
    desenvolvedora.sede.cidade = questionary.text("Digite a cidade da sede").ask()
    desenvolvedora.sede.pais = questionary.text("Digite o país da sede").ask()

    desenvolvedoras.append(desenvolvedora)
    console.print("Desenvolvedora cadastrada com sucesso", style="green")
    input("Pressione ENTER para continuar...")
    limpar_tela()


def listar_desenvolvedoras():
    # Listar desenvolvedoras
    if len(desenvolvedoras) == 0:
        console.print("Nenhuma desenvolvedora cadastrada", style="red")
        input("Pressione ENTER para continuar...")
        limpar_tela()
        return

    table = Table("Nome", "Proprietário", "Endereço")

    for i in range(0, len(desenvolvedoras)):
        desenvolvedora = desenvolvedoras[i]
        table.add_row(
            desenvolvedora.nome,
            desenvolvedora.proprietario,
            f"{desenvolvedora.sede.pais} - {desenvolvedora.sede.cidade}"
        )
    
    
    console.print(table)

exemplo_crud_lista_objetos()



class Dono:
    def __init__(self):
        self.nome: str = None
        self.cpf: str = None
        self.bairro: str = None
        self.rua: str = None
        self.numero: str = None


class Animal:
    def __init__(self):
        self.raca: str = None
        self.dono: Dono = None
        self.data_nascimento: date = None
        self.peso: float = None
        self.altura: float = None
        self.sexo: str = None
        self.cor: str = None
        self.origem_raca: str = None
        


def cadastrar_animal():
    print("\nCadastro de Dono")
    dono = Dono()
    dono.nome = input("Digite o nome do dono: ")
    dono.cpf = input("Digite o CPF do dono: ")
    dono.bairro = input("Digite o bairro: ")
    dono.rua = input("Digite a rua: ")
    dono.numero = input("Digite o número: ")

    print("\nCadastro de Animal")
    animal = Animal()
    animal.raca = input("Digite a raça do animal: ")

    data = input("Digite a data de nascimento (DD/MM/AAAA): ")
    animal.data_nascimento = datetime.strptime(data, "%d/%m/%Y").date()

    animal.peso = float(input("Digite o peso do animal (kg): "))
    animal.altura = float(input("Digite a altura do animal (cm): "))
    animal.sexo = input("Digite o sexo do animal (M/F): ")
    animal.cor = input("Digite a cor do animal: ")
    animal.origem_raca = input("Digite a origem da raça: ")

    animal.dono = dono

    print("\nAnimal cadastrado com sucesso!\n")
    return animal


def mostrar_animal(animal: Animal):
    print("\nDADOS DO ANIMAL")
    print("Raça:", animal.raca)
    print("Data de nascimento:", animal.data_nascimento.strftime("%d/%m/%Y"))
    print("Peso:", str(animal.peso) + " kg")
    print("Altura:", str(animal.altura) + " cm")
    print("Sexo:", animal.sexo)
    print("Cor:", animal.cor)
    print("Origem da raça:", animal.origem_raca)

    print("\nDADOS DO DONO")
    print("Nome do dono:", animal.dono.nome)
    print("CPF:", animal.dono.cpf)
    print("Bairro:", animal.dono.bairro)
    print("Rua:", animal.dono.rua)
    print("Número:", animal.dono.numero)



